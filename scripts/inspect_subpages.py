import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

for name in ['outbound_callcenter', 'vdo_production', 'sales_admin', 'work_with_us_jobs', 'form_telesales', 'form_admin', 'form_call_center', 'form_tv_program']:
    try:
        with open(f'scraped_data/{name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"\n=======================================================")
        print(f"PAGE: {data['name']} ({data['url']})")
        print(f"TITLE: {data['title']}")
        print(f"HEADINGS: {data['headings']}")
        print(f"FORMS: {data['forms']}")
        print("--- CONTENT TEXT PREVIEW ---")
        print(data['text'][:1000])
        print("...")
    except Exception as e:
        print(f"Error {name}: {e}")
