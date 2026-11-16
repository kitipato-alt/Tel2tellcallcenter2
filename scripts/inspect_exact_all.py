import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup

url = 'https://www.tel2tellcallcenter.com/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.content, 'html.parser')

content_sec = soup.find('div', id='section-content')
children = content_sec.find_all(['section', 'div'], recursive=False)

for idx, c in enumerate(children):
    text = c.get_text(separator=' ', strip=True)
    imgs = [img.get('data-src') or img.get('src') for img in c.find_all('img')]
    print(f"\n==========================================")
    print(f"ORIGINAL SEC #{idx+1}")
    print(f"==========================================")
    print("STYLE:", c.get('style'))
    print("IMGS:", imgs)
    print("TEXT:", text[:250])
