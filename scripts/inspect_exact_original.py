import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.tel2tellcallcenter.com/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.content, 'html.parser')

body_sec = soup.find('div', class_='section-body')
content_sec = soup.find('div', id='section-content')

print("Header HTML:")
hdr = soup.find('div', id='section-header')
if hdr:
    print(hdr.prettify()[:1000])

print("\nSections in #section-content:")
if content_sec:
    children = content_sec.find_all(['section', 'div'], recursive=False)
    for i, c in enumerate(children):
        style = c.get('style', '')
        bg = re.findall(r'background(?:-color)?:\s*([^;]+)', style)
        print(f"\n--- Section #{i+1} [class='{' '.join(c.get('class', []))}'] bg={bg} ---")
        # Headings
        for h in c.find_all(['h1', 'h2', 'h3', 'h4']):
            print(f"  {h.name}: {h.get_text(strip=True)} | style: {h.get('style', '')}")
        # Images
        for img in c.find_all('img'):
            src = img.get('data-src') or img.get('src')
            print(f"  IMG: {src}")
