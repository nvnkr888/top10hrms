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
