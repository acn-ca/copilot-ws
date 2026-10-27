# ASVS 5.0.0: V14, V15, V16, V17

Load when: Full Assessment (V17 rows N/A without WebRTC)
Total: 63 requirements (L1: 5, L2: 40, L3: 18). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the official ASVS 5.0.0 CSV with the leading "Verify that" removed. Cite IDs in reports as v5.0.0-<number> (V1.2.4 -> v5.0.0-1.2.4).
Look up one row: `grep -F "| V14.1.1 |" references/<this file>`

## Contents

- [V14 Data Protection (13 reqs, 2 at L1)](#v14-data-protection-13-reqs-2-at-l1)
- [V15 Secure Coding and Architecture (21 reqs, 3 at L1)](#v15-secure-coding-and-architecture-21-reqs-3-at-l1)
- [V16 Security Logging and Error Handling (17 reqs, 0 at L1)](#v16-security-logging-and-error-handling-17-reqs-0-at-l1)
- [V17 WebRTC (12 reqs, 0 at L1)](#v17-webrtc-12-reqs-0-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## V14 Data Protection (13 reqs, 2 at L1)

### V14.1 Data Protection Documentation

| ID | L | Requirement |
|---|---|---|
| V14.1.1 | 2 | All sensitive data created and processed by the application has been identified and classified into protection levels. This includes data that is only encoded and therefore easily decoded, such as Base64 strings or the plaintext payload inside a JWT. Protection levels need to take into account any data protection and privacy regulations and standards which the application is required to comply with. |
| V14.1.2 | 2 | All sensitive data protection levels have a documented set of protection requirements. This must include (but not be limited to) requirements related to general encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, database-level encryption, privacy and privacy-enhancing technologies to be used, and other confidentiality requirements. |

### V14.2 General Data Protection

| ID | L | Requirement |
|---|---|---|
| V14.2.1 | 1 | Sensitive data is only sent to the server in the HTTP message body or header fields, and that the URL and query string do not contain sensitive information, such as an API key or session token. |
| V14.2.2 | 2 | The application prevents sensitive data from being cached in server components, such as load balancers and application caches, or ensures that the data is securely purged after use. |
| V14.2.3 | 2 | Defined sensitive data is not sent to untrusted parties (e.g., user trackers) to prevent unwanted collection of data outside of the application's control. |
| V14.2.4 | 2 | Controls around sensitive data related to encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, privacy and privacy-enhancing technologies, are implemented as defined in the documentation for the specific data's protection level. |
| V14.2.5 | 3 | Caching mechanisms are configured to only cache responses which have the expected content type for that resource and do not contain sensitive, dynamic content. The web server should return a 404 or 302 response when a non-existent file is accessed rather than returning a different, valid file. This should prevent Web Cache Deception attacks. |
| V14.2.6 | 3 | The application only returns the minimum required sensitive data for the application's functionality. For example, only returning some of the digits of a credit card number and not the full number. If the complete data is required, it should be masked in the user interface unless the user specifically views it. |
| V14.2.7 | 3 | Sensitive information is subject to data retention classification, ensuring that outdated or unnecessary data is deleted automatically, on a defined schedule, or as the situation requires. |
| V14.2.8 | 3 | Sensitive information is removed from the metadata of user-submitted files unless storage is consented to by the user. |

### V14.3 Client-side Data Protection

| ID | L | Requirement |
|---|---|---|
| V14.3.1 | 1 | Authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated. The 'Clear-Site-Data' HTTP response header field may be able to help with this but the client-side should also be able to clear up if the server connection is not available when the session is terminated. |
| V14.3.2 | 2 | The application sets sufficient anti-caching HTTP response header fields (i.e., Cache-Control: no-store) so that sensitive data is not cached in browsers. |
| V14.3.3 | 2 | Data stored in browser storage (such as localStorage, sessionStorage, IndexedDB, or cookies) does not contain sensitive data, with the exception of session tokens. |

---

## V15 Secure Coding and Architecture (21 reqs, 3 at L1)

### V15.1 Secure Coding and Architecture Documentation

| ID | L | Requirement |
|---|---|---|
| V15.1.1 | 1 | Application documentation defines risk based remediation time frames for 3rd party component versions with vulnerabilities and for updating libraries in general, to minimize the risk from these components. |
| V15.1.2 | 2 | An inventory catalog, such as software bill of materials (SBOM), is maintained of all third-party libraries in use, including verifying that components come from pre-defined, trusted, and continually maintained repositories. |
| V15.1.3 | 2 | The application documentation identifies functionality which is time-consuming or resource-demanding. This must include how to prevent a loss of availability due to overusing this functionality and how to avoid a situation where building a response takes longer than the consumer's timeout. Potential defenses may include asynchronous processing, using queues, and limiting parallel processes per user and per application. |
| V15.1.4 | 3 | Application documentation highlights third-party libraries which are considered to be "risky components". |
| V15.1.5 | 3 | Application documentation highlights parts of the application where "dangerous functionality" is being used. |

### V15.2 Security Architecture and Dependencies

| ID | L | Requirement |
|---|---|---|
| V15.2.1 | 1 | The application only contains components which have not breached the documented update and remediation time frames. |
| V15.2.2 | 2 | The application has implemented defenses against loss of availability due to functionality which is time-consuming or resource-demanding, based on the documented security decisions and strategies for this. |
| V15.2.3 | 2 | The production environment only includes functionality that is required for the application to function, and does not expose extraneous functionality such as test code, sample snippets, and development functionality. |
| V15.2.4 | 3 | Third-party components and all of their transitive dependencies are included from the expected repository, whether internally owned or an external source, and that there is no risk of a dependency confusion attack. |
| V15.2.5 | 3 | The application implements additional protections around parts of the application which are documented as containing "dangerous functionality" or using third-party libraries considered to be "risky components". This could include techniques such as sandboxing, encapsulation, containerization or network level isolation to delay and deter attackers who compromise one part of an application from pivoting elsewhere in the application. |

### V15.3 Defensive Coding

| ID | L | Requirement |
|---|---|---|
| V15.3.1 | 1 | The application only returns the required subset of fields from a data object. For example, it should not return an entire data object, as some individual fields should not be accessible to users. |
| V15.3.2 | 2 | Where the application backend makes calls to external URLs, it is configured to not follow redirects unless it is intended functionality. |
| V15.3.3 | 2 | The application has countermeasures to protect against mass assignment attacks by limiting allowed fields per controller and action, e.g., it is not possible to insert or update a field value when it was not intended to be part of that action. |
| V15.3.4 | 2 | All proxying and middleware components transfer the user's original IP address correctly using trusted data fields that cannot be manipulated by the end user, and the application and web server use this correct value for logging and security decisions such as rate limiting, taking into account that even the original IP address may not be reliable due to dynamic IPs, VPNs, or corporate firewalls. |
| V15.3.5 | 2 | The application explicitly ensures that variables are of the correct type and performs strict equality and comparator operations. This is to avoid type juggling or type confusion vulnerabilities caused by the application code making an assumption about a variable type. |
| V15.3.6 | 2 | JavaScript code is written in a way that prevents prototype pollution, for example, by using Set() or Map() instead of object literals. |
| V15.3.7 | 2 | The application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (query string, body parameters, cookies, or header fields). |

### V15.4 Safe Concurrency

| ID | L | Requirement |
|---|---|---|
| V15.4.1 | 3 | Shared objects in multi-threaded code (such as caches, files, or in-memory objects accessed by multiple threads) are accessed safely by using thread-safe types and synchronization mechanisms like locks or semaphores to avoid race conditions and data corruption. |
| V15.4.2 | 3 | Checks on a resource's state, such as its existence or permissions, and the actions that depend on them are performed as a single atomic operation to prevent time-of-check to time-of-use (TOCTOU) race conditions. For example, checking if a file exists before opening it, or verifying a user’s access before granting it. |
| V15.4.3 | 3 | Locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing the resource to ensure locks cannot be inadvertently or maliciously modified by external classes or code. |
| V15.4.4 | 3 | Resource allocation policies prevent thread starvation by ensuring fair access to resources, such as by leveraging thread pools, allowing lower-priority threads to proceed within a reasonable timeframe. |

---

## V16 Security Logging and Error Handling (17 reqs, 0 at L1)

### V16.1 Security Logging Documentation

| ID | L | Requirement |
|---|---|---|
| V16.1.1 | 2 | An inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it is used, how access to it is controlled, and for how long logs are kept. |

### V16.2 General Logging

| ID | L | Requirement |
|---|---|---|
| V16.2.1 | 2 | Each log entry includes necessary metadata (such as when, where, who, what) that would allow for a detailed investigation of the timeline when an event happens. |
| V16.2.2 | 2 | Time sources for all logging components are synchronized, and that timestamps in security event metadata use UTC or include an explicit time zone offset. UTC is recommended to ensure consistency across distributed systems and to prevent confusion during daylight saving time transitions. |
| V16.2.3 | 2 | The application only stores or broadcasts logs to the files and services that are documented in the log inventory. |
| V16.2.4 | 2 | Logs can be read and correlated by the log processor that is in use, preferably by using a common logging format. |
| V16.2.5 | 2 | When logging sensitive data, the application enforces logging based on the data's protection level. For example, it may not be allowed to log certain data, such as credentials or payment details. Other data, such as session tokens, may only be logged by being hashed or masked, either in full or partially. |

### V16.3 Security Events

| ID | L | Requirement |
|---|---|---|
| V16.3.1 | 2 | All authentication operations are logged, including successful and unsuccessful attempts. Additional metadata, such as the type of authentication or factors used, should also be collected. |
| V16.3.2 | 2 | Failed authorization attempts are logged. For L3, this must include logging all authorization decisions, including logging when sensitive data is accessed (without logging the sensitive data itself). |
| V16.3.3 | 2 | The application logs the security events that are defined in the documentation and also logs attempts to bypass the security controls, such as input validation, business logic, and anti-automation. |
| V16.3.4 | 2 | The application logs unexpected errors and security control failures such as backend TLS failures. |

### V16.4 Log Protection

| ID | L | Requirement |
|---|---|---|
| V16.4.1 | 2 | All logging components appropriately encode data to prevent log injection. |
| V16.4.2 | 2 | Logs are protected from unauthorized access and cannot be modified. |
| V16.4.3 | 2 | Logs are securely transmitted to a logically separate system for analysis, detection, alerting, and escalation. The aim is to ensure that if the application is breached, the logs are not compromised. |

### V16.5 Error Handling

| ID | L | Requirement |
|---|---|---|
| V16.5.1 | 2 | A generic message is returned to the consumer when an unexpected or security-sensitive error occurs, ensuring no exposure of sensitive internal system data such as stack traces, queries, secret keys, and tokens. |
| V16.5.2 | 2 | The application continues to operate securely when external resource access fails, for example, by using patterns such as circuit breakers or graceful degradation. |
| V16.5.3 | 2 | The application fails gracefully and securely, including when an exception occurs, preventing fail-open conditions such as processing a transaction despite errors resulting from validation logic. |
| V16.5.4 | 3 | A "last resort" error handler is defined which will catch all unhandled exceptions. This is both to avoid losing error details that must go to log files and to ensure that an error does not take down the entire application process, leading to a loss of availability. |

---

## V17 WebRTC (12 reqs, 0 at L1)

### V17.1 TURN Server

| ID | L | Requirement |
|---|---|---|
| V17.1.1 | 2 | The Traversal Using Relays around NAT (TURN) service only allows access to IP addresses that are not reserved for special purposes (e.g., internal networks, broadcast, loopback). Note that this applies to both IPv4 and IPv6 addresses. |
| V17.1.2 | 3 | The Traversal Using Relays around NAT (TURN) service is not susceptible to resource exhaustion when legitimate users attempt to open a large number of ports on the TURN server. |

### V17.2 Media

| ID | L | Requirement |
|---|---|---|
| V17.2.1 | 2 | The key for the Datagram Transport Layer Security (DTLS) certificate is managed and protected based on the documented policy for management of cryptographic keys. |
| V17.2.2 | 2 | The media server is configured to use and support approved Datagram Transport Layer Security (DTLS) cipher suites and a secure protection profile for the DTLS Extension for establishing keys for the Secure Real-time Transport Protocol (DTLS-SRTP). |
| V17.2.3 | 2 | Secure Real-time Transport Protocol (SRTP) authentication is checked at the media server to prevent Real-time Transport Protocol (RTP) injection attacks from leading to either a Denial of Service condition or audio or video media insertion into media streams. |
| V17.2.4 | 2 | The media server is able to continue processing incoming media traffic when encountering malformed Secure Real-time Transport Protocol (SRTP) packets. |
| V17.2.5 | 3 | The media server is able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users. |
| V17.2.6 | 3 | The media server is not susceptible to the "ClientHello" Race Condition vulnerability in Datagram Transport Layer Security (DTLS) by checking if the media server is publicly known to be vulnerable or by performing the race condition test. |
| V17.2.7 | 3 | Any audio or video recording mechanisms associated with the media server are able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users. |
| V17.2.8 | 3 | The Datagram Transport Layer Security (DTLS) certificate is checked against the Session Description Protocol (SDP) fingerprint attribute, terminating the media stream if the check fails, to ensure the authenticity of the media stream. |

### V17.3 Signaling

| ID | L | Requirement |
|---|---|---|
| V17.3.1 | 2 | The signaling server is able to continue processing legitimate incoming signaling messages during a flood attack. This should be achieved by implementing rate limiting at the signaling level. |
| V17.3.2 | 2 | The signaling server is able to continue processing legitimate signaling messages when encountering malformed signaling message that could cause a denial of service condition. This could include implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques. |

---

## Key PASS/FAIL Patterns

### V14.2.1 Sensitive Data Not in URLs (L1)

FAIL:
```javascript
// Token in query parameter — logged in server logs, browser history, referrer
res.redirect(`/dashboard?token=${authToken}`)
```

PASS:
```javascript
// Token in header or body only
res.setHeader('Authorization', `Bearer ${authToken}`)
```

### V14.3.1 Clear Authenticated Data After Session End (L1)

FAIL:
```javascript
// No cleanup on logout — data persists in DOM/storage
logout() { this.session.destroy() }
```

PASS:
```javascript
logout() {
  this.session.destroy();
  localStorage.clear();
  sessionStorage.clear();
}
```

### V15.1.1 Third-party Update Timeframes (L1)

Check: `npm audit`, `pip audit`, `safety check`, Snyk, or Dependabot output.
FAIL: known critical/high CVEs in dependencies without documented remediation timeline.

### V15.2.1 Components Within Update Policy (L1)

FAIL: dependencies with known critical vulnerabilities.
PASS: `npm audit` / `pip audit` shows no critical/high findings, or documented exceptions.

### V15.3.1 Minimal Data in Responses (L1)

FAIL:
```javascript
app.get('/api/users/:id', (req, res) => {
  const user = await User.findByPk(req.params.id);
  res.json(user)  // exposes passwordHash, internalId, etc.
})
```

PASS:
```javascript
app.get('/api/users/:id', (req, res) => {
  const user = await User.findByPk(req.params.id, {
    attributes: ['id', 'name', 'email']  // explicit field selection
  });
  res.json(user)
})
```

### V16 Note: All V16 requirements are L2+

V16 (Security Logging) has no L1 requirements. For L2+ assessments, verify:
- Auth success/failure logging (V16.3.1)
- Authorization failure logging (V16.3.2)
- Sensitive data logged only as its protection level allows (V16.2.5)
- Generic error messages to users (V16.5.1)
