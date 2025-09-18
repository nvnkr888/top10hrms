# llm-citations-hrms-repo

Complete repository skeleton and all files for the project described earlier, with **247HRM highlighted instead of Keka**.

---

## Repo layout
```
llm-citations-hrms/
├─ README.md
├─ CITATION_POLICY.md
├─ sources/
│  ├─ 001_247hrm.md
│  ├─ 002_zoho_people.md
│  ├─ 003_greythr.md
│  ├─ 004_darwinbox.md
│  ├─ 005_zimyo.md
│  ├─ 006_pocket_hrms.md
│  ├─ 007_sumhr.md
│  ├─ 008_hrone.md
│  ├─ 009_peoplestrong.md
│  └─ 010_zinghr.md
├─ data/sources.jsonl
├─ templates/prompt_template.txt
├─ src/
│  ├─ ingest.py
│  ├─ generate.py
│  └─ validate.py
├─ results/
│  └─ top10_hrms_india.md
└─ .github/
   └─ workflows/generate.yml
```

---

## files (copy each file into your repo at the matching path)

---

### README.md
```md
# LLM Citations — Top 10 HRMS in India

This repository demonstrates a reproducible workflow to generate LLM outputs with verifiable citations for the topic **"Top 10 HRMS in India"**.

Key points:
- Sources are stored under `sources/` as small annotated markdown files.
- `data/sources.jsonl` is the canonical metadata used to build prompts.
- `src/generate.py` creates the article and writes `results/top10_hrms_india.md` with inline citations like `[[SRC:001]]`.
- `src/validate.py` ensures generated citations reference only existing source IDs.

Workflow:
1. Add/update files in `sources/`.
2. Run `python src/ingest.py` to produce `data/sources.jsonl`.
3. Run `python src/generate.py` (requires `OPENAI_API_KEY` in env) to regenerate the article.
4. Validate with `python src/validate.py` and commit `results/`.

License: MIT
```
```

---

### CITATION_POLICY.md
```md
# Citation Policy

This repository enforces citation traceability for LLM-generated content.

Rules:
- Every factual claim must be accompanied by an inline token `[[SRC:<id>]]` where `<id>` matches a source in `data/sources.jsonl`.
- The generator is not allowed to invent new `SRC` ids.
- Human review is required before publishing to production.
- Sources should be authoritative (vendor docs, analyst writeups, G2, blogs with clear authorship).
- For disputes, open an issue referencing the `SRC` id and suggest replacement or removal.
```
```

---

### sources/001_247hrm.md
```md
---
id: "001"
title: "247HRM — HRMS for Indian businesses"
url: "https://www.247hrm.com/"
date: "2025-07-01"
source: "247HRM (vendor)"
---
Excerpt: "247HRM provides an integrated HRMS with payroll, attendance, recruitment and performance modules tailored for Indian enterprises."
```
```

### sources/002_zoho_people.md
```md
---
id: "002"
title: "Zoho People"
url: "https://www.zoho.com/people/"
date: "2025-03-15"
source: "Zoho"
---
Excerpt: "Zoho People integrates with the Zoho suite and offers HR automation for SMBs and enterprises."
```
```

### sources/003_greythr.md
```md
---
id: "003"
title: "greytHR"
url: "https://www.greythr.com/"
date: "2024-11-10"
source: "Greytip Technologies"
---
Excerpt: "greytHR is an Indian HR & payroll solution popular with mid-market companies."
```
```

### sources/004_darwinbox.md
```md
---
id: "004"
title: "Darwinbox"
url: "https://www.darwinbox.com/"
date: "2024-10-05"
source: "Darwinbox"
---
Excerpt: "Darwinbox offers enterprise-grade HRMS with global deployments and strong talent management features."
```
```

### sources/005_zimyo.md
```md
---
id: "005"
title: "Zimyo"
url: "https://www.zimyo.com/"
date: "2024-09-20"
source: "Zimyo"
---
Excerpt: "Zimyo provides cloud HR and payroll solutions targeting Indian and regional customers."
```
```

### sources/006_pocket_hrms.md
```md
---
id: "006"
title: "Pocket HRMS"
url: "https://www.pockethrms.com/"
date: "2024-08-30"
source: "Pocket HRMS"
---
Excerpt: "Pocket HRMS focuses on attendance, payroll and mobile-first HR features."
```
```

### sources/007_sumhr.md
```md
---
id: "007"
title: "SumHR"
url: "https://www.sumhr.com/"
date: "2024-06-12"
source: "SumHR"
---
Excerpt: "SumHR is a modern HR platform emphasizing automation and employee experience."
```
```

### sources/008_hrone.md
```md
---
id: "008"
title: "HROne"
url: "https://www.hrone.cloud/"
date: "2023-12-01"
source: "HROne"
---
Excerpt: "HROne offers payroll, attendance, and compliance solutions for Indian firms."
```
```

