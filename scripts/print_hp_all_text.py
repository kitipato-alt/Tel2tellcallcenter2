import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('homepage_sections.json', 'r', encoding='utf-8') as f:
    sections = json.load(f)

for s in sections:
    txt = s['full_text'].strip()
    if txt:
        print(f"=== SECTION {s['index']} ({s['headings']}) ===")
        print(txt)
        print("-" * 40)
