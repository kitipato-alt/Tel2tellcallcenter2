import sys
import json
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

with open('scraped_data/all_articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

print(f"Total articles loaded: {len(articles)}")

categories = defaultdict(list)
for a in articles:
    t = a['title'].lower()
    if any(k in t for k in ['vdo', 'video', 'วิดีโอ', 'วีดีโอ', 'production']):
        categories['VDO & Production'].append(a)
    elif any(k in t for k in ['event', 'อีเว้นท์', 'อีเวนต์']):
        categories['Event Production'].append(a)
    elif any(k in t for k in ['telesales', 'tele-sales', 'tele sale', 'sales admin', 'ขายทางโทรศัพท์', 'ยอดขาย']):
        categories['Telesales & Sales Admin'].append(a)
    elif any(k in t for k in ['รางวัล', 'award', 'tccta', '1668', 'บริจาค', 'ช่วยเหลือ', 'ทำบุญ', 'บวงสรวง', 'กิจกรรม', 'party']):
        categories['CSR, Awards & Company News'].append(a)
    elif any(k in t for k in ['fulfilment', 'fulfillment', 'logistics', 'คลังสินค้า']):
        categories['Logistics & Fulfillment'].append(a)
    else:
        categories['Call Center Knowledge & Insights'].append(a)

for cat, arts in categories.items():
    print(f"\n=== CATEGORY: {cat} ({len(arts)} articles) ===")
    for a in arts[:8]:
        print(f"  * [{a['id']}] {a['title'][:60]}")
    if len(arts) > 8:
        print(f"  ... and {len(arts) - 8} more")
