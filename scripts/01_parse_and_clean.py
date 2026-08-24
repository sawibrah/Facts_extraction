import json, re
from pathlib import Path

def clean_text(t: str) -> str:
    if not t:
        return ""
    t = t.replace("\\n", " ").replace("\n", " ")
    t = re.sub(r"\s+", " ", t).strip()
    return t

def read_bulk_json(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    i = 0
    while i < len(lines):
        obj = json.loads(lines[i])
        if "index" in obj:
            i += 1
            if i >= len(lines): break
            art = json.loads(lines[i])
        else:
            art = obj
        row = {
            "id": art.get("identifiantArticle"),
            "url": art.get("urlArticle"),
            "source": art.get("sourceArticle"),
            "title": clean_text(art.get("titreArticle","")),
            "summary": clean_text(art.get("resumeArticle","")),
            "content": clean_text(art.get("contenuArticle","")),
            "keywords": clean_text(art.get("motsClesArticle","")),
            "published_at": art.get("datePublicationArticle"),
            "collected_at": art.get("dateCollecteArticle"),
        }
        if len(row["content"]) > 200:   # minimum text length filter
            rows.append(row)
        i += 1
    return rows

if __name__ == "__main__":
    data = read_bulk_json("results1.json")
    Path("out").mkdir(exist_ok=True)
    with open("out/articles_clean.jsonl", "w", encoding="utf-8") as w:
        for r in data:
            w.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("saved:", len(data))
