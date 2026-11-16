import sys
import requests
from bs4 import BeautifulSoup
import json

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.tel2tellcallcenter.com/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.content, 'html.parser')

container = soup.find('div', class_='section-container')
if not container:
    print("No section-container found")
    sys.exit(0)

sections = container.find_all(['section', 'div'], recursive=False)
print(f"Total top-level children in section-container: {len(sections)}")

for i, sec in enumerate(sections):
    sec_id = sec.get('id', '')
    sec_class = ' '.join(sec.get('class', []))
    print(f"\n==========================================")
    print(f"SECTION #{i+1}: tag=<{sec.name}> id='{sec_id}' class='{sec_class}'")
    print(f"==========================================")
    
    # Check headlines
    headings = [h.get_text(strip=True) for h in sec.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    if headings:
        print("HEADINGS:", headings)
        
    # Check text
    text = sec.get_text(separator='\n', strip=True)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    print(f"TEXT LINES ({len(lines)} lines):")
    for line in lines[:20]:
        print("  -", line)
    if len(lines) > 20:
        print(f"  ... and {len(lines) - 20} more lines")

    # Check images
    imgs = sec.find_all('img')
    if imgs:
        print(f"IMAGES ({len(imgs)}):")
        for img in imgs[:5]:
            src = img.get('data-src') or img.get('src')
            alt = img.get('alt', '')
            print(f"  img: src='{src}' alt='{alt}'")
