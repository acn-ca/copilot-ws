# AISVS 1.0: C8, C9, C10

Load when: Quick Scan when RAG, agents/tool calling, or MCP are present; always in Full Assessment
Total: 68 requirements (L1: 17, L2: 38, L3: 13). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the locked AISVS v1.0 source (1.0/en) with the leading "Verify that" removed. Cite IDs as v1.0-<id> (C2.1.3 -> v1.0-C2.1.3).
Look up one row: `grep -F "| C8.1.1 |" references/<this file>`

## Contents

- [C8 Memory, Embeddings & Vector Database Security (11 reqs, 2 at L1)](#c8-memory-embeddings-vector-database-security-11-reqs-2-at-l1)
- [C9 Orchestration & Agentic Security (34 reqs, 6 at L1)](#c9-orchestration-agentic-security-34-reqs-6-at-l1)
- [C10 Model Context Protocol (MCP) Security (23 reqs, 9 at L1)](#c10-model-context-protocol-mcp-security-23-reqs-9-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## C8 Memory, Embeddings & Vector Database Security (11 reqs, 2 at L1)

### C8.1 Access Controls on Memory & RAG Indices

| ID | L | Requirement |
|---|---|---|
| C8.1.1 | 1 | Vector identifiers and namespaces enforce uniqueness per tenant and prevent cross-tenant collisions. |
| C8.1.2 | 2 | Document metadata tags are immutable after the initial write. |
| C8.1.3 | 2 | Retrieval operations enforce scope constraints. |

### C8.2 Embedding Sanitization & Validation

| ID | L | Requirement |
|---|---|---|
| C8.2.1 | 1 | Sensitive fields are detected before embedding and are masked, tokenized, or dropped. |
| C8.2.2 | 2 | Vectors that fall outside normal clustering patterns are flagged and quarantined before entering production indices. |
| C8.2.3 | 2 | Agent outputs and tool outputs are not automatically written to trusted agent memory without explicit source validation. |
| C8.2.4 | 3 | Content crafted to manipulate retrieval results is detected and rejected or quarantined before vectorization. |
| C8.2.5 | 3 | New content written to memory is checked for contradictions with what is already stored and that conflicts trigger alerts. |

### C8.3 Memory Expiry & Revocation

| ID | L | Requirement |
|---|---|---|
| C8.3.1 | 2 | Expired vectors are excluded from retrieval results. |
| C8.3.2 | 2 | Memory can be reset. |
| C8.3.3 | 3 | Quarantined content is retained but excluded from all retrieval results. |

---

## C9 Orchestration & Agentic Security (34 reqs, 6 at L1)

### C9.1 Execution Budgets, Loop Control, and Circuit Breakers

| ID | L | Requirement |
|---|---|---|
| C9.1.1 | 1 | Per-tool quotas and timeouts (e.g., CPU, memory, disk, egress, and execution time) are enforced. |
| C9.1.2 | 1 | Per-execution budgets (e.g., max recursion depth, token use, and monetary spend) are configured and enforced by the runtime. |
| C9.1.3 | 2 | A swarm-level kill-switch exists that can halt all active agent instances. |

### C9.2 High-Impact Action Approval and Irreversibility Controls

| ID | L | Requirement |
|---|---|---|
| C9.2.1 | 1 | The agent runtime blocks execution of privileged, high-impact, or irreversible actions until explicit human approval is received and verified. |
| C9.2.2 | 2 | Approval requests display canonicalized and complete action parameters, such as diffs, commands, recipients, amounts, resources, and scopes, without truncation or unsafe transformation. |
| C9.2.3 | 2 | Each high-impact action has a trusted reversibility classification, such as read-only, reversible, externally reversible, or irreversible. |
| C9.2.4 | 2 | The agent runtime enforces reversibility classifications by blocking, requiring approval, or restricting actions based on their impact and ability to be reversed. |
| C9.2.5 | 2 | Any self-modification capability (e.g., prompt rewriting, tool-list changes, parameter updates) is restricted by enforceable boundaries. |
| C9.2.6 | 2 | Agentic systems include an AI-augmented review of planned high-risk actions before execution that adds to, and does not replace, the deterministic policy gate. |
| C9.2.7 | 2 | The AI-augmented review mechanism is protected against manipulation by adversarial inputs, and cannot be overridden or bypassed through prompt injection. |
| C9.2.8 | 3 | Approvals are cryptographically bound to action parameters, requester identity, execution context, and a unique single-use nonce. |
| C9.2.9 | 3 | Cryptographic key material or credentials used to issue approvals are isolated from the agent runtime. |
| C9.2.10 | 3 | Approval gates for multi-step or multi-agent action chains enforce the highest-impact reversibility classification present anywhere in the chain. |

### C9.3 Component Isolation and Tool Authorization

| ID | L | Requirement |
|---|---|---|
| C9.3.1 | 1 | Each tool/plugin executes in a least-privilege sandbox or is otherwise isolated from model operations. |
| C9.3.2 | 1 | Tool outputs are validated against schemas. |
| C9.3.3 | 2 | Tool manifests declare required privileges, resource limits, and output validation requirements. |
| C9.3.4 | 2 | The runtime enforces the privileges, resource limits, and output-validation requirements declared in tool manifests. |
| C9.3.5 | 2 | Components processing untrusted data are isolated from tool-calling capabilities, ensuring that compromised data processing cannot trigger unauthorized tool invocations. |
| C9.3.6 | 2 | There is architectural separation between processing of untrusted tool outputs and agent operations. |
| C9.3.7 | 2 | External resources named in model output are verified against an approved allow-list or registry before the agent installs or invokes them. |
| C9.3.8 | 3 | Policy violations trigger automated tool containment. |

### C9.4 Agent and Orchestrator Identity

| ID | L | Requirement |
|---|---|---|
| C9.4.1 | 2 | Each agent instance has a unique cryptographic identity and authenticates as a first-class principal to downstream systems. |
| C9.4.2 | 2 | Agent-initiated actions are cryptographically bound to each step of the execution chain for non-repudiation. |
| C9.4.3 | 3 | Agent identity credentials rotate on a defined schedule. |
| C9.4.4 | 3 | Agent state persisted between invocations is integrity-protected. |

### C9.5 Agent Authorization, Delegation, and Continuous Enforcement

| ID | L | Requirement |
|---|---|---|
| C9.5.1 | 2 | Agent actions are authorized against fine-grained policies enforced by the runtime that restrict which tools an agent may invoke, and which parameter values it may supply. |
| C9.5.2 | 2 | When an agent acts on a user's behalf, the runtime propagates an integrity-protected, scope-limited token that carries the user's authorization context and is enforced at every downstream call. |
| C9.5.3 | 2 | All access control decisions are enforced by application logic or a policy engine, never by the AI model itself. |
| C9.5.4 | 2 | Secrets and credentials required by an agent at runtime are not exposed within the model's observable context, including the context window, system prompts, or tool call parameters. |
| C9.5.5 | 2 | Inter-agent task delegation is restricted by an explicit authorization policy. |
| C9.5.6 | 3 | Long-running agent sessions re-evaluate current backend authorization policy on every privileged action. |

### C9.6 Shutdown and Graceful Degradation

| ID | L | Requirement |
|---|---|---|
| C9.6.1 | 1 | A manual kill-switch mechanism exists to immediately halt AI model inference and outputs. |
| C9.6.2 | 2 | When a human-approval gate is not satisfied within the defined approval time, the system blocks the pending action. |
| C9.6.3 | 3 | Kill-switch commands are implemented through an out-of-band channel that is isolated from the agent runtime. |

---

## C10 Model Context Protocol (MCP) Security (23 reqs, 9 at L1)

### C10.1 Component Integrity

| ID | L | Requirement |
|---|---|---|
| C10.1.1 | 1 | MCP components are obtained only from trusted sources and cryptographically verified. |
| C10.1.2 | 2 | Only allow-listed MCP servers are permitted. |
| C10.1.3 | 2 | Locally launched MCP servers run in a least-privilege sandbox with restricted file system, network, and system access. |

### C10.2 Authentication & Authorization

| ID | L | Requirement |
|---|---|---|
| C10.2.1 | 1 | MCP servers validate access tokens for each request and do not rely on transport security alone. |
| C10.2.2 | 1 | MCP servers validate the presented access token's issuer, audience, expiration, and scope claims in accordance with OAuth 2.1. |
| C10.2.3 | 1 | MCP servers acting as OAuth 2.1 resource servers do not store or persist access tokens or user credentials. |
| C10.2.4 | 2 | MCP tools/list returns only tools permitted by resource owners' authorized scopes. |
| C10.2.5 | 2 | MCP servers enforce access control on every tool invocation, validating that the user's access token authorizes both the requested tool and the specific argument values supplied. |
| C10.2.6 | 2 | MCP servers ensure all session artifacts are removed when a session terminates. |
| C10.2.7 | 2 | MCP servers do not pass through access tokens received from clients to downstream APIs. |

### C10.3 Secure Transport

| ID | L | Requirement |
|---|---|---|
| C10.3.1 | 1 | Authenticated, encrypted streamable HTTP is used for MCP transport for remote services. |
| C10.3.2 | 1 | Stdio transport is permitted only in controlled local environments. |
| C10.3.3 | 2 | MCP servers validate both the Origin header and the Host header independently on all HTTP-based transports to prevent DNS rebinding attacks. |
| C10.3.4 | 2 | MCP clients enforce a minimum acceptable protocol version and reject initialize responses that propose a version below that minimum. |
| C10.3.5 | 3 | Access tokens between the MCP client and server are sender-constrained using mTLS or DPoP. |

### C10.4 Schema, Message, and Input Validation

| ID | L | Requirement |
|---|---|---|
| C10.4.1 | 1 | MCP tools/list and tools/call responses are validated against their declared schemas before being injected into the model context. |
| C10.4.2 | 1 | MCP tools/list and tools/call responses are screened for indirect prompt injection before being injected into the model context. |
| C10.4.3 | 1 | MCP servers reject unrecognized or oversized parameters in function calls. |
| C10.4.4 | 2 | All MCP servers enforce strict schema validation. |
| C10.4.5 | 2 | All MCP transports enforce maximum payload size limits. |
| C10.4.6 | 2 | MCP servers sign tool responses with a unique nonce and timestamp so MCP clients can detect replay attempts. |
| C10.4.7 | 2 | MCP clients present users with explicit consent dialogue and cancellation options upon installation of a local MCP server. |
| C10.4.8 | 3 | MCP clients maintain a snapshot of tool definitions and that any change to a tool definition triggers re-approval before the modified tool can be invoked. |

---

## Key PASS/FAIL Patterns

### C8.1.1 / C8.1.3 Tenant-scoped retrieval

FAIL:
```python
results = vectorstore.similarity_search(user_query, k=5)            # shared namespace, no filter
```

PASS:
```python
results = vectorstore.similarity_search(user_query, k=5, namespace=f"tenant-{tenant_id}", filter={"owner": user.id})
```

### C8.2.1 Sensitive fields handled before embedding

FAIL: raw documents (with emails, national IDs, keys) chunked and embedded unchanged.
PASS: a PII/secret detection step masks or drops fields before `add_documents`.

### C9.1.1 / C9.1.2 Budgets and loop control

FAIL: agent loop with no iteration, token, time, or spend limit.
PASS: `max_iterations`, per-tool timeouts, and a token or cost budget that stops the run.

### C9.2.1 Human approval for high-impact actions

FAIL:
```python
tools = [Tool(name="run_shell", func=lambda c: subprocess.run(c, shell=True)),
         Tool(name="send_payment", func=pay)]
agent.run(user_input)                         # executes whatever the model chooses
```

PASS: destructive or irreversible tools are wrapped so execution blocks until a human approves the exact parameters; read-only tools run freely.

### C9.3.1 / C9.5.3 Tool sandboxing; authorization outside the model

FAIL: the system prompt says "only admins may delete records" and the delete tool itself performs no check.
PASS: the tool checks the caller's permissions in code (policy engine or app logic) and runs with least privilege.

### C10.2.1 / C10.2.5 MCP server auth on every request and tool call

FAIL:
```python
@mcp.tool()
def execute_query(sql: str) -> str:
    return db.execute(sql)        # no token validation, no per-tool authorization, raw SQL
```

PASS:
```python
@mcp.tool()
async def search_documents(query: str, ctx: Context) -> str:
    claims = verify_access_token(ctx)            # issuer, audience, expiry, scope (C10.2.2)
    require_scope(claims, "docs:read")           # per-tool authorization (C10.2.5)
    if len(query) > 500: raise ValueError("too long")   # C10.4.3
    return format(db.search(query, owner=claims.sub))
```

### C10.3.2 Transport

stdio MCP servers are acceptable only for local, controlled use; remote servers need authenticated, encrypted streamable HTTP (C10.3.1).
