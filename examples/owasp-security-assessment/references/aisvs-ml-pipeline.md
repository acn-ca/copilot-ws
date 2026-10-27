# AISVS 1.0: C1, C3, C4, C6, C11

Load when: Full Assessment (rows N/A when the code does not train, host, package, or download models)
Total: 66 requirements (L1: 17, L2: 29, L3: 20). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the locked AISVS v1.0 source (1.0/en) with the leading "Verify that" removed. Cite IDs as v1.0-<id> (C2.1.3 -> v1.0-C2.1.3).
Look up one row: `grep -F "| C1.1.1 |" references/<this file>`

## Contents

- [C1 Training Data Integrity & Traceability (13 reqs, 2 at L1)](#c1-training-data-integrity-traceability-13-reqs-2-at-l1)
- [C3 Model Lifecycle Management & Change Control (15 reqs, 3 at L1)](#c3-model-lifecycle-management-change-control-15-reqs-3-at-l1)
- [C4 Infrastructure, Configuration & Deployment Security (14 reqs, 3 at L1)](#c4-infrastructure-configuration-deployment-security-14-reqs-3-at-l1)
- [C6 Supply Chain Security for Models (7 reqs, 3 at L1)](#c6-supply-chain-security-for-models-7-reqs-3-at-l1)
- [C11 Adversarial Robustness (17 reqs, 6 at L1)](#c11-adversarial-robustness-17-reqs-6-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## C1 Training Data Integrity & Traceability (13 reqs, 2 at L1)

### C1.1 Training Data Origin & Data Security

| ID | L | Requirement |
|---|---|---|
| C1.1.1 | 1 | Training data includes only features, attributes, and fields required for the model's stated purpose. |
| C1.1.2 | 2 | An up-to-date inventory is kept of every training-data source, including its origin, responsible party, license, collection method, intended use constraints, and processing history. |
| C1.1.3 | 2 | Data integrity is provided when training data is stored and transferred. |
| C1.1.4 | 2 | Integrity monitoring is applied to guard against unauthorized modifications or corruption of training data. |
| C1.1.5 | 3 | Datasets are watermarked so their use can be attributed and any unauthorized use detected. |

### C1.2 Data Labeling and Annotation Security

| ID | L | Requirement |
|---|---|---|
| C1.2.1 | 1 | Labeling platforms enforce access controls that restrict who can create, modify, or approve annotations. |
| C1.2.2 | 2 | Cryptographic integrity is applied to labeling artifacts. |
| C1.2.3 | 2 | Sensitive information in labels is redacted, anonymized, or encrypted before being used in any labeling artifact. |

### C1.3 Training Data Quality and Security Assurance

| ID | L | Requirement |
|---|---|---|
| C1.3.1 | 2 | Training and fine-tuning pipelines implement poisoning detection techniques to identify potential data poisoning or unintentional corruption in training data. |
| C1.3.2 | 2 | Automatically generated labels are subject to confidence thresholds and consistency checks to detect misleading or low-confidence labels. |
| C1.3.3 | 2 | Models used in security-relevant decisions are evaluated for bias patterns. |
| C1.3.4 | 2 | Disallowed content is detected and removed before training. |
| C1.3.5 | 3 | Defenses against clean-label poisoning attacks are implemented. |

---

## C3 Model Lifecycle Management & Change Control (15 reqs, 3 at L1)

### C3.1 Model Authorization & Integrity

| ID | L | Requirement |
|---|---|---|
| C3.1.1 | 1 | A model registry maintains an inventory of all deployed model artifacts and their origin. |
| C3.1.2 | 2 | All model artifacts (weights, configurations, tokenizers, base models, fine-tunes, adapters, and safety/policy models) are cryptographically signed by authorized entities. |
| C3.1.3 | 2 | Model cryptographic signatures are verified at deployment admission and on load. |

### C3.2 Model Validation & Testing

| ID | L | Requirement |
|---|---|---|
| C3.2.1 | 1 | Models undergo automated input validation testing, safety evaluation testing, and output sanitization testing before deployment. |
| C3.2.2 | 2 | Models subjected to post-training quantization are re-evaluated against the same safety and alignment test suite on the compressed artifact before deployment. |
| C3.2.3 | 3 | Provider model, version, or routing changes trigger security re-evaluation before continued use. |

### C3.3 Controlled Deployment & Rollback

| ID | L | Requirement |
|---|---|---|
| C3.3.1 | 2 | Production deployments implement rollout mechanisms with automated rollback triggers. |
| C3.3.2 | 2 | Rollback capabilities restore the complete model state. |
| C3.3.3 | 2 | Model versions running in parallel use isolated runtime state so that AI-specific shared resources are not shared across deployments. |

### C3.4 Secure Development Practices

| ID | L | Requirement |
|---|---|---|
| C3.4.1 | 1 | AI-specific runtime components are not shared across environment boundaries (e.g., development, staging, production). |
| C3.4.2 | 2 | Model training and fine-tuning environments are isolated from production environments. |

### C3.5 Pipeline Fine-Tuning

| ID | L | Requirement |
|---|---|---|
| C3.5.1 | 2 | Models used in RLHF fine-tuning are versioned and integrity-verified before use in a training run. |
| C3.5.2 | 3 | RLHF training stages include automated detection of reward hacking or reward model over-optimization. |
| C3.5.3 | 3 | In multi-stage fine-tuning pipelines, each stage's output is integrity-verified before it is consumed by the next stage. |
| C3.5.4 | 3 | Fine-tuning checkpoints are registered as distinct artifacts. |

---

## C4 Infrastructure, Configuration & Deployment Security (14 reqs, 3 at L1)

### C4.1 AI Workload Sandboxing & Validation

| ID | L | Requirement |
|---|---|---|
| C4.1.1 | 1 | AI models execute in isolated sandboxes. |
| C4.1.2 | 1 | Model artifact loading enforces an explicit allow-list of serialization formats that do not permit arbitrary code execution during deserialization. |
| C4.1.3 | 3 | Workload attestation is performed before model loading to provide proof that the execution environment has not been tampered with. |
| C4.1.4 | 3 | Confidential inference services protect model weights during runtime through isolated execution environments. |

### C4.2 AI Hardware Security

| ID | L | Requirement |
|---|---|---|
| C4.2.1 | 2 | AI accelerator (GPU) firmware is version-pinned, signed, and attested at boot. |
| C4.2.2 | 3 | Execution within a trusted execution environment (TEE) provides hardware-enforced isolation, memory encryption, and integrity protection. |
| C4.2.3 | 3 | AI accelerator (GPU) integrity is validated using hardware-based attestation mechanisms before each workload executes. |
| C4.2.4 | 3 | Accelerator (GPU) memory is isolated between workloads through partitioning mechanisms with memory sanitization between jobs. |
| C4.2.5 | 3 | Accelerator interconnects are restricted to approved topologies and authenticated endpoints. |

### C4.3 Edge & Distributed AI Security

| ID | L | Requirement |
|---|---|---|
| C4.3.1 | 1 | Edge AI devices authenticate to central infrastructure using strong authentication mechanisms. |
| C4.3.2 | 2 | Models deployed to edge or mobile devices are cryptographically signed during packaging, and that the on-device runtime validates these signatures or checksums before loading or inference. |
| C4.3.3 | 3 | Inference runtimes enforce process, memory, and file access isolation. |
| C4.3.4 | 3 | Model weights and sensitive parameters stored locally are encrypted using hardware-backed key stores or secure enclaves. |
| C4.3.5 | 3 | Models packaged within mobile, IoT, or embedded applications are encrypted at rest, and decrypted only inside a trusted runtime or secure enclave, preventing direct extraction from the app package or filesystem. |

---

## C6 Supply Chain Security for Models (7 reqs, 3 at L1)

### C6.1 Model Artifact Integrity

| ID | L | Requirement |
|---|---|---|
| C6.1.1 | 1 | Models are scanned for malicious code before import. |
| C6.1.2 | 1 | Model weights, datasets, and fine-tuning adapters are downloaded only from approved sources. |
| C6.1.3 | 2 | Every third-party model artifact can be integrity-verified. |
| C6.1.4 | 2 | Models pass a behavioral acceptance test suite before being promoted to any non-development environment. |

### C6.2 AI BOM & Supply Chain Monitoring

| ID | L | Requirement |
|---|---|---|
| C6.2.1 | 1 | Every model artifact publishes a version-controlled, machine-readable AI BOM listing datasets, weights, licenses, and data-origin statements. |
| C6.2.2 | 2 | AI BOMs are cryptographically signed before deployment. |
| C6.2.3 | 2 | AI BOM completeness checks fail the build if any component metadata is missing. |

---

## C11 Adversarial Robustness (17 reqs, 6 at L1)

### C11.1 Model Alignment, Safety, and Robustness Testing and Training

| ID | L | Requirement |
|---|---|---|
| C11.1.1 | 1 | The model has undergone alignment and safety training or fine-tuning to prevent the model from generating disallowed content categories. |
| C11.1.2 | 1 | A version-controlled alignment test suite is run on every model update or release. |
| C11.1.3 | 1 | Models are evaluated against known adversarial attack techniques relevant to their modality. |
| C11.1.4 | 2 | Models are hardened against adversarial inputs. |
| C11.1.5 | 3 | An automated evaluator measures harmful-content rate and flags regressions beyond a defined threshold. |

### C11.2 Membership-Inference and Model-Inversion Mitigation

| ID | L | Requirement |
|---|---|---|
| C11.2.1 | 1 | Model-inferred sensitive attributes are not directly returned in outputs. |
| C11.2.2 | 1 | Inference endpoints enforce per-principal and global rate limits sized to the extraction threat model, and not solely as a generic API throttle. |
| C11.2.3 | 2 | Model outputs are calibrated to reduce overconfident predictions. |
| C11.2.4 | 2 | Training on sensitive datasets employs differentially-private optimization. |
| C11.2.5 | 3 | Membership-inference attack simulations demonstrate that attack accuracy does not exceed random guessing on evaluated data. |

### C11.3 Model-Extraction Defense

| ID | L | Requirement |
|---|---|---|
| C11.3.1 | 1 | Query-pattern analysis feeds an extraction-attempt detector. |
| C11.3.2 | 2 | Raw model outputs are not directly exposed beyond the application backend, and that externally visible responses are calibrated to the extraction risk level. |
| C11.3.3 | 3 | Model watermarking or fingerprinting techniques are applied so that unauthorized copies can be identified. |
| C11.3.4 | 3 | Detection of suspected extraction triggers response measures. |

### C11.4 Model Runtime Anomaly Detection

| ID | L | Requirement |
|---|---|---|
| C11.4.1 | 2 | Inputs from external or untrusted sources pass through anomaly detection before model inference. |
| C11.4.2 | 2 | Inputs flagged as anomalous trigger gating actions. |
| C11.4.3 | 3 | The safety violation feedback pipeline includes poisoning detection and human review gates to prevent adversarial manipulation of the improvement mechanism. |

---

## Key PASS/FAIL Patterns

### C4.1.2 Serialization allow-list (also C6.1.1 scanning)

FAIL (formats that can execute code on load):
```python
model = pickle.load(open("model.pkl", "rb"))
model = torch.load("model.pt")          # without weights_only=True
model = joblib.load(path_from_user)
```

PASS:
```python
from safetensors.torch import load_file
weights = load_file("model.safetensors")
model = torch.load("model.pt", weights_only=True)
session = onnxruntime.InferenceSession("model.onnx")
```

### C6.1.2 / C6.1.3 Approved sources and integrity

FAIL: `AutoModel.from_pretrained(name_from_config)` with no allow-list and no pinned revision; `trust_remote_code=True` on an unreviewed repo.
PASS: source on an allow-list, `revision="<commit sha>"`, and hash verification of downloaded files.

### C1.1.3 Training data integrity in transit and at rest

FAIL: `pd.read_csv("http://example.com/data.csv")` feeding a training run.
PASS: HTTPS or authenticated storage, checksum or DVC/MLflow-tracked hash checked before training.

### C3.1.1 Model inventory

FAIL: models referenced by ad-hoc paths in code. PASS: a registry (MLflow, SageMaker, internal table) recording every deployed artifact and its origin.

### C11.2.2 / C11.3.2 Extraction and inference defences

FAIL:
```python
return {"label": label, "probabilities": model.predict_proba(x).tolist()}   # raw scores to any caller, no rate limit
```

PASS: per-principal rate limits on the inference endpoint, and only the decision (or coarse confidence band) leaves the backend.

### C4.1.1 / C4.3.1 Isolation and endpoint exposure

FAIL: inference server (Ollama, vLLM, Triton) bound to 0.0.0.0 with no auth in compose or k8s manifests.
PASS: server only reachable on an internal network behind an authenticated gateway, running in its own container or sandbox.
