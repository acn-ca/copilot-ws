# ASVS 5.0.0: V9, V10

Load when: Full Assessment (rows N/A when no tokens, OAuth, or OIDC)
Total: 43 requirements (L1: 9, L2: 27, L3: 7). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the official ASVS 5.0.0 CSV with the leading "Verify that" removed. Cite IDs in reports as v5.0.0-<number> (V1.2.4 -> v5.0.0-1.2.4).
Look up one row: `grep -F "| V9.1.1 |" references/<this file>`

## Contents

- [V9 Self-contained Tokens (7 reqs, 4 at L1)](#v9-self-contained-tokens-7-reqs-4-at-l1)
- [V10 OAuth and OIDC (36 reqs, 5 at L1)](#v10-oauth-and-oidc-36-reqs-5-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## V9 Self-contained Tokens (7 reqs, 4 at L1)

### V9.1 Token source and integrity

| ID | L | Requirement |
|---|---|---|
| V9.1.1 | 1 | Self-contained tokens are validated using their digital signature or MAC to protect against tampering before accepting the token's contents. |
| V9.1.2 | 1 | Only algorithms on an allowlist can be used to create and verify self-contained tokens, for a given context. The allowlist must include the permitted algorithms, ideally only either symmetric or asymmetric algorithms, and must not include the 'None' algorithm. If both symmetric and asymmetric must be supported, additional controls will be needed to prevent key confusion. |
| V9.1.3 | 1 | Key material that is used to validate self-contained tokens is from trusted pre-configured sources for the token issuer, preventing attackers from specifying untrusted sources and keys. For JWTs and other JWS structures, headers such as 'jku', 'x5u', and 'jwk' must be validated against an allowlist of trusted sources. |

### V9.2 Token content

| ID | L | Requirement |
|---|---|---|
| V9.2.1 | 1 | If a validity time span is present in the token data, the token and its content are accepted only if the verification time is within this validity time span. For example, for JWTs, the claims 'nbf' and 'exp' must be verified. |
| V9.2.2 | 2 | The service receiving a token validates the token to be the correct type and is meant for the intended purpose before accepting the token's contents. For example, only access tokens can be accepted for authorization decisions and only ID Tokens can be used for proving user authentication. |
| V9.2.3 | 2 | The service only accepts tokens which are intended for use with that service (audience). For JWTs, this can be achieved by validating the 'aud' claim against an allowlist defined in the service. |
| V9.2.4 | 2 | If a token issuer uses the same private key for issuing tokens to different audiences, the issued tokens contain an audience restriction that uniquely identifies the intended audiences. This will prevent a token from being reused with an unintended audience. If the audience identifier is dynamically provisioned, the token issuer must validate these audiences in order to make sure that they do not result in audience impersonation. |

---

## V10 OAuth and OIDC (36 reqs, 5 at L1)

### V10.1 Generic OAuth and OIDC Security

| ID | L | Requirement |
|---|---|---|
| V10.1.1 | 2 | Tokens are only sent to components that strictly need them. For example, when using a backend-for-frontend pattern for browser-based JavaScript applications, access and refresh tokens shall only be accessible for the backend. |
| V10.1.2 | 2 | The client only accepts values from the authorization server (such as the authorization code or ID Token) if these values result from an authorization flow that was initiated by the same user agent session and transaction. This requires that client-generated secrets, such as the proof key for code exchange (PKCE) 'code_verifier', 'state' or OIDC 'nonce', are not guessable, are specific to the transaction, and are securely bound to both the client and the user agent session in which the transaction was started. |

### V10.2 OAuth Client

| ID | L | Requirement |
|---|---|---|
| V10.2.1 | 2 | If the code flow is used, the OAuth client has protection against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF), which trigger token requests, either by using proof key for code exchange (PKCE) functionality or checking the 'state' parameter that was sent in the authorization request. |
| V10.2.2 | 2 | If the OAuth client can interact with more than one authorization server, it has a defense against mix-up attacks. For example, it could require that the authorization server return the 'iss' parameter value and validate it in the authorization response and the token response. |
| V10.2.3 | 3 | The OAuth client only requests the required scopes (or other authorization parameters) in requests to the authorization server. |

### V10.3 OAuth Resource Server

| ID | L | Requirement |
|---|---|---|
| V10.3.1 | 2 | The resource server only accepts access tokens that are intended for use with that service (audience). The audience may be included in a structured access token (such as the 'aud' claim in JWT), or it can be checked using the token introspection endpoint. |
| V10.3.2 | 2 | The resource server enforces authorization decisions based on claims from the access token that define delegated authorization. If claims such as 'sub', 'scope', and 'authorization_details' are present, they must be part of the decision. |
| V10.3.3 | 2 | If an access control decision requires identifying a unique user from an access token (JWT or related token introspection response), the resource server identifies the user from claims that cannot be reassigned to other users. Typically, it means using a combination of 'iss' and 'sub' claims. |
| V10.3.4 | 2 | If the resource server requires specific authentication strength, methods, or recentness, it verifies that the presented access token satisfies these constraints. For example, if present, using the OIDC 'acr', 'amr' and 'auth_time' claims respectively. |
| V10.3.5 | 3 | The resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP). |

