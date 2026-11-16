import sys
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.tel2tellcallcenter.com/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.content, 'html.parser')

body_sec = soup.find('div', class_='section-body')
for i, child in enumerate(body_sec.find_all(['section', 'div'], recursive=False)):
    classes = child.get('class', [])
    cid = child.get('id', '')
    print(f"\n=======================================================")
    print(f"BODY CHILD #{i+1}: <{child.name}> id='{cid}' class='{' '.join(classes)}'")
    print(f"=======================================================")
    
    # Check inner content summary
    h_tags = child.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    if h_tags:
        print("HEADINGS:", [h.get_text(strip=True) for h in h_tags])
        
    # All paragraphs or text blocks
    text_content = child.get_text(separator=' | ', strip=True)
    print("TEXT PREVIEW:", text_content[:400])
    
    # Check images inside
    imgs = child.find_all('img')
    print(f"IMG COUNT: {len(imgs)}")
    for img in imgs[:5]:
        src = img.get('data-src') or img.get('src')
        alt = img.get('alt')
        print(f"  - img: {src} (alt: {alt})")
