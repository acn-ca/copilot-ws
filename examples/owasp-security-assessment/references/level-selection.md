# Level Selection Guide

Levels are cumulative in ASVS and AISVS: an L2 assessment checks every requirement marked 1 or 2.

## ASVS 5.0.0 (345 requirements)

| Level | New at this level | Checked in total | Target |
|---|---|---|---|
| L1 | 70 | 70 | Minimum baseline for any web app or API |
| L2 | 183 | 253 | Apps handling sensitive data, most business apps |
| L3 | 92 | 345 | High-assurance and regulated systems |

| App profile | Level |
|---|---|
| Marketing site, blog, docs, wiki, prototype | L1 |
| SaaS, e-commerce, CRM, apps with PII | L2 |
| Identity and authorization services, banking, healthcare, government, critical infrastructure | L3 (L2 if the user wants a first pass) |

## MASVS 2.1.0 (24 controls)

MASVS has no levels. The MAS project is reworking its official "MAS Profiles" (see mas.owasp.org/Profiles), so this skill uses its own depth tiers. Name them as this skill's tiers in reports, not as official profiles.

| Tier (this skill) | Groups assessed | Target |
|---|---|---|
| Baseline | STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, PRIVACY | All mobile apps |
| Baseline + Resilience | All eight groups, including RESILIENCE | Banking, payments, DRM, apps with anti-tamper requirements |

All 24 controls are always listed; groups outside the tier are N/A ("not in tier"). Quick Scan and Full Assessment differ for MASVS in depth and output, not row count: Full uses the full report template and covers native code and every entry point instead of sampling.

## AISVS 1.0 (191 requirements)

| Level | New at this level | Checked in total | Target |
|---|---|---|---|
| L1 | 51 | 51 | Any AI feature in production |
| L2 | 95 | 146 | AI handling sensitive data or decisions, agents with tool access |
| L3 | 45 | 191 | Autonomous agents, regulated or high-stakes AI |

## Quick Scan scope

Quick Scan always uses the lowest tier: ASVS L1, MASVS Baseline, AISVS L1. The exact chapters and fixed row counts are in assessment-rules.md "Which rows go in the table". The report must say which chapters were not assessed.

## Monorepo: different components may need different levels

Shared libraries inherit the highest consumer level.

```
web-api (PII)              --> ASVS L2
admin-panel (internal)     --> ASVS L1
mobile-app (payments)      --> MASVS Baseline + Resilience
ml-service (internal)      --> AISVS L1
shared/auth                --> ASVS L2 (highest consumer)
```
