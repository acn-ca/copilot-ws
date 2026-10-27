# ASVS 5.0.0: V6, V7, V8

Load when: Always when ASVS applies
Total: 79 requirements (L1: 23, L2: 37, L3: 19). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the official ASVS 5.0.0 CSV with the leading "Verify that" removed. Cite IDs in reports as v5.0.0-<number> (V1.2.4 -> v5.0.0-1.2.4).
Look up one row: `grep -F "| V6.1.1 |" references/<this file>`

## Contents

- [V6 Authentication (47 reqs, 13 at L1)](#v6-authentication-47-reqs-13-at-l1)
- [V7 Session Management (19 reqs, 6 at L1)](#v7-session-management-19-reqs-6-at-l1)
- [V8 Authorization (13 reqs, 4 at L1)](#v8-authorization-13-reqs-4-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## V6 Authentication (47 reqs, 13 at L1)

### V6.1 Authentication Documentation

| ID | L | Requirement |
|---|---|---|
| V6.1.1 | 1 | Application documentation defines how controls such as rate limiting, anti-automation, and adaptive response, are used to defend against attacks such as credential stuffing and password brute force. The documentation must make clear how these controls are configured and prevent malicious account lockout. |
| V6.1.2 | 2 | A list of context-specific words is documented in order to prevent their use in passwords. The list could include permutations of organization names, product names, system identifiers, project codenames, department or role names, and similar. |
| V6.1.3 | 2 | If the application includes multiple authentication pathways, these are all documented together with the security controls and authentication strength which must be consistently enforced across them. |

### V6.2 Password Security

| ID | L | Requirement |
|---|---|---|
| V6.2.1 | 1 | User set passwords are at least 8 characters in length although a minimum of 15 characters is strongly recommended. |
| V6.2.2 | 1 | Users can change their password. |
| V6.2.3 | 1 | Password change functionality requires the user's current and new password. |
| V6.2.4 | 1 | Passwords submitted during account registration or password change are checked against an available set of, at least, the top 3000 passwords which match the application's password policy, e.g. minimum length. |
| V6.2.5 | 1 | Passwords of any composition can be used, without rules limiting the type of characters permitted. There must be no requirement for a minimum number of upper or lower case characters, numbers, or special characters. |
| V6.2.6 | 1 | Password input fields use type=password to mask the entry. Applications may allow the user to temporarily view the entire masked password, or the last typed character of the password. |
| V6.2.7 | 1 | "paste" functionality, browser password helpers, and external password managers are permitted. |
| V6.2.8 | 1 | The application verifies the user's password exactly as received from the user, without any modifications such as truncation or case transformation. |
| V6.2.9 | 2 | Passwords of at least 64 characters are permitted. |
| V6.2.10 | 2 | A user's password stays valid until it is discovered to be compromised or the user rotates it. The application must not require periodic credential rotation. |
| V6.2.11 | 2 | The documented list of context specific words is used to prevent easy to guess passwords being created. |
| V6.2.12 | 2 | Passwords submitted during account registration or password changes are checked against a set of breached passwords. |

### V6.3 General Authentication Security

| ID | L | Requirement |
|---|---|---|
| V6.3.1 | 1 | Controls to prevent attacks such as credential stuffing and password brute force are implemented according to the application's security documentation. |
| V6.3.2 | 1 | Default user accounts (e.g., "root", "admin", or "sa") are not present in the application or are disabled. |
| V6.3.3 | 2 | Either a multi-factor authentication mechanism or a combination of single-factor authentication mechanisms, must be used in order to access the application. For L3, one of the factors must be a hardware-based authentication mechanism which provides compromise and impersonation resistance against phishing attacks while verifying the intent to authenticate by requiring a user-initiated action (such as a button press on a FIDO hardware key or a mobile phone). Relaxing any of the considerations in this requirement requires a fully documented rationale and a comprehensive set of mitigating controls. |
| V6.3.4 | 2 | If the application includes multiple authentication pathways, there are no undocumented pathways and that security controls and authentication strength are enforced consistently. |
| V6.3.5 | 3 | Users are notified of suspicious authentication attempts (successful or unsuccessful). This may include authentication attempts from an unusual location or client, partially successful authentication (only one of multiple factors), an authentication attempt after a long period of inactivity or a successful authentication after several unsuccessful attempts. |
| V6.3.6 | 3 | Email is not used as either a single-factor or multi-factor authentication mechanism. |
| V6.3.7 | 3 | Users are notified after updates to authentication details, such as credential resets or modification of the username or email address. |
| V6.3.8 | 3 | Valid users cannot be deduced from failed authentication challenges, such as by basing on error messages, HTTP response codes, or different response times. Registration and forgot password functionality must also have this protection. |

### V6.4 Authentication Factor Lifecycle and Recovery

| ID | L | Requirement |
|---|---|---|
| V6.4.1 | 1 | System generated initial passwords or activation codes are securely randomly generated, follow the existing password policy, and expire after a short period of time or after they are initially used. These initial secrets must not be permitted to become the long term password. |
| V6.4.2 | 1 | Password hints or knowledge-based authentication (so-called "secret questions") are not present. |
| V6.4.3 | 2 | A secure process for resetting a forgotten password is implemented, that does not bypass any enabled multi-factor authentication mechanisms. |
| V6.4.4 | 2 | If a multi-factor authentication factor is lost, evidence of identity proofing is performed at the same level as during enrollment. |
| V6.4.5 | 3 | Renewal instructions for authentication mechanisms which expire are sent with enough time to be carried out before the old authentication mechanism expires, configuring automated reminders if necessary. |
| V6.4.6 | 3 | Administrative users can initiate the password reset process for the user, but that this does not allow them to change or choose the user's password. This prevents a situation where they know the user's password. |

### V6.5 General Multi-factor authentication requirements

| ID | L | Requirement |
|---|---|---|
| V6.5.1 | 2 | Lookup secrets, out-of-band authentication requests or codes, and time-based one-time passwords (TOTPs) are only successfully usable once. |
| V6.5.2 | 2 | When being stored in the application's backend, lookup secrets with less than 112 bits of entropy (19 random alphanumeric characters or 34 random digits) are hashed with an approved password storage hashing algorithm that incorporates a 32-bit random salt. A standard hash function can be used if the secret has 112 bits of entropy or more. |
| V6.5.3 | 2 | Lookup secrets, out-of-band authentication code, and time-based one-time password seeds, are generated using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) to avoid predictable values. |
| V6.5.4 | 2 | Lookup secrets and out-of-band authentication codes have a minimum of 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient). |
| V6.5.5 | 2 | Out-of-band authentication requests, codes, or tokens, as well as time-based one-time passwords (TOTPs) have a defined lifetime. Out of band requests must have a maximum lifetime of 10 minutes and for TOTP a maximum lifetime of 30 seconds. |
| V6.5.6 | 3 | Any authentication factor (including physical devices) can be revoked in case of theft or other loss. |
| V6.5.7 | 3 | Biometric authentication mechanisms are only used as secondary factors together with either something you have or something you know. |
| V6.5.8 | 3 | Time-based one-time passwords (TOTPs) are checked based on a time source from a trusted service and not from an untrusted or client provided time. |

### V6.6 Out-of-Band authentication mechanisms

| ID | L | Requirement |
|---|---|---|
| V6.6.1 | 2 | Authentication mechanisms using the Public Switched Telephone Network (PSTN) to deliver One-time Passwords (OTPs) via phone or SMS are offered only when the phone number has previously been validated, alternate stronger methods (such as Time based One-time Passwords) are also offered, and the service provides information on their security risks to users. For L3 applications, phone and SMS must not be available as options. |
| V6.6.2 | 2 | Out-of-band authentication requests, codes, or tokens are bound to the original authentication request for which they were generated and are not usable for a previous or subsequent one. |
| V6.6.3 | 2 | A code based out-of-band authentication mechanism is protected against brute force attacks by using rate limiting. Consider also using a code with at least 64 bits of entropy. |
| V6.6.4 | 3 | Where push notifications are used for multi-factor authentication, rate limiting is used to prevent push bombing attacks. Number matching may also mitigate this risk. |

### V6.7 Cryptographic authentication mechanism

| ID | L | Requirement |
|---|---|---|
| V6.7.1 | 3 | The certificates used to verify cryptographic authentication assertions are stored in a way protects them from modification. |
| V6.7.2 | 3 | The challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device. |

### V6.8 Authentication with an Identity Provider

| ID | L | Requirement |
|---|---|---|
| V6.8.1 | 2 | If the application supports multiple identity providers (IdPs), the user's identity cannot be spoofed via another supported identity provider (eg. by using the same user identifier). The standard mitigation would be for the application to register and identify the user using a combination of the IdP ID (serving as a namespace) and the user's ID in the IdP. |
| V6.8.2 | 2 | The presence and integrity of digital signatures on authentication assertions (for example on JWTs or SAML assertions) are always validated, rejecting any assertions that are unsigned or have invalid signatures. |
| V6.8.3 | 2 | SAML assertions are uniquely processed and used only once within the validity period to prevent replay attacks. |
| V6.8.4 | 2 | If an application uses a separate Identity Provider (IdP) and expects specific authentication strength, methods, or recentness for specific functions, the application verifies this using the information returned by the IdP. For example, if OIDC is used, this might be achieved by validating ID Token claims such as 'acr', 'amr', and 'auth_time' (if present). If the IdP does not provide this information, the application must have a documented fallback approach that assumes that the minimum strength authentication mechanism was used (for example, single-factor authentication using username and password). |

---

## V7 Session Management (19 reqs, 6 at L1)

### V7.1 Session Management Documentation

| ID | L | Requirement |
|---|---|---|
| V7.1.1 | 2 | The user's session inactivity timeout and absolute maximum session lifetime are documented, are appropriate in combination with other controls, and that the documentation includes justification for any deviations from NIST SP 800-63B re-authentication requirements. |
| V7.1.2 | 2 | The documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviors and actions to be taken when the maximum number of active sessions is reached. |
| V7.1.3 | 2 | All systems that create and manage user sessions as part of a federated identity management ecosystem (such as SSO systems) are documented along with controls to coordinate session lifetimes, termination, and any other conditions that require re-authentication. |

### V7.2 Fundamental Session Management Security

| ID | L | Requirement |
|---|---|---|
| V7.2.1 | 1 | The application performs all session token verification using a trusted, backend service. |
| V7.2.2 | 1 | The application uses either self-contained or reference tokens that are dynamically generated for session management, i.e. not using static API secrets and keys. |
| V7.2.3 | 1 | If reference tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG) and possess at least 128 bits of entropy. |
| V7.2.4 | 1 | The application generates a new session token on user authentication, including re-authentication, and terminates the current session token. |

