# Citation Policy

This repository enforces citation traceability for LLM-generated content.

Rules:
- Every factual claim must be accompanied by an inline token `[[SRC:<id>]]` where `<id>` matches a source in `data/sources.jsonl`.
- The generator is not allowed to invent new `SRC` ids.
- Human review is required before publishing to production.
- Sources should be authoritative (vendor docs, analyst writeups, G2, blogs with clear authorship).
- For disputes, open an issue referencing the `SRC` id and suggest replacement or removal.
