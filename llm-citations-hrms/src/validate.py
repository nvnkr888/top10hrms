# src/validate.py
import re
import json

s = open('results/top10_hrms_india.md', 'r', encoding='utf-8').read()
ids = set(re.findall(r"\[\[SRC:(\d+)\]\]", s))

sources = {json.loads(line)['id'] for line in open('data/sources.jsonl', 'r', encoding='utf-8')}
missing = ids - sources
if missing:
    raise SystemExit('Missing source ids: ' + ','.join(sorted(missing)))
print('All citations valid')
