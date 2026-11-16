import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('homepage_sections.json', 'r', encoding='utf-8') as f:
    sections = json.load(f)

for idx in [7, 8, 9, 10, 11, 13, 14, 15]:
    sec = sections[idx - 1]
    print(f"\n=============================================")
    print(f"DETAILED SECTION #{idx}")
    print(f"=============================================")
    print("Headings:", sec['headings'])
    print("Images:", [img['src'] for img in sec['images']])
    print("Text:")
    print(sec['full_text'])