### V10.4 OAuth Authorization Server

| ID | L | Requirement |
|---|---|---|
| V10.4.1 | 1 | The authorization server validates redirect URIs based on a client-specific allowlist of pre-registered URIs using exact string comparison. |
| V10.4.2 | 1 | If the authorization server returns the authorization code in the authorization response, it can be used only once for a token request. For the second valid request with an authorization code that has already been used to issue an access token, the authorization server must reject a token request and revoke any issued tokens related to the authorization code. |
| V10.4.3 | 1 | The authorization code is short-lived. The maximum lifetime can be up to 10 minutes for L1 and L2 applications and up to 1 minute for L3 applications. |
| V10.4.4 | 1 | For a given client, the authorization server only allows the usage of grants that this client needs to use. Note that the grants 'token' (Implicit flow) and 'password' (Resource Owner Password Credentials flow) must no longer be used. |
| V10.4.5 | 1 | The authorization server mitigates refresh token replay attacks for public clients, preferably using sender-constrained refresh tokens, i.e., Demonstrating Proof of Possession (DPoP) or Certificate-Bound Access Tokens using mutual TLS (mTLS). For L1 and L2 applications, refresh token rotation may be used. If refresh token rotation is used, the authorization server must invalidate the refresh token after usage, and revoke all refresh tokens for that authorization if an already used and invalidated refresh token is provided. |
| V10.4.6 | 2 | If the code grant is used, the authorization server mitigates authorization code interception attacks by requiring proof key for code exchange (PKCE). For authorization requests, the authorization server must require a valid 'code_challenge' value and must not accept a 'code_challenge_method' value of 'plain'. For a token request, it must require validation of the 'code_verifier' parameter. |
| V10.4.7 | 2 | If the authorization server supports unauthenticated dynamic client registration, it mitigates the risk of malicious client applications. It must validate client metadata such as any registered URIs, ensure the user's consent, and warn the user before processing an authorization request with an untrusted client application. |
| V10.4.8 | 2 | Refresh tokens have an absolute expiration, including if sliding refresh token expiration is applied. |
| V10.4.9 | 2 | Refresh tokens and reference access tokens can be revoked by an authorized user using the authorization server user interface, to mitigate the risk of malicious clients or stolen tokens. |
| V10.4.10 | 2 | Confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, pushed authorization requests (PAR), and token revocation requests. |
| V10.4.11 | 2 | The authorization server configuration only assigns the required scopes to the OAuth client. |
| V10.4.12 | 3 | For a given client, the authorization server only allows the 'response_mode' value that this client needs to use. For example, by having the authorization server validate this value against the expected values or by using pushed authorization request (PAR) or JWT-secured Authorization Request (JAR). |
| V10.4.13 | 3 | Grant type 'code' is always used together with pushed authorization requests (PAR). |
| V10.4.14 | 3 | The authorization server issues only sender-constrained (Proof-of-Possession) access tokens, either with certificate-bound access tokens using mutual TLS (mTLS) or DPoP-bound access tokens (Demonstration of Proof of Possession). |
| V10.4.15 | 3 | For a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example, by requiring the usage of pushed authorization request (PAR) or JWT-secured Authorization Request (JAR). |
| V10.4.16 | 3 | The client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), such as mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') or private key JWT ('private_key_jwt'). |

### V10.5 OIDC Client

| ID | L | Requirement |
|---|---|---|
| V10.5.1 | 2 | The client (as the relying party) mitigates ID Token replay attacks. For example, by ensuring that the 'nonce' claim in the ID Token matches the 'nonce' value sent in the authentication request to the OpenID Provider (in OAuth2 refereed to as the authorization request sent to the authorization server). |
| V10.5.2 | 2 | The client uniquely identifies the user from ID Token claims, usually the 'sub' claim, which cannot be reassigned to other users (for the scope of an identity provider). |
| V10.5.3 | 2 | The client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata. The client must reject authorization server metadata if the issuer URL in the authorization server metadata does not exactly match the pre-configured issuer URL expected by the client. |
| V10.5.4 | 2 | The client validates that the ID Token is intended to be used for that client (audience) by checking that the 'aud' claim from the token is equal to the 'client_id' value for the client. |
| V10.5.5 | 2 | When using OIDC back-channel logout, the relying party mitigates denial of service through forced logout and cross-JWT confusion in the logout flow. The client must verify that the logout token is correctly typed with a value of 'logout+jwt', contains the 'event' claim with the correct member name, and does not contain a 'nonce' claim. Note that it is also recommended to have a short expiration (e.g., 2 minutes). |