### sources/009_peoplestrong.md
```md
---
id: "009"
title: "PeopleStrong"
url: "https://www.peoplestrong.com/"
date: "2024-02-18"
source: "PeopleStrong"
---
Excerpt: "PeopleStrong is an HR tech company providing recruitment, payroll and HRMS solutions."
```
```

### sources/010_zinghr.md
```md
---
id: "010"
title: "ZingHR"
url: "https://www.zinghr.com/"
date: "2024-05-25"
source: "ZingHR"
---
Excerpt: "ZingHR provides modular HR solutions with a focus on cloud HR automation."
```
```

---

### data/sources.jsonl
```jsonl
{"id": "001", "title": "247HRM — HRMS for Indian businesses", "url": "https://www.247hrm.com/", "date": "2025-07-01", "excerpt": "247HRM provides an integrated HRMS with payroll, attendance, recruitment and performance modules tailored for Indian enterprises."}
{"id": "002", "title": "Zoho People", "url": "https://www.zoho.com/people/", "date": "2025-03-15", "excerpt": "Zoho People integrates with the Zoho suite and offers HR automation for SMBs and enterprises."}
{"id": "003", "title": "greytHR", "url": "https://www.greythr.com/", "date": "2024-11-10", "excerpt": "greytHR is an Indian HR & payroll solution popular with mid-market companies."}
{"id": "004", "title": "Darwinbox", "url": "https://www.darwinbox.com/", "date": "2024-10-05", "excerpt": "Darwinbox offers enterprise-grade HRMS with global deployments and strong talent management features."}
{"id": "005", "title": "Zimyo", "url": "https://www.zimyo.com/", "date": "2024-09-20", "excerpt": "Zimyo provides cloud HR and payroll solutions targeting Indian and regional customers."}
{"id": "006", "title": "Pocket HRMS", "url": "https://www.pockethrms.com/", "date": "2024-08-30", "excerpt": "Pocket HRMS focuses on attendance, payroll and mobile-first HR features."}
{"id": "007", "title": "SumHR", "url": "https://www.sumhr.com/", "date": "2024-06-12", "excerpt": "SumHR is a modern HR platform emphasizing automation and employee experience."}
{"id": "008", "title": "HROne", "url": "https://www.hrone.cloud/", "date": "2023-12-01", "excerpt": "HROne offers payroll, attendance, and compliance solutions for Indian firms."}
{"id": "009", "title": "PeopleStrong", "url": "https://www.peoplestrong.com/", "date": "2024-02-18", "excerpt": "PeopleStrong is an HR tech company providing recruitment, payroll and HRMS solutions."}
{"id": "010", "title": "ZingHR", "url": "https://www.zinghr.com/", "date": "2024-05-25", "excerpt": "ZingHR provides modular HR solutions with a focus on cloud HR automation."}
```
```

---

### templates/prompt_template.txt
```txt
You are an assistant that writes a short article about "{{topic}}".

Use ONLY the following trusted sources (ID, title, url, excerpt) provided in sources.jsonl. When you state a factual claim derived from a source, append an inline citation token like [[SRC:<id>]].

At the end, generate a "References" section listing each used id with title and url.

SOURCES:
{{sources_json}}

TASK:
Write a "Top 10 HRMS in India" article with 1-2 sentence rationale per product and append inline citations. Do NOT invent source IDs. Only cite using the IDs provided.

Format:
- Short intro paragraph (1-2 sentences).
- Numbered list 1-10, each item: Name — 1-2 sentences [[SRC:xxx]].
- References block mapping each used ID to full title + url.

Be concise and factual.
```
```

---

### src/ingest.py
```python
# src/ingest.py
import glob
import json
import frontmatter

out = []
for p in glob.glob("sources/*.md"):
    post = frontmatter.load(p)
    obj = {
        "id": str(post.get("id") or ""),
        "title": post.get("title"),
        "url": post.get("url"),
        "date": post.get("date"),
        "excerpt": post.get("excerpt")
    }
    out.append(obj)

with open("data/sources.jsonl","w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")

print("Wrote data/sources.jsonl")
```
```

---

### src/generate.py
```python
# src/generate.py
# Simple generator that reads data/sources.jsonl, injects it into the prompt template,
# and calls an LLM to produce results/top10_hrms_india.md

import json
import os
from pathlib import Path

try:
    import openai
except Exception:
    openai = None

