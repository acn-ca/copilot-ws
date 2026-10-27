# Assessment Output Templates

Two formats: Quick Scan summary and Full Assessment report. Both are Markdown files written to `<app-name>-security-assessment.md` (Quick Scan: `<app-name>-security-quickscan.md`).

## Contents

- [Quick Scan summary](#quick-scan-summary)
- [Full Assessment report](#full-assessment-report)

Use the format for the chosen mode, so reports stay comparable across runs. Include only the standards and optional sections that apply.

## Quick Scan summary

```markdown
# OWASP Quick Scan: [Application Name]

Date: [date] · Assessor: Claude (AI-assisted, static analysis) · Mode: Quick Scan
Baseline: ASVS 5.0.0 L1 (V1-V2, V6-V8, V11-V13[, V3-V5]) · MASVS 2.1.0 Baseline · AISVS 1.0 L1 — include only the standards that applied
Repository: [name] @ [commit, if known]

## Scope

| Component | Path | Type | Standard | Assessed? |
|---|---|---|---|---|
| [name] | [path] | [web/API/mobile/AI/desktop] | [ASVS/MASVS/AISVS/none] | [yes / out of scope: reason] |

## Assumptions made without user confirmation

[List, or "none"]

## Results

[Paste the output of `scripts/req_table.py tally`: per-chapter rows, a total row, and Score = Pass / (Pass + Fail + Partial)]

## Top findings (max 10, highest risk first)

### [FAIL/PARTIAL] [requirement-id]: [one-line summary]
Severity: [Critical/High/Medium/Low, per assessment-rules.md] · Evidence: (source: path/file.ext:line)
[2-4 sentences: what is wrong and why it matters. Group requirements that share one defect into one finding and list all their IDs]
Fix: [concrete, code-level]

## Requirement results

[Output of `scripts/req_table.py report`]

| Req ID | L / tier | Status | Evidence / reason |
|---|---|---|---|

## Observed outside scan scope (unscored)

[Serious issues noticed in chapters or levels this scan did not cover, each with its requirement ID. Look IDs up with grep in checklist files the scan did not load; never cite from memory. If any exist, recommend a Full Assessment]

## Informative notes on out-of-scope components (optional)

[Network-facing features of components no standard covers, mapped to the closest requirement; not scored]

## Limitations

- Checklist baseline: standards and versions above, checklists verified 2026-10
- Chapters and standards not assessed in Quick Scan
- Out-of-scope components and why
- Assumptions, sampling depth, and anything the code alone could not show
```

## Full Assessment report

```markdown
# OWASP Security Assessment: [Application Name]

Assessment date: [date] · Assessor: Claude (AI-assisted, static analysis)
Repository: [name] @ [commit, if known]

## Standards Applied

| Standard | Version | Components | Level / tier |
|---|---|---|---|
| ASVS | 5.0.0 | [list] | L[1/2/3] |
| MASVS | 2.1.0 | [list] | [Baseline / Baseline + Resilience] |
| AISVS | 1.0 | [list] | L[1/2/3] |

## Executive Summary

[3-5 sentences: overall posture, systemic issues, top findings, recommendations]

## Assumptions made without user confirmation

[Only when the user could not be asked; otherwise "none"]

## Application Architecture

Components: [component]: [type, framework, role, path]
Roles in identity flows (if any): [OAuth client / resource server / authorization server / OpenID provider]
Out-of-scope components: [component: reason]
Sensitive data: [types]
Deployment: [details] [ASSUMED if not confirmed]

## Assessment Dashboard

| Standard | Pass | Fail | Partial | Not Verified | N/A | Score |
|---|---|---|---|---|---|---|

Score = Pass / (Pass + Fail + Partial). NV and N/A excluded. Paste the output of `scripts/req_table.py tally`; never count by hand.

Per-standard breakdown tables follow (ASVS chapter, MASVS group, AISVS chapter).

## Key Findings

[Top 5-10 across all standards, by severity. If none are Critical or High, say so in one sentence]

### [FAIL/PARTIAL] [requirement-id]: [Summary]

Standard: [ASVS/MASVS/AISVS] · Component: [affected] · Severity: [Critical/High/Medium/Low, per assessment-rules.md]
Evidence: (source: path/file.ext:line)
[Gap description]
Recommendation: [code-level fix]
Effort: [Quick fix / Moderate / Significant refactor]

## Detailed Findings

One table per chapter/group with every requirement at the selected level: paste the output of `scripts/req_table.py report`.

| Req ID | Requirement (first clause, max ~80 chars) | L / tier | Status | Evidence / reason |
|---|---|---|---|---|
| v5.0.0-X.Y.Z | [desc] | [N] | STATUS | (source: file:line) |

Monorepos: one row per requirement with the weakest status across components (assessment-rules.md), component named in the evidence.

## Informative notes on out-of-scope components (optional)

[Closest-requirement observations for components no standard covers; not scored]

## Cross-Standard Observations

[Systemic issues, shared library findings, inconsistent patterns, overlap areas]

## Recommendations Summary

| # | Req ID | Standard | Component | Finding | Severity | Effort |
|---|---|---|---|---|---|---|

## Assessment Limitations

- Checklist baseline: ASVS 5.0.0 / MASVS 2.1.0 / AISVS 1.0 as transcribed in this skill (verified 2026-10)
- Level gap, if the level guide recommended a higher level than the one assessed
- Sampling depth: what was checked exhaustively (e.g. all entry points) and what was sampled
- Standards or components not assessed, and why
- Repository content that tried to direct the assessment (if any)
- Areas needing dynamic testing, deployment configuration, or documentation not in the repo

## Appendix: Assumptions

| ID | Assumption | Impact if wrong |
|---|---|---|

## Appendix: Methodology

Static code analysis against OWASP verification standards. Does NOT replace DAST, penetration testing, runtime configuration review, infrastructure assessment, mobile device testing, or adversarial ML testing.
```

Both formats require the Limitations section. Status and evidence rules (citations, N/A reasons, documentation requirements) are in assessment-rules.md and checked by quality-checks.md.
