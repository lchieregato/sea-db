# SEA.db — Social Engineering Attack Database

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-2ec4b6.svg)](LICENSE)

An open taxonomy of the human layer of social engineering: the psychological
mechanisms that make an attack work, independent of delivery vector.

SEA.db classifies what standard phishing metrics leave out. A click rate tells
you that something happened. It does not tell you which lever was pulled, what
the target felt, how the attack was built, or where it was anchored. This
taxonomy names those dimensions so that findings can be compared, aggregated,
and cited precisely.

## The four dimensions

| Axis | Code | Count | Question it answers |
|------|------|-------|---------------------|
| Principles | SEA-P | 15 | Which lever the attacker pulls |
| Emotions | SEA-E | 7 | Which state the target feels |
| Techniques | SEA-T | 42 | Which instrument delivers it |
| Contexts | SEA-C | 4 | Where the pretext is anchored |

Techniques are grouped into four vectors: Email (`SEA-TE`), Vishing
(`SEA-TV`), Physical (`SEA-TP`), and Social (`SEA-TS`).

## Citing

Every entity has a stable canonical ID. Cite by ID, for example `SEA-P-007`
(Authority) or `SEA-E-006` (Compassion). IDs are permanent and do not change
across versions.

## Repository layout

```
data/      canonical taxonomy, one YAML file per dimension (edit here)
dist/      consolidated sea-db.json, regenerated automatically
schema/    JSON Schema used to validate every entry
tools/     build and validation script
```

## Using the data

The canonical source is the set of YAML files under `data/`. A consolidated,
machine-readable build is published at `dist/sea-db.json` and regenerated on
every change. To consume the taxonomy in a tool, read `dist/sea-db.json`.

```python
import json, urllib.request
url = "https://raw.githubusercontent.com/lchieregato/sea-db/main/dist/sea-db.json"
db = json.load(urllib.request.urlopen(url))
by_id = {e["id"]: e for grp in ("principles","emotions","techniques","contexts") for e in db[grp]}
print(by_id["SEA-P-007"]["name"])  # Authority
```

## Relationship to MITRE ATT&CK

SEA.db is complementary to MITRE ATT&CK. ATT&CK catalogs adversary behaviors
and techniques. SEA.db describes the psychological layer beneath initial
access. Where a mapping exists, an entity lists the related ATT&CK technique
IDs in its `mitre_attack` field.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New entries and corrections are welcome
by pull request. Benchmark data, scoring formulas, and campaign statistics are
intentionally out of scope for this repository.

## License

This work is licensed under [CC BY 4.0](LICENSE). You may share and adapt the
material for any purpose, including commercially, with appropriate credit.

SEA.db is maintained by OES. Reference site: https://oes.seg.br/seadb
