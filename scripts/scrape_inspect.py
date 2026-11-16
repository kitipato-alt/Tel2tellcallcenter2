import sys
import requests
from bs4 import BeautifulSoup
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.tel2tellcallcenter.com/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.content, 'html.parser')

print("=== META TAGS ===")
for m in soup.find_all('meta'):
    print(m.attrs)

print("\n=== STYLESHEETS ===")
for link in soup.find_all('link', rel='stylesheet'):
    print(link.get('href'))

print("\n=== FONTS ===")
for link in soup.find_all('link'):
    if 'font' in str(link.get('href', '')).lower():
        print(link.get('href'))

print("\n=== IMAGES ===")
images = []
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    alt = img.get('alt', '')
    if src:
        images.append({'src': src, 'alt': alt})
print(f"Total images on homepage: {len(images)}")
for img in images[:15]:
    print(f"  {img['src']} | alt: {img['alt']}")

print("\n=== ALL TEXTS BY CONTAINER / SECTION ===")
# Let's inspect direct children of body or main content wrappers
body = soup.body
if body:
    # Look for top-level divs/sections
    for child in body.children:
        if child.name:
            text = child.get_text(separator=' ', strip=True)
            if len(text) > 0:
                print(f"TAG: <{child.name} id='{child.get('id', '')}' class='{child.get('class', '')}'> Length: {len(text)}")
                print(f"PREVIEW: {text[:150]}...\n")