### V7.3 Session Timeout

| ID | L | Requirement |
|---|---|---|
| V7.3.1 | 2 | There is an inactivity timeout such that re-authentication is enforced according to risk analysis and documented security decisions. |
| V7.3.2 | 2 | There is an absolute maximum session lifetime such that re-authentication is enforced according to risk analysis and documented security decisions. |

### V7.4 Session Termination

| ID | L | Requirement |
|---|---|---|
| V7.4.1 | 1 | When session termination is triggered (such as logout or expiration), the application disallows any further use of the session. For reference tokens or stateful sessions, this means invalidating the session data at the application backend. Applications using self-contained tokens will need a solution such as maintaining a list of terminated tokens, disallowing tokens produced before a per-user date and time or rotating a per-user signing key. |
| V7.4.2 | 1 | The application terminates all active sessions when a user account is disabled or deleted (such as an employee leaving the company). |
| V7.4.3 | 2 | The application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update). |
| V7.4.4 | 2 | All pages that require authentication have easy and visible access to logout functionality. |
| V7.4.5 | 2 | Application administrators are able to terminate active sessions for an individual user or for all users. |

### V7.5 Defenses Against Session Abuse

| ID | L | Requirement |
|---|---|---|
| V7.5.1 | 2 | The application requires full re-authentication before allowing modifications to sensitive account attributes which may affect authentication such as email address, phone number, MFA configuration, or other information used in account recovery. |
| V7.5.2 | 2 | Users are able to view and (having authenticated again with at least one factor) terminate any or all currently active sessions. |
| V7.5.3 | 3 | The application requires further authentication with at least one factor or secondary verification before performing highly sensitive transactions or operations. |

