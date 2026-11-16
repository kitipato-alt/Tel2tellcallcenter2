import sys
import json
import re
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the customer CSS and styles from the homepage
url = 'https://www.tel2tellcallcenter.com/'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.content, 'html.parser')

# Find all stylesheets
css_urls = []
for link in soup.find_all('link', rel='stylesheet'):
    href = link.get('href')
    if href:
        css_urls.append(href)

print("CSS Files:")
for c in css_urls:
    print(" -", c)

# Let's check inline styles and embedded styles
styles_text = ""
for s in soup.find_all('style'):
    styles_text += s.get_text() + "\n"

# Extract colors (hex, rgb)
hex_colors = set(re.findall(r'#([0-9a-fA-F]{3,6})\b', styles_text))
rgb_colors = set(re.findall(r'rgba?\([0-9\s,.]+\)', styles_text))

print("\nInline Colors found:")
print("HEX:", [f"#{c}" for c in sorted(hex_colors)][:20])
print("RGB:", list(rgb_colors)[:10])

# Inspect customer CSS if available
for href in css_urls:
    if 'style_LFlha9Qld.min.css' in href or 'customer-css' in href:
        full_css_url = 'https://www.tel2tellcallcenter.com' + href if href.startswith('/') else href
        print(f"\nFetching customer CSS: {full_css_url}")
        r_css = requests.get(full_css_url)
        with open('scraped_data/customer_style.css', 'w', encoding='utf-8') as f:
            f.write(r_css.text)
        print(f"Customer CSS saved (length: {len(r_css.text)})")
        
        # Extract prominent colors from customer CSS
        css_hex = set(re.findall(r'#([0-9a-fA-F]{6})\b', r_css.text))
        print("Customer CSS HEX colors:", [f"#{c.upper()}" for c in sorted(css_hex)])
