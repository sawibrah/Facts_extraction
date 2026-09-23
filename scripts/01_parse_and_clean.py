import argparse
import json
import re
from pathlib import Path
from typing import Iterable, Iterator


def clean_text(t: str) -> str:
    if not t:
        return ""
    t = t.replace("\\n", " ").replace("\n", " ")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def iter_records(path: Path) -> Iterator[dict]:
    with path.open("r", encoding="utf-8") as f:
        first_char = f.read(1)
        f.seek(0)
        if first_char == "[":
            data = json.load(f)
            for item in data:
                if isinstance(item, dict):
                    yield item
            return

        lines = [ln.strip() for ln in f if ln.strip()]

    i = 0
    while i < len(lines):
        obj = json.loads(lines[i])
        if isinstance(obj, dict) and "index" in obj:
            i += 1
            if i >= len(lines):
                break
            article = json.loads(lines[i])
            if isinstance(article, dict):
                yield article
        elif isinstance(obj, dict):
            yield obj
        i += 1


def iter_input_files(path: Path, excluded_paths: set[Path] | None = None) -> Iterator[Path]:
    excluded_paths = excluded_paths or set()
    if path.is_file():
        resolved = path.resolve()
        if resolved not in excluded_paths:
            yield path
        return

    if not path.is_dir():
        raise FileNotFoundError(path)

    for candidate in sorted(path.rglob("*")):
        if candidate.suffix.lower() in {".json", ".jsonl", ".ndjson"} and candidate.resolve() not in excluded_paths:
            yield candidate


def normalize_article(article: dict) -> dict:
    return {
        "id": article.get("identifiantArticle") or article.get("id"),
        "url": article.get("urlArticle") or article.get("url"),
        "source": article.get("sourceArticle") or article.get("source"),
        "title": clean_text(article.get("titreArticle") or article.get("title", "")),
        "summary": clean_text(article.get("resumeArticle") or article.get("summary", "")),
        "content": clean_text(article.get("contenuArticle") or article.get("content", "")),
        "keywords": clean_text(article.get("motsClesArticle") or article.get("keywords", "")),
        "published_at": article.get("datePublicationArticle") or article.get("published_at"),
        "collected_at": article.get("dateCollecteArticle") or article.get("collected_at"),
    }



def read_bulk_json(path: str, min_content_length: int = 200, excluded_paths: set[Path] | None = None) -> list[dict]:
    rows = []
    for input_path in iter_input_files(Path(path), excluded_paths=excluded_paths):
        for article in iter_records(input_path):
            row = normalize_article(article)
            if len(row["content"]) >= min_content_length:
                rows.append(row)
    return rows



def write_jsonl(rows: Iterable[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as w:
        for row in rows:
            w.write(json.dumps(row, ensure_ascii=False) + "\n")



def main() -> None:
    parser = argparse.ArgumentParser(description="Clean article exports into JSONL for ONIE tests.")
    parser.add_argument("input", nargs="?", default="results1.json", help="Input JSON/JSONL file or directory")
    parser.add_argument(
        "--output",
        default="out/articles_clean.jsonl",
        help="Output JSONL file",
    )
    parser.add_argument(
        "--min-content-length",
        type=int,
        default=200,
        help="Minimum cleaned content length to keep a document",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    data = read_bulk_json(
        args.input,
        min_content_length=args.min_content_length,
        excluded_paths={output_path.resolve()},
    )
    write_jsonl(data, output_path)
    print("saved:", len(data), "->", output_path)


if __name__ == "__main__":
    main()