### V7.6 Federated Re-authentication

| ID | L | Requirement |
|---|---|---|
| V7.6.1 | 2 | Session lifetime and termination between Relying Parties (RPs) and Identity Providers (IdPs) behave as documented, requiring re-authentication as necessary such as when the maximum time between IdP authentication events is reached. |
| V7.6.2 | 2 | Creation of a session requires either the user's consent or an explicit action, preventing the creation of new application sessions without user interaction. |

---

## V8 Authorization (13 reqs, 4 at L1)

### V8.1 Authorization Documentation

| ID | L | Requirement |
|---|---|---|
| V8.1.1 | 1 | Authorization documentation defines rules for restricting function-level and data-specific access based on consumer permissions and resource attributes. |
| V8.1.2 | 2 | Authorization documentation defines rules for field-level access restrictions (both read and write) based on consumer permissions and resource attributes. Note that these rules might depend on other attribute values of the relevant data object, such as state or status. |
| V8.1.3 | 3 | The application's documentation defines the environmental and contextual attributes (including but not limited to, time of day, user location, IP address, or device) that are used in the application to make security decisions, including those pertaining to authentication and authorization. |
| V8.1.4 | 3 | Authentication and authorization documentation defines how environmental and contextual factors are used in decision-making, in addition to function-level, data-specific, and field-level authorization. This should include the attributes evaluated, thresholds for risk, and actions taken (e.g., allow, challenge, deny, step-up authentication). |

### V8.2 General Authorization Design

