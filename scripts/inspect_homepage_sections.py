import sys
import requests
from bs4 import BeautifulSoup
import json

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.tel2tellcallcenter.com/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.content, 'html.parser')

content_sec = soup.find('div', id='section-content')
if not content_sec:
    print("No section-content found")
    sys.exit(0)

# Find all direct child sections/divs inside section-content
child_sections = content_sec.find_all(['section', 'div'], recursive=False)
print(f"Total direct children in #section-content: {len(child_sections)}")

sections_data = []

for idx, child in enumerate(child_sections):
    cid = child.get('id', '')
    classes = child.get('class', [])
    
    # Try finding sub-sections if this child is a wrapper
    sub_sections = child.find_all(['section', 'div'], recursive=False)
    
    # Extract headings
    headings = []
    for h in child.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        headings.append(f"{h.name}: {h.get_text(strip=True)}")
        
    # Extract images
    imgs = []
    for img in child.find_all('img'):
        src = img.get('data-src') or img.get('src')
        alt = img.get('alt', '')
        if src and not src.startswith('data:'):
            imgs.append({'src': src, 'alt': alt})
            
    # Extract links and buttons
    links = []
    for a in child.find_all('a'):
        txt = a.get_text(strip=True)
        href = a.get('href', '')
        if txt or href:
            links.append({'text': txt, 'href': href})
            
    # Text paragraphs
    paragraphs = []
    for p in child.find_all(['p', 'span', 'li', 'div']):
        # only keep if it has direct text
        t = p.get_text(strip=True)
        # we can collect distinct texts
        
    full_text = child.get_text(separator='\n', strip=True)
    
    sec_info = {
        'index': idx + 1,
        'tag': child.name,
        'id': cid,
        'class': classes,
        'headings': headings,
        'image_count': len(imgs),
        'images': imgs,
        'link_count': len(links),
        'links': links,
        'full_text': full_text
    }
    sections_data.append(sec_info)
    
    print(f"\n=======================================================")
    print(f"SUBSECTION #{idx+1} [id='{cid}', class='{' '.join(classes)}']")
    print(f"=======================================================")
    print("HEADINGS:", headings)
    print(f"IMAGES ({len(imgs)}):", [img['src'] for img in imgs[:4]])
    print(f"LINKS ({len(links)}):", [(l['text'], l['href']) for l in links[:5]])
    print("TEXT PREVIEW:")
    print(full_text[:300])

with open('homepage_sections.json', 'w', encoding='utf-8') as f:
    json.dump(sections_data, f, ensure_ascii=False, indent=2)
print("\nSaved to homepage_sections.json")
