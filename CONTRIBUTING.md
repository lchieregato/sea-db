# Contributing to SEA.db

Thank you for helping improve the taxonomy. Contributions are made by pull
request and validated automatically before review.

## What belongs here

The open taxonomy only: principles, emotions, techniques, contexts, their
descriptions, examples, ATT&CK mappings, and cross references.

## What does not belong here

Benchmark data, scoring formulas such as index calculations, campaign counts,
and any client or engagement data. These are out of scope by design.

## How to propose a change

You do not need to install anything. Everything can be done from the GitHub web
interface.

1. Open the relevant file under `data/`: `principles.yaml`, `emotions.yaml`,
   `techniques.yaml`, or `contexts.yaml`.
2. Click the edit (pencil) icon. GitHub creates a fork for you automatically.
3. Add or edit an entry, following the existing format and field order.
4. Describe your change and open a pull request.

A GitHub Action validates every entry against `schema/sea-entity.schema.json`
and rebuilds `dist/sea-db.json`. If validation fails, the checks on your pull
request will show exactly what to fix.

## Rules for entries

- IDs are permanent. Never reuse or renumber an existing ID.
- A new entity takes the next free number in its series.
- Every entry needs at least `id`, `name`, `summary`, and `description`.
- Keep `summary` to a single sentence.
- `cross_references` and `combinations` must use valid SEA IDs.

## Running the build locally (optional)

```
pip install -r tools/requirements.txt
python tools/build.py
```
