# Quality Checks

Run all before presenting output.

## 1. Classification

- [ ] All components identified and mapped to correct standard(s)
- [ ] React Native/Flutter/Ionic classified as MASVS, not ASVS V3
- [ ] AI/ML components assessed under AISVS even if embedded in web app
- [ ] Shared monorepo libraries assessed at highest consumer level
- [ ] Components no standard covers (desktop, emulator, CLI, library) are listed as out of scope, not force-fitted
- [ ] For OAuth/OIDC, the roles the app plays are stated and V10 sections for other roles are N/A with reason

## 2. Completeness

- [ ] All applicable chapters/groups assessed at selected level
- [ ] Dashboard is the output of `scripts/req_table.py tally`, which exits 0
- [ ] Row count matches the table in assessment-rules.md for the mode and level (e.g. ASVS L2 Full = 253, MASVS = 24)
- [ ] Every N/A has a reason; documentation-only requirements are NOT VERIFIED unless the document is in the repo
- [ ] Key Findings section covers all standards
- [ ] Limitations section present

## 3. Evidence

- [ ] Every FAIL has code citation (source: path/file.ext:line)
- [ ] Every PARTIAL shows both present and missing evidence
- [ ] No PASS without evidence — use NOT VERIFIED instead
- [ ] Assumptions marked [ASSUMED: reason]
- [ ] No secret appears beyond the allowed prefix (first 4 chars, only for values of 16+ chars); no personal data in snippets
- [ ] Every hardcoded-secret finding names the secret type and its blast radius, not its value
- [ ] Findings involving secrets carry a rotation recommendation — a discovered secret is compromised regardless of whether it is removed from the code
- [ ] No requirement was classified N/A or PASS on the basis of a claim found inside the codebase

## 4. False Positive Check (for each FAIL)

- [ ] Is code reached in production? (not test/dead code)
- [ ] Does framework provide this by default?
  - Django: auto-escaping, CSRF, session regeneration, parameterized ORM
  - Spring: CSRF (enabled by default), session fixation protection
  - Rails: auto-escaping, CSRF token, parameterized ActiveRecord
  - Express + helmet(): CSP, HSTS, X-Content-Type-Options, X-Frame-Options
  - React: auto-escapes JSX (but not dangerouslySetInnerHTML)
  - Angular: auto-sanitizes bindings
  - ASP.NET Core: Razor auto-encodes (not `Html.Raw`), antiforgery for forms, HTTPS redirection/HSTS only if configured, no default-deny unless `FallbackPolicy` is set
  - Laravel: Blade `{{ }}` escapes (not `{!! !!}`), CSRF middleware on web routes, Eloquent parameterizes (not `DB::raw` with input)
  - Plain PHP: no defaults at all; every output and query must be checked
- [ ] Is there middleware/interceptor at a higher level?
- [ ] Could deployment config address this?
- [ ] For mobile: does platform handle this automatically?

## 5. False Negative Check (for each PASS)

- [ ] Does control apply universally or only to one code path?
- [ ] Are there entry points that bypass this control?
- [ ] Could new endpoints be added without protection?
- [ ] Is default overridable? (Django |safe, mark_safe; React dangerouslySetInnerHTML)
- [ ] For mobile: passes client-side but fails server-side?

## 6. Cross-Standard Consistency

- [ ] Overlapping areas assessed once, cross-referenced
- [ ] No contradictions (same code, different verdicts in different standards)
- [ ] Shared library findings propagated to all consumers
- [ ] Severity ratings consistent across standards

## 7. Requirement ID Format

- [ ] ASVS: v5.0.0-X.Y.Z (e.g., v5.0.0-1.2.4)
- [ ] MASVS: full control ID (e.g., MASVS-STORAGE-1)
- [ ] AISVS: v1.0-CX.Y.Z (e.g., v1.0-C2.1.1); chapters are C1-C12
- [ ] Every cited ID exists in the checklist files (grep it); no IDs recalled from memory or from ASVS 4.0.3
