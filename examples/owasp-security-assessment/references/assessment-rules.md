# Assessment Rules

Decision rules for statuses, severity, scope edge cases and secrets. Load at the start of Phase 1.

## Contents

- [Which rows go in the table](#which-rows-go-in-the-table)
- [Choosing a status](#choosing-a-status)
- [Severity](#severity)
- [Scope edge cases](#scope-edge-cases)
- [Secrets and keys](#secrets-and-keys)
- [Event-driven services](#event-driven-services)
- [Large codebases](#large-codebases)

## Which rows go in the table

The table always has a fixed size for a given mode and level, so runs are comparable:

| Mode | ASVS rows | MASVS rows | AISVS rows |
|---|---|---|---|
| Quick Scan | L1 of V1-V2, V6-V8, V11-V13 (42), plus L1 of V3-V5 (14) when the app serves a browser UI or handles file upload/download | All 24 (RESILIENCE rows N/A: "not in Baseline tier") | L1 of C2, C5, C7, C12 (+ C8-C10 L1 when RAG/agents/MCP) |
| Full | Every row at the level, all 17 chapters (L1: 70, L2: 253, L3: 345) | All 24 | Every row at the level, all 12 chapters |

Chapters for features the app lacks (V17 without WebRTC, V10 roles it does not play, V5 without files) stay in the table as N/A with the reason. Build the table with `scripts/req_table.py init` and count it with `scripts/req_table.py tally`; keep it in one working file and generate the report table from it.

Monorepos: one row per requirement. Status = the weakest status across in-scope components (FAIL > PARTIAL > NOT VERIFIED > PASS; N/A only if N/A everywhere). Name the component in the evidence. If components were assessed at different levels, use one table per component.

## Choosing a status

| Status | Use when |
|---|---|
| PASS | Code or config in the repo shows the control on every relevant path (framework defaults count, overrides break them) |
| FAIL | Code shows the control is missing or wrong on at least one reachable path, or the app needs a feature the requirement governs and does not have it |
| PARTIAL | The control exists but is incomplete: some paths, some services, or a weaker variant |
| NOT VERIFIED | The control may live where you cannot see it: deployment config, API gateway, external package, out-of-scope native code, absent submodule, documentation not in the repo. Say what would resolve it |
| N/A | The feature the requirement governs legitimately does not exist (no uploads, no WebRTC, not an authorization server) |

Tie-breakers:
- Services with no human users (service-to-service APIs, queue consumers, batch jobs): password, MFA, credential recovery and browser-session rows (most of V6, V7) are N/A with "no human users". Machine-to-machine authentication and authorization (V8, V9, V10 client rows) still apply.
- When a row is both a documentation requirement and about a feature the app lacks, N/A wins (the feature reason makes the documentation moot).
- One defect may fail several rows; mark each row it breaks and report it once as a grouped finding. The repeated rows are intended, not double counting.
- Absence that is itself the defect is FAIL, not N/A: an admin function with no authentication fails V8.2.1 even if the app has no login at all. Fail the most specific row; mark rows that depend on the missing feature N/A with "see V8.2.1".
- Code proves the defect even if infrastructure might compensate: `TrustServerCertificate=true` or `ValidateIssuer = false` is FAIL; mention the possible compensating control as [ASSUMED].
- Controls delegated to an external library or service: NOT VERIFIED (name the package/service), unless the repo's configuration of it is visibly wrong, which is FAIL. Relying on an insecure library default counts as visibly wrong: a JDBC/Postgres URL built in the repo without `sslmode=verify-full` (pgjdbc defaults to `prefer`, which does not validate certificates), MySQL without `sslMode=VERIFY_IDENTITY`, an HTTP client with default trust disabled. If the platform injects those settings through environment variables the repo reads, cite that instead.
- API-only services and V3: rows about rendering in browsers (CSP, SRI, frame embedding) are N/A when responses are only consumed by other services; rows that say "all HTTP responses" still apply.
- Documentation requirements ("application documentation defines..."): NOT VERIFIED unless the document is in the repo or provided; name the document that would resolve it.
- Visible vs invisible: if the requirement could be met entirely by code or config you can see and it is not there, FAIL. If it could be met by a component not in the repo (gateway, ingress, backend, store policy), NOT VERIFIED and name that component.
- Response headers (HSTS, nosniff, CSP, cache headers): FAIL when the repo contains the full serving path (app pipeline plus any ingress/proxy config, e.g. nginx, Helm ingress, Front Door/APIM definitions) and none sets the header. NOT VERIFIED when the edge layer is not in the repo; say "not set by the application".
- Code that is not shipped (projects no Dockerfile, pipeline, or publish profile builds; samples; local dev hosts) is treated like test code: excluded from PASS evidence, reported only if it holds secrets or is reachable in production.
- Absence as evidence: "the app never calls exec/eval" is PASS when you cite the search (pattern and scope) that found no matches across the in-scope source. Rows about a technology the app does not use at all (no crypto of its own, no file handling) are N/A, not PASS.
- A lone correct usage in a feature used once (one login form) is PASS for that feature; do not extrapolate to features you did not inspect.
- Reading token claims without validation (`ReadJwtToken`, `jwt.decode`) is acceptable only if the same token was validated earlier in the pipeline; trace it before deciding V9.1.1.

## Severity

| Severity | Meaning |
|---|---|
| Critical | Remote, unauthenticated compromise of the system or of other users' data: injection to code/command execution, auth bypass on sensitive data, exposed admin functions |
| High | Exploitable by an authenticated or adjacent attacker with significant impact: IDOR across tenants, missing token issuer/audience validation, stored secrets granting production access |
| Medium | Weakens defenses or needs extra conditions: missing headers, verbose errors, weak TLS settings, no rate limiting |
| Low | Hardening and hygiene: documentation gaps, outdated but unexploited dependencies, minor information leaks |

Raise one level when findings chain (unauthenticated tool + raw SQL); lower one level when the code is reachable only from a trusted network and the report shows that evidence. Apply each adjustment once and state its reason.

Mobile: a network attacker (MITM, malicious server) maps to the server-side scale. A malicious app on the same device, or physical access to an unlocked device, starts at Medium; raise to High when it exposes credentials or tokens for remote accounts.

## Scope edge cases

- "OWASP" with no standard named, and requests for the OWASP Top 10: see Mode Selection in SKILL.md.
- Intentionally vulnerable or training apps (DVWA, Juice Shop, CTF repos) are assessed as delivered. Note their purpose in Limitations; do not soften findings.
- Internal admin tools that serve HTTP are web apps in scope. Their exposure model affects severity, not applicability.
- Mobile apps with a shared native core (C/C++ via JNI, Flutter engine plugins, game/emulator cores): code the mobile app executes is part of the mobile component for MASVS controls whose behavior lives there (storage, network, crypto, and CODE-4 parsing of untrusted files or network data). Sample the native paths and record the sampling in Limitations. Native code the mobile app never runs stays out of scope.
- End-of-life judgments for vendored libraries need outside knowledge: mark them [ASSUMED] unless the repo or the user's sources confirm them.
- Emulator, console, or firmware keys embedded to emulate hardware are platform constants, not project secrets. Note them under CRYPTO/V11 as informative; do not demand rotation.
- Missing lock files or submodules: dependency rows (V15.2.1, MASVS-CODE-3) are NOT VERIFIED, stating what is missing. For .NET without lock files, read `Directory.Packages.props` versions and note whether `NuGetAudit` is enabled.
- An explicit level from the user beats the level guide. If the guide recommends a higher level, say so in Limitations ("L3 recommended for identity services; L3-only rows not assessed").
- Full Assessment with no level named and no user to ask: use the level the guide recommends for the profile (not the "first pass" alternative) and record it as an assumption.
- Quick Scan of an app whose profile calls for L2 or L3: Quick Scan stays at L1; note the recommended level in Limitations and recommend a Full Assessment at that level.

## Secrets and keys

- For values of 16 characters or more, show at most the first four followed by "...[REDACTED]". For shorter values show none: "[REDACTED, 8-char password]". If the repo only shows where a secret is stored (no value), report the type and location.
- Name the type and what it grants, the file and line, and recommend rotation.
- Well-known public development values (Azurite/Azure Storage emulator key, documented sample keys, `changeme`) are not secrets to rotate. Report them only if they appear in non-development configuration, as a configuration finding.

## Event-driven services

Queue consumers and workers are ASVS components: they process untrusted input and usually expose an HTTP listener for health and metrics.
- Messages are the input surface: V1/V2 apply to message fields as they would to request parameters.
- Topic/queue ACLs and producer identity are the authorization layer (V8, V4.1.5). Accepting security-relevant events from any topic or producer without checking origin is a V8 finding.
- Broker and database connections are backend TLS (V12.3).
- Delivery guarantees (marking work done before the broker acknowledges) fall under V2.3 business-logic integrity and V16.5 error handling.
- Library-provided HTTP endpoints (health, metrics, shutdown) count as the app's HTTP surface: check whether they are exposed beyond the cluster.

## Platform-owned controls

When a shared platform library or the hosting platform owns a control (the HTTP server, Kafka client setup, token client, mesh TLS), mark the rows NOT VERIFIED once per row naming the library or platform, and add one Limitations entry listing the library, version, and every row it affects. Do not repeat the explanation in each finding. If the repo pins that library, note the version so a reader can check it separately.

## Large codebases

- Enumerate entry points first (routes, controllers, minimal-API maps, MCP tools) with grep, and check authorization on all of them; that list is cheap and catches the worst defects.
- Deeper checks may be sampled. Record the sampling in Limitations: what was checked exhaustively and what was sampled.
- Check for a default-deny fallback (ASP.NET Core `FallbackPolicy`, Spring `anyRequest().authenticated()`, global middleware). Without one, every new endpoint is anonymous unless annotated.
