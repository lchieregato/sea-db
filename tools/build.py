#!/usr/bin/env python3
"""Validate SEA.db YAML sources against the schema and build dist/sea-db.json."""
import json, sys, datetime
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SCHEMA = json.loads((ROOT / "schema" / "sea-entity.schema.json").read_text(encoding="utf-8"))
FILES = [("principles", "principle"), ("emotions", "emotion"),
         ("techniques", "technique"), ("contexts", "context")]

def validator_for(kind):
    sub = {"$schema": SCHEMA["$schema"], "$defs": SCHEMA["$defs"], "$ref": f"#/$defs/{kind}"}
    return Draft202012Validator(sub)

def main():
    out = {"name": "SEA.db", "title": "Social Engineering Attack Database",
           "version": "1.1.0", "license": "CC-BY-4.0",
           "homepage": "https://oes.seg.br/seadb",
           "generated": datetime.date.today().isoformat(), "counts": {}}
    errors = 0
    loaded = {}
    for fname, kind in FILES:
        items = yaml.safe_load((DATA / f"{fname}.yaml").read_text(encoding="utf-8")) or []
        v = validator_for(kind)
        seen = set()
        for it in items:
            for e in v.iter_errors(it):
                errors += 1
                print(f"[{fname}] {it.get('id', '?')}: {e.message}", file=sys.stderr)
            if it.get("id") in seen:
                errors += 1
                print(f"[{fname}] duplicate id {it['id']}", file=sys.stderr)
            seen.add(it.get("id"))
        loaded[fname] = items
        out[fname] = items
        out["counts"][fname] = len(items)

    all_ids = {it["id"] for items in loaded.values() for it in items}
    for fname, items in loaded.items():
        for it in items:
            for ref in it.get("cross_references", []) + it.get("combinations", []):
                if ref not in all_ids:
                    print(f"[warn] {it['id']} references unknown id {ref}", file=sys.stderr)

    if errors:
        print(f"\n{errors} schema validation error(s).", file=sys.stderr)
        sys.exit(1)
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "sea-db.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total = sum(out["counts"].values())
    print(f"OK: {total} entities -> dist/sea-db.json ({out['counts']})")

if __name__ == "__main__":
    main()
