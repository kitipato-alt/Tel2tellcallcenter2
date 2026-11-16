import sys
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

r = requests.get('https://www.tel2tellcallcenter.com/sitemap.xml', headers=headers)
root = ET.fromstring(r.content)
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

content_urls = []
for url in root.findall('s:url', ns):
    loc = url.find('s:loc', ns)
    if loc is not None and '/content/' in loc.text:
        content_urls.append(loc.text)

print(f"Total articles found in sitemap: {len(content_urls)}")

os.makedirs('scraped_data/articles', exist_ok=True)

articles = []

for idx, curl in enumerate(content_urls):
    try:
        res = requests.get(curl, headers=headers, timeout=15)
        if res.status_code != 200:
            print(f"[{idx+1}/{len(content_urls)}] Failed {curl} ({res.status_code})")
            continue
            
        sp = BeautifulSoup(res.content, 'html.parser')
        
        title = sp.title.string.strip() if sp.title else ""
        
        # Meta description
        meta_desc = ""
        m = sp.find('meta', attrs={'name': 'description'})
        if m:
            meta_desc = m.get('content', '')
            
        # Try to find article content container
        # In MakeWebEasy, article content is usually in .content-detail, or .box-content, or #section-content
        art_container = sp.find('div', class_='box-content') or sp.find('div', class_='content-detail') or sp.find('div', id='section-content')
        
        # Let's clean scripts and styles
        if art_container:
            for s in art_container.find_all(['script', 'style', 'noscript']):
                s.decompose()
            body_text = art_container.get_text(separator='\n', strip=True)
        else:
            body_text = ""
            
        # Extract images in article
        imgs = []
        if art_container:
            for img in art_container.find_all('img'):
                src = img.get('data-src') or img.get('src')
                alt = img.get('alt', '')
                if src and not src.startswith('data:'):
                    imgs.append({'src': src, 'alt': alt})
                    
        # Article Headings
        headings = []
        if art_container:
            for h in art_container.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                headings.append(f"<{h.name}> {h.get_text(strip=True)}")
                
        # Slug/ID
        slug_match = re.search(r'/content/(\d+)/(.*)', curl)
        art_id = slug_match.group(1) if slug_match else str(idx)
        slug_name = slug_match.group(2) if slug_match else f"art_{idx}"
        
        art_data = {
            "id": art_id,
            "slug": slug_name,
            "url": curl,
            "title": title,
            "meta_description": meta_desc,
            "headings": headings,
            "images": imgs,
            "body_text": body_text
        }
        
        articles.append(art_data)
        
        safe_filename = re.sub(r'[\\/*?:"<>|]', '_', f"{art_id}_{slug_name[:40]}")
        with open(f"scraped_data/articles/{safe_filename}.json", 'w', encoding='utf-8') as f:
            json.dump(art_data, f, ensure_ascii=False, indent=2)
            
        print(f"[{idx+1}/{len(content_urls)}] Saved {art_id}: {title[:35]} (text len: {len(body_text)})")
    except Exception as e:
        print(f"[{idx+1}/{len(content_urls)}] Error {curl}: {e}")

with open("scraped_data/all_articles.json", 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"\nAll {len(articles)} articles saved successfully!")