| ID | L | Requirement |
|---|---|---|
| V8.2.1 | 1 | The application ensures that function-level access is restricted to consumers with explicit permissions. |
| V8.2.2 | 1 | The application ensures that data-specific access is restricted to consumers with explicit permissions to specific data items to mitigate insecure direct object reference (IDOR) and broken object level authorization (BOLA). |
| V8.2.3 | 2 | The application ensures that field-level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA). |
| V8.2.4 | 3 | Adaptive security controls based on a consumer's environmental and contextual attributes (such as time of day, location, IP address, or device) are implemented for authentication and authorization decisions, as defined in the application's documentation. These controls must be applied when the consumer tries to start a new session and also during an existing session. |

### V8.3 Operation Level Authorization

| ID | L | Requirement |
|---|---|---|
| V8.3.1 | 1 | The application enforces authorization rules at a trusted service layer and doesn't rely on controls that an untrusted consumer could manipulate, such as client-side JavaScript. |
| V8.3.2 | 3 | Changes to values on which authorization decisions are made are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in self-contained tokens), there must be mitigating controls to alert when a consumer performs an action when they are no longer authorized to do so and revert the change. Note that this alternative would not mitigate information leakage. |
| V8.3.3 | 3 | Access to an object is based on the originating subject's (e.g. consumer's) permissions, not on the permissions of any intermediary or service acting on their behalf. For example, if a consumer calls a web service using a self-contained token for authentication, and the service then requests data from a different service, the second service will use the consumer's token, rather than a machine-to-machine token from the first service, to make permission decisions. |

### V8.4 Other Authorization Considerations

| ID | L | Requirement |
|---|---|---|
| V8.4.1 | 2 | Multi-tenant applications use cross-tenant controls to ensure consumer operations will never affect tenants with which they do not have permissions to interact. |
| V8.4.2 | 3 | Access to administrative interfaces incorporates multiple layers of security, including continuous consumer identity verification, device security posture assessment, and contextual risk analysis, ensuring that network location or trusted endpoints are not the sole factors for authorization even though they may reduce the likelihood of unauthorized access. |

---

## Key PASS/FAIL Patterns

### V6.2.1 Password Minimum Length (L1)

FAIL:
```javascript
if (password.length < 4) return "Too short"  // below 8 char minimum
```

PASS:
```javascript
if (password.length < 8) return "Password must be at least 8 characters"
// Better: 15+ recommended
```

### V6.3.1 Brute Force Protection (L1)

FAIL:
```javascript
// Login endpoint with no rate limiting or lockout
app.post('/login', async (req, res) => {
  const user = await User.findByEmail(req.body.email);
  if (user && await bcrypt.compare(req.body.password, user.hash)) { ... }
})
```

PASS:
```javascript
// Rate limiting on auth endpoints
const loginLimiter = rateLimit({ windowMs: 15*60*1000, max: 10 });
app.post('/login', loginLimiter, async (req, res) => { ... })
```

### V6.3.2 No Default Credentials (L1)

FAIL:
```javascript
// Seed file with default admin credentials
await User.create({ email: 'admin@app.com', password: 'admin123', role: 'admin' })
```

### V7.2.4 Session Regeneration After Auth (L1)

FAIL:
```javascript
// Session ID unchanged after login
app.post('/login', (req, res) => {
  req.session.userId = user.id;  // same session ID as before auth
})
```

PASS:
```javascript
app.post('/login', (req, res) => {
  req.session.regenerate(() => {  // new session ID after login
    req.session.userId = user.id;
  })
})
```

Framework defaults:
- Django: PASS — `login()` regenerates session automatically
- Spring Security: PASS — session fixation protection enabled by default
- Express/express-session: FAIL — must call `req.session.regenerate()` manually

### V8.2.1 Function-level Authorization (L1)

FAIL:
```javascript
// Admin endpoint with no authorization check
app.delete('/api/users/:id', async (req, res) => {
  await User.destroy({ where: { id: req.params.id } });
})
```

PASS:
```javascript
app.delete('/api/users/:id', requireRole('admin'), async (req, res) => {
  await User.destroy({ where: { id: req.params.id } });
})
```

ASP.NET Core: check for a default-deny fallback. Without it every controller lacking `[Authorize]` is anonymous.
```csharp
builder.Services.AddAuthorization(o => o.FallbackPolicy = new AuthorizationPolicyBuilder().RequireAuthenticatedUser().Build());  // PASS (deny by default)
```
Then grep `[AllowAnonymous]` and list each use with its justification. Spring equivalent: `anyRequest().authenticated()`.

### V8.2.2 Data-level Authorization / IDOR Prevention (L1)

FAIL:
```javascript
// Any authenticated user can access any order by ID
app.get('/api/orders/:id', auth, async (req, res) => {
  const order = await Order.findByPk(req.params.id);  // no ownership check
  res.json(order);
})
```

PASS:
```javascript
app.get('/api/orders/:id', auth, async (req, res) => {
  const order = await Order.findOne({
    where: { id: req.params.id, userId: req.user.id }  // ownership check
  });
  if (!order) return res.status(404).end();
  res.json(order);
})
```
