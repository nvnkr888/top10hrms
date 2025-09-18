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
