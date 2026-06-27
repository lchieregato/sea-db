# Changelog

All notable changes to the SEA.db taxonomy are documented here. The format is
based on Keep a Changelog, and the project follows semantic versioning.

## [1.2.0] - 2026-06-27
### Added
- New attack vector **AI-Mediated** (`SEA-TA`), covering social engineering in which
  an AI system is the channel, the actor, or the trust anchor — as distinct from attacks
  that merely use AI as a tool to generate content delivered through another vector.
- Eight techniques: Summary / Output Injection (SEA-TA-001), RAG / Copilot Poisoning
  (SEA-TA-002), AI Answer / Source Poisoning (SEA-TA-003), Slopsquatting (SEA-TA-004),
  Citation Laundering (SEA-TA-005), Agent Hijacking via Indirect Prompt Injection
  (SEA-TA-006), Confused-Deputy / Tool-Call Abuse (SEA-TA-007), and Memory Poisoning
  (SEA-TA-008).
- MITRE ATLAS technique references (`AML.*`) for the new vector, recorded in the existing
  `mitre_attack` field alongside ATT&CK, covering adversarial-AI behaviour that ATT&CK
  does not map.
### Changed
- Techniques now total 56 across six vectors.
- Schema: `id` pattern and the technique `vector` enum extended to accept `SEA-TA`
  and `AI`.

## [1.1.0] - 2026-06-25
### Added
- New attack vector **Collaboration / Messaging Platforms** (`SEA-TC`), covering
  impersonation and abuse on collaboration platforms such as Microsoft Teams and Slack.
- Six techniques: External Tenant Impersonation (SEA-TC-001), Internal Account
  Lateral Messaging (SEA-TC-002), OAuth Consent / Malicious App Grant (SEA-TC-003),
  Webhook / Connector / Bot Spoofing (SEA-TC-004), Guest Access / Shared-Channel
  Infiltration (SEA-TC-005), and Trusted-Platform Link/File Laundering (SEA-TC-006).
### Changed
- Techniques now total 48 across five vectors.
- Schema: `id` pattern and the technique `vector` enum extended to accept `SEA-TC`
  and `COLLABORATION`.

## [1.0.0] - 2026-06-21
### Added
- Initial public release of the SEA.db taxonomy.
- 15 principles (SEA-P), 7 emotions (SEA-E), 42 techniques (SEA-T) across four
  vectors, and 4 contexts (SEA-C).
- JSON Schema for entity validation and an automated build to `dist/sea-db.json`.
