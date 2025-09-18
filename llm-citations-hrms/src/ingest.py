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
