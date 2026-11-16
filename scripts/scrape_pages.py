import sys
import requests
from bs4 import BeautifulSoup
import json
import os

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

pages_to_scrape = [
    {"name": "Home", "url": "https://www.tel2tellcallcenter.com/"},
    {"name": "Outbound Callcenter", "url": "https://www.tel2tellcallcenter.com/outbond-callcenter"},
    {"name": "VDO Production", "url": "https://www.tel2tellcallcenter.com/vdoproduction2"},
    {"name": "Sales Admin", "url": "https://www.tel2tellcallcenter.com/salesadmin"},
    {"name": "Work with us (Jobs)", "url": "https://www.tel2tellcallcenter.com/tel2telljobs"},
    {"name": "Form Admin", "url": "https://www.tel2tellcallcenter.com/form/15/สมัครงาน-admin"},
    {"name": "Form Telesales", "url": "https://www.tel2tellcallcenter.com/form/16/สมัครงาน-telesales"},
    {"name": "Form Call Center", "url": "https://www.tel2tellcallcenter.com/form/22/สมัครงาน-callcenter"},
    {"name": "Form TV Program", "url": "https://www.tel2tellcallcenter.com/form/62/สนใจออกรายการทีวี-"},
    {"name": "Gallery", "url": "https://www.tel2tellcallcenter.com/gallery/5233/ภาพบรรยากาศการทำงาน"},
    {"name": "Privacy Policy", "url": "https://www.tel2tellcallcenter.com/privacy-policy"},
    {"name": "Cookies Policy", "url": "https://www.tel2tellcallcenter.com/cookies-policy"}
]

os.makedirs('scraped_data', exist_ok=True)

scraped_summary = []

for page in pages_to_scrape:
    try:
        r = requests.get(page['url'], headers=headers, timeout=15)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        # Title & Meta
        title = soup.title.string.strip() if soup.title else ""
        meta_desc = ""
        m = soup.find('meta', attrs={'name': 'description'})
        if m:
            meta_desc = m.get('content', '')
            
        # Extract headings
        headings = []
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            t = h.get_text(strip=True)
            if t:
                headings.append(f"<{h.name}> {t}")
                
        # Extract main text
        body = soup.find('div', class_='section-body') or soup.find('div', class_='section-container') or soup.body
        # remove script and style
        for s in body.find_all(['script', 'style', 'noscript']):
            s.decompose()
            
        clean_text = body.get_text(separator='\n', strip=True)
        
        # Images
        imgs = []
        for img in body.find_all('img'):
            src = img.get('data-src') or img.get('src')
            alt = img.get('alt', '')
            if src and not src.startswith('data:'):
                imgs.append({'src': src, 'alt': alt})
                
        # Forms
        forms_info = []
        for form in body.find_all('form'):
            f_inputs = []
            for inp in form.find_all(['input', 'textarea', 'select']):
                f_inputs.append({
                    'type': inp.get('type', inp.name),
                    'name': inp.get('name', ''),
                    'placeholder': inp.get('placeholder', ''),
                    'id': inp.get('id', '')
                })
            forms_info.append({'action': form.get('action', ''), 'inputs': f_inputs})
            
        page_data = {
            "name": page['name'],
            "url": page['url'],
            "title": title,
            "meta_description": meta_desc,
            "headings": headings,
            "images": imgs,
            "forms": forms_info,
            "text": clean_text
        }
        
        file_slug = page['name'].lower().replace(' ', '_').replace('(', '').replace(')', '')
        with open(f"scraped_data/{file_slug}.json", 'w', encoding='utf-8') as f:
            json.dump(page_data, f, ensure_ascii=False, indent=2)
            
        print(f"Scraped '{page['name']}': status {r.status_code}, headings: {len(headings)}, imgs: {len(imgs)}, text len: {len(clean_text)}")
        scraped_summary.append({
            "name": page['name'],
            "url": page['url'],
            "title": title,
            "headings_count": len(headings),
            "text_len": len(clean_text)
        })
    except Exception as e:
        print(f"Error scraping {page['url']}: {e}")

print("\nDone scraping main pages!")