### V10.6 OpenID Provider

| ID | L | Requirement |
|---|---|---|
| V10.6.1 | 2 | The OpenID Provider only allows values 'code', 'ciba', 'id_token', or 'id_token code' for response mode. Note that 'code' is preferred over 'id_token code' (the OIDC Hybrid flow), and 'token' (any Implicit flow) must not be used. |
| V10.6.2 | 2 | The OpenID Provider mitigates denial of service through forced logout. By obtaining explicit confirmation from the end-user or, if present, validating parameters in the logout request (initiated by the relying party), such as the 'id_token_hint'. |

### V10.7 Consent Management

| ID | L | Requirement |
|---|---|---|
| V10.7.1 | 2 | The authorization server ensures that the user consents to each authorization request. If the identity of the client cannot be assured, the authorization server must always explicitly prompt the user for consent. |
| V10.7.2 | 2 | When the authorization server prompts for user consent, it presents sufficient and clear information about what is being consented to. When applicable, this should include the nature of the requested authorizations (typically based on scope, resource server, Rich Authorization Requests (RAR) authorization details), the identity of the authorized application, and the lifetime of these authorizations. |
| V10.7.3 | 2 | The user can review, modify, and revoke consents which the user has granted through the authorization server. |

---

## Key PASS/FAIL Patterns

### V9.1.1 Token Signature Verification (L1)

FAIL:
```javascript
// Decode without verification
const payload = jwt.decode(token)  // does NOT verify signature
```

PASS:
```javascript
const payload = jwt.verify(token, publicKey, { algorithms: ['RS256'] })
```

ASP.NET Core:
```csharp
// FAIL for V9.2.3 / V10.3.1 (audience). Disabled issuer validation also weakens V9.1.3 (trusted issuer keys)
// and V10.3.3 (user identified from iss + sub): assess those rows explicitly

TokenValidationParameters = new() { ValidateIssuer = false, ValidateAudience = false, ValidateIssuerSigningKey = true, ... }
// PASS
TokenValidationParameters = new() { ValidIssuer = cfg.Issuer, ValidAudience = cfg.Audience, ValidateIssuerSigningKey = true,
                                    ValidAlgorithms = new[] { "RS256" }, ValidateLifetime = true }
```
`JwtSecurityTokenHandler.ReadJwtToken()` / `jwt.decode()` parse without validating: acceptable only for a token already validated earlier in the same request pipeline.

### V9.1.2 Algorithm Allowlist (L1)

FAIL:
```javascript
// No algorithm restriction — vulnerable to alg:none attack
jwt.verify(token, secret)
```

PASS:
```javascript
jwt.verify(token, secret, { algorithms: ['HS256'] })  // explicit allowlist
```

### V10.4.1 Redirect URI Validation (L1)

FAIL:
```javascript
// Starts-with check — allows redirect to attacker subdomain
if (redirectUri.startsWith('https://app.example.com')) { ... }
// Matches: https://app.example.com.evil.com
```

PASS:
```javascript
// Exact match against registered URIs
const allowed = ['https://app.example.com/callback'];
if (!allowed.includes(redirectUri)) return res.status(400).send('Invalid redirect');
```

Role scoping (check this before marking V10 requirements N/A or FAIL):
- V10 is split by the role the application plays: V10.2 OAuth client, V10.3 resource server, V10.4 authorization server, V10.5 OIDC client, V10.6 OpenID provider, V10.7 consent management. V10.1 applies to every role.
- Identify which roles the codebase implements (one app can be both client and resource server). Sections for roles it does not play are N/A, with the reason stated.
- An app that delegates login to an external IdP is usually client + resource server only; V10.4/V10.6 then belong to the IdP's assessment.

Framework notes:
- Most OAuth libraries (passport, next-auth, spring-security-oauth2) handle redirect validation
- Check that the library configuration uses exact match, not pattern matching
- PKCE is V10.4.6 (L2, authorization server must require it and reject 'plain'). V10.4.2 (L1) is one-time use of authorization codes; V10.2.1 (L2) is client-side CSRF protection via PKCE or 'state'.