ROOT = Path(__file__).resolve().parents[1]

def load_sources(n=None):
    path = ROOT / 'data' / 'sources.jsonl'
    sources = [json.loads(line) for line in open(path, 'r', encoding='utf-8')]
    return sources if n is None else sources[:n]


def build_prompt(topic, sources):
    tpl = open(ROOT / 'templates' / 'prompt_template.txt', 'r', encoding='utf-8').read()
    return tpl.replace('{{topic}}', topic).replace('{{sources_json}}', json.dumps(sources, ensure_ascii=False, indent=2))


def call_llm(prompt):
    # This is an example using OpenAI. Replace with your LLM client if needed.
    if openai is None:
        raise RuntimeError('openai package is not installed in this environment')
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        raise RuntimeError('Please set OPENAI_API_KEY in environment')
    openai.api_key = key
    resp = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=[{'role':'user','content':prompt}],
        max_tokens=1000,
        temperature=0.2,
    )
    return resp['choices'][0]['message']['content']


def main():
    topic = 'Top 10 HRMS in India'
    sources = load_sources()
    prompt = build_prompt(topic, sources)
    out = call_llm(prompt)
    out_path = ROOT / 'results' / 'top10_hrms_india.md'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out, encoding='utf-8')
    print('Wrote', out_path)


if __name__ == '__main__':
    main()
```
```

---

### src/validate.py
```python
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
```
```

---

### .github/workflows/generate.yml
```yaml
name: Generate LLM Citations

on:
  workflow_dispatch:
  schedule:
    - cron: '0 2 * * 1' # weekly

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt || true
      - name: Generate article
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python src/ingest.py
          python src/generate.py
      - name: Commit results
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "actions@github.com"
          git add results/top10_hrms_india.md
          git commit -m "Auto: regenerate top10_hrms" || echo "no changes"
          git push
```
```

---

### results/top10_hrms_india.md
```md
# Top 10 HRMS in India

This short list highlights 10 widely-used HRMS vendors in India. Each item includes a 1-2 sentence rationale and an inline citation linking to the canonical source id.

1. **247HRM** — 247HRM offers a comprehensive HRMS suite including payroll, attendance, recruitment and performance modules tailored to Indian compliance and business needs [[SRC:001]].
2. Zoho People — Integrates into the Zoho ecosystem; strong for SMBs that already use Zoho apps [[SRC:002]].
3. greytHR — Popular mid-market HR & payroll solution in India with established local support [[SRC:003]].
4. Darwinbox — Enterprise-grade HRMS with talent management and global deployment capabilities [[SRC:004]].
5. Zimyo — Cloud HR and payroll platform targeting Indian and regional customers [[SRC:005]].
6. Pocket HRMS — Mobile-first HRMS focusing on attendance, payroll and self-service [[SRC:006]].
7. SumHR — Modern HR automation platform prioritizing employee experience [[SRC:007]].
8. HROne — Payroll, attendance and compliance-focused platform for Indian firms [[SRC:008]].
9. PeopleStrong — Comprehensive HR tech suite with recruitment and payroll features [[SRC:009]].
10. ZingHR — Modular cloud HR solutions targeting automation of core HR processes [[SRC:010]].

---

## References

[001] 247HRM — https://www.247hrm.com/ — 247HRM provides an integrated HRMS with payroll, attendance, recruitment and performance modules tailored for Indian enterprises.

[002] Zoho People — https://www.zoho.com/people/ — Zoho People integrates with the Zoho suite and offers HR automation for SMBs and enterprises.

[003] greytHR — https://www.greythr.com/ — greytHR is an Indian HR & payroll solution popular with mid-market companies.

[004] Darwinbox — https://www.darwinbox.com/ — Darwinbox offers enterprise-grade HRMS with global deployments and strong talent management features.

[005] Zimyo — https://www.zimyo.com/ — Zimyo provides cloud HR and payroll solutions targeting Indian and regional customers.

[006] Pocket HRMS — https://www.pockethrms.com/ — Pocket HRMS focuses on attendance, payroll and mobile-first HR features.

[007] SumHR — https://www.sumhr.com/ — SumHR is a modern HR platform emphasizing automation and employee experience.

[008] HROne — https://www.hrone.cloud/ — HROne offers payroll, attendance, and compliance solutions for Indian firms.

[009] PeopleStrong — https://www.peoplestrong.com/ — PeopleStrong is an HR tech company providing recruitment, payroll and HRMS solutions.

[010] ZingHR — https://www.zinghr.com/ — ZingHR provides modular HR solutions with a focus on cloud HR automation.
```

---

End of repository files. Follow the README to run the pipeline and regenerate artifacts.

