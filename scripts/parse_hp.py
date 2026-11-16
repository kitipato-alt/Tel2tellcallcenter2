import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('homepage_sections.json', 'r', encoding='utf-8') as f:
    sections = json.load(f)

print(f"Loaded {len(sections)} homepage sections:")
for sec in sections:
    print(f"\n--- Section #{sec['index']} (id='{sec['id']}', class='{sec['class']}') ---")
    if sec['headings']:
        print("HEADINGS:", sec['headings'])
    if sec['images']:
        print(f"IMAGES ({len(sec['images'])}):")
        for im in sec['images'][:3]:
            print("  *", im['src'], "|", im['alt'])
    lines = [line.strip() for line in sec['full_text'].split('\n') if line.strip()]
    if lines:
        print(f"TEXT ({len(lines)} lines):")
        for l in lines[:10]:
            print("  >", l)
        if len(lines) > 10:
            print(f"  ... (+ {len(lines) - 10} lines)")
