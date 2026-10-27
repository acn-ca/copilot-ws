# ASVS 5.0.0: V11, V12, V13

Load when: Always when ASVS applies
Total: 57 requirements (L1: 7, L2: 29, L3: 21). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the official ASVS 5.0.0 CSV with the leading "Verify that" removed. Cite IDs in reports as v5.0.0-<number> (V1.2.4 -> v5.0.0-1.2.4).
Look up one row: `grep -F "| V11.1.1 |" references/<this file>`

## Contents

- [V11 Cryptography (24 reqs, 3 at L1)](#v11-cryptography-24-reqs-3-at-l1)
- [V12 Secure Communication (12 reqs, 3 at L1)](#v12-secure-communication-12-reqs-3-at-l1)
- [V13 Configuration (21 reqs, 1 at L1)](#v13-configuration-21-reqs-1-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## V11 Cryptography (24 reqs, 3 at L1)

### V11.1 Cryptographic Inventory and Documentation

| ID | L | Requirement |
|---|---|---|
| V11.1.1 | 2 | There is a documented policy for management of cryptographic keys and a cryptographic key lifecycle that follows a key management standard such as NIST SP 800-57. This should include ensuring that keys are not overshared (for example, with more than two entities for shared secrets and more than one entity for private keys). |
| V11.1.2 | 2 | A cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. It must also document where keys can and cannot be used in the system, and the types of data that can and cannot be protected using the keys. |
| V11.1.3 | 3 | Cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations. |
| V11.1.4 | 3 | A cryptographic inventory is maintained. This must include a documented plan that outlines the migration path to new cryptographic standards, such as post-quantum cryptography, in order to react to future threats. |

### V11.2 Secure Cryptography Implementation

| ID | L | Requirement |
|---|---|---|
| V11.2.1 | 2 | Industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations. |
| V11.2.2 | 2 | The application is designed with crypto agility such that random number, authenticated encryption, MAC, or hashing algorithms, key lengths, rounds, ciphers and modes can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. Similarly, it must also be possible to replace keys and passwords and re-encrypt data. This will allow for seamless upgrades to post-quantum cryptography (PQC), once high-assurance implementations of approved PQC schemes or standards are widely available. |
| V11.2.3 | 2 | All cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration. For example, a 256-bit ECC key provides roughly 128 bits of security where RSA requires a 3072-bit key to achieve 128 bits of security. |
| V11.2.4 | 3 | All cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information. |
| V11.2.5 | 3 | All cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks. |

### V11.3 Encryption Algorithms

| ID | L | Requirement |
|---|---|---|
| V11.3.1 | 1 | Insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used. |
| V11.3.2 | 1 | Only approved ciphers and modes such as AES with GCM are used. |
| V11.3.3 | 2 | Encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved MAC algorithm. |
| V11.3.4 | 3 | Nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used. |
| V11.3.5 | 3 | Any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode. |

### V11.4 Hashing and Hash-based Functions

| ID | L | Requirement |
|---|---|---|
| V11.4.1 | 1 | Only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Disallowed hash functions, such as MD5, must not be used for any cryptographic purpose. |
| V11.4.2 | 2 | Passwords are stored using an approved, computationally intensive, key derivation function (also known as a "password hashing function"), with parameter settings configured based on current guidance. The settings should balance security and performance to make brute-force attacks sufficiently challenging for the required level of security. |
| V11.4.3 | 2 | Hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths. If collision resistance is required, the output length must be at least 256 bits. If only resistance to second pre-image attacks is required, the output length must be at least 128 bits. |
| V11.4.4 | 2 | The application uses approved key derivation functions with key stretching parameters when deriving secret keys from passwords. The parameters in use must balance security and performance to prevent brute-force attacks from compromising the resulting cryptographic key. |

### V11.5 Random Values

| ID | L | Requirement |
|---|---|---|
| V11.5.1 | 2 | All random numbers and strings which are intended to be non-guessable must be generated using a cryptographically secure pseudo-random number generator (CSPRNG) and have at least 128 bits of entropy. Note that UUIDs do not respect this condition. |
| V11.5.2 | 3 | The random number generation mechanism in use is designed to work securely, even under heavy demand. |

### V11.6 Public Key Cryptography

| ID | L | Requirement |
|---|---|---|
| V11.6.1 | 2 | Only approved cryptographic algorithms and modes of operation are used for key generation and seeding, and digital signature generation and verification. Key generation algorithms must not generate insecure keys vulnerable to known attacks, for example, RSA keys which are vulnerable to Fermat factorization. |
| V11.6.2 | 3 | Approved cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus on ensuring that key exchange mechanisms use secure parameters. This will prevent attacks on the key establishment process which could lead to adversary-in-the-middle attacks or cryptographic breaks. |

### V11.7 In-Use Data Cryptography

| ID | L | Requirement |
|---|---|---|
| V11.7.1 | 3 | Full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes. |
| V11.7.2 | 3 | Data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible. |

---

## V12 Secure Communication (12 reqs, 3 at L1)

### V12.1 General TLS Security Guidance

| ID | L | Requirement |
|---|---|---|
| V12.1.1 | 1 | Only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol must be the preferred option. |
| V12.1.2 | 2 | Only recommended cipher suites are enabled, with the strongest cipher suites set as preferred. L3 applications must only support cipher suites which provide forward secrecy. |
| V12.1.3 | 2 | The application validates that mTLS client certificates are trusted before using the certificate identity for authentication or authorization. |
| V12.1.4 | 3 | Proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured. |
| V12.1.5 | 3 | Encrypted Client Hello (ECH) is enabled in the application's TLS settings to prevent exposure of sensitive metadata, such as the Server Name Indication (SNI), during TLS handshake processes. |

### V12.2 HTTPS Communication with External Facing Services

| ID | L | Requirement |
|---|---|---|
| V12.2.1 | 1 | TLS is used for all connectivity between a client and external facing, HTTP-based services, and does not fall back to insecure or unencrypted communications. |
| V12.2.2 | 1 | External facing services use publicly trusted TLS certificates. |

### V12.3 General Service to Service Communication Security

| ID | L | Requirement |
|---|---|---|
| V12.3.1 | 2 | An encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs. The server must not fall back to insecure or unencrypted protocols. |
| V12.3.2 | 2 | TLS clients validate certificates received before communicating with a TLS server. |
| V12.3.3 | 2 | TLS or another appropriate transport encryption mechanism used for all connectivity between internal, HTTP-based services within the application, and does not fall back to insecure or unencrypted communications. |
| V12.3.4 | 2 | TLS connections between internal services use trusted certificates. Where internally generated or self-signed certificates are used, the consuming service must be configured to only trust specific internal CAs and specific self-signed certificates. |
| V12.3.5 | 3 | Services communicating internally within a system (intra-service communications) use strong authentication to ensure that each endpoint is verified. Strong authentication methods, such as TLS client authentication, must be employed to ensure identity, using public-key infrastructure and mechanisms that are resistant to replay attacks. For microservice architectures, consider using a service mesh to simplify certificate management and enhance security. |

---

## V13 Configuration (21 reqs, 1 at L1)

### V13.1 Configuration Documentation

| ID | L | Requirement |
|---|---|---|
| V13.1.1 | 2 | All communication needs for the application are documented. This must include external services which the application relies upon and cases where an end user might be able to provide an external location to which the application will then connect. |
| V13.1.2 | 3 | For each service the application uses, the documentation defines the maximum number of concurrent connections (e.g., connection pool limits) and how the application behaves when that limit is reached, including any fallback or recovery mechanisms, to prevent denial of service conditions. |
| V13.1.3 | 3 | The application documentation defines resource‑management strategies for every external system or service it uses (e.g., databases, file handles, threads, HTTP connections). This should include resource‑release procedures, timeout settings, failure handling, and where retry logic is implemented, specifying retry limits, delays, and back‑off algorithms. For synchronous HTTP request–response operations it should mandate short timeouts and either disable retries or strictly limit retries to prevent cascading delays and resource exhaustion. |
| V13.1.4 | 3 | The application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and business requirements. |

### V13.2 Backend Communication Configuration

| ID | L | Requirement |
|---|---|---|
| V13.2.1 | 2 | Communications between backend application components that don't support the application's standard user session mechanism, including APIs, middleware, and data layers, are authenticated. Authentication must use individual service accounts, short-term tokens, or certificate-based authentication and not unchanging credentials such as passwords, API keys, or shared accounts with privileged access. |
| V13.2.2 | 2 | Communications between backend application components, including local or operating system services, APIs, middleware, and data layers, are performed with accounts assigned the least necessary privileges. |
| V13.2.3 | 2 | If a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g., root/root or admin/admin). |
| V13.2.4 | 2 | An allowlist is used to define the external resources or systems with which the application is permitted to communicate (e.g., for outbound requests, data loads, or file access). This allowlist can be implemented at the application layer, web server, firewall, or a combination of different layers. |
| V13.2.5 | 2 | The web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from. |
| V13.2.6 | 3 | Where the application connects to separate services, it follows the documented configuration for each connection, such as maximum parallel connections, behavior when maximum allowed connections is reached, connection timeouts, and retry strategies. |

### V13.3 Secret Management

| ID | L | Requirement |
|---|---|---|
| V13.3.1 | 2 | A secrets management solution, such as a key vault, is used to securely create, store, control access to, and destroy backend secrets. These could include passwords, key material, integrations with databases and third-party systems, keys and seeds for time-based tokens, other internal secrets, and API keys. Secrets must not be included in application source code or included in build artifacts. For an L3 application, this must involve a hardware-backed solution such as an HSM. |
| V13.3.2 | 2 | Access to secret assets adheres to the principle of least privilege. |
| V13.3.3 | 3 | All cryptographic operations are performed using an isolated security module (such as a vault or hardware security module) to securely manage and protect key material from exposure outside of the security module. |
| V13.3.4 | 3 | Secrets are configured to expire and be rotated based on the application's documentation. |

### V13.4 Unintended Information Leakage

| ID | L | Requirement |
|---|---|---|
| V13.4.1 | 1 | The application is deployed either without any source control metadata, including the .git or .svn folders, or in a way that these folders are inaccessible both externally and to the application itself. |
| V13.4.2 | 2 | Debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage. |
| V13.4.3 | 2 | Web servers do not expose directory listings to clients unless explicitly intended. |
| V13.4.4 | 2 | Using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage. |
| V13.4.5 | 2 | Documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended. |
| V13.4.6 | 3 | The application does not expose detailed version information of backend components. |
| V13.4.7 | 3 | The web tier is configured to only serve files with specific file extensions to prevent unintentional information, configuration, and source code leakage. |

---

## Key PASS/FAIL Patterns

### V11.3.1 No ECB Mode or Weak Padding (L1)

FAIL:
```javascript
crypto.createCipheriv('aes-128-ecb', key, null)  // ECB mode
```

PASS:
```javascript
crypto.createCipheriv('aes-256-gcm', key, iv)  // GCM mode (authenticated)
```

### V11.4.1 Approved Hash Functions (L1)

FAIL:
```python
import hashlib
hashlib.md5(password.encode()).hexdigest()  # MD5 for password — FAIL
hashlib.sha1(data).hexdigest()  # SHA1 for security — FAIL
```

PASS:
```python
import bcrypt
bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # proper password hashing
import hashlib
hashlib.sha256(data).hexdigest()  # SHA256 for integrity (not passwords)
```

Note: SHA256 is fine for integrity/checksums but NOT for password storage.
Passwords require bcrypt, argon2, scrypt, or PBKDF2 (see V11.4.2 at L2).

### V12.1.1 TLS 1.2+ (L1)

FAIL:
```javascript
// TLS 1.0/1.1 still enabled
const server = tls.createServer({ minVersion: 'TLSv1' })
```

PASS:
```javascript
const server = tls.createServer({ minVersion: 'TLSv1.2' })
```

### V12.2.1 TLS for All External Connectivity (L1)

FAIL:
```javascript
fetch('http://api.example.com/data')  // HTTP, not HTTPS
```

PASS:
```javascript
fetch('https://api.example.com/data')
```

Red flag: `rejectUnauthorized: false` or `NODE_TLS_REJECT_UNAUTHORIZED=0` disables cert validation.

### V13.4.1 No Source Control Metadata in Production (L1)

FAIL: `.git/`, `.svn/`, `.env` files deployed to production.
Check: deployment scripts, Dockerfiles, .dockerignore for exclusion of these.
