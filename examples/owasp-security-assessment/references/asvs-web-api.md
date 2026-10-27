# ASVS 5.0.0: V3, V4, V5

Load when: Full Assessment; Quick Scan when a browser UI or file handling is present
Total: 60 requirements (L1: 14, L2: 24, L3: 22). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the official ASVS 5.0.0 CSV with the leading "Verify that" removed. Cite IDs in reports as v5.0.0-<number> (V1.2.4 -> v5.0.0-1.2.4).
Look up one row: `grep -F "| V3.1.1 |" references/<this file>`

## Contents

- [V3 Web Frontend Security (31 reqs, 8 at L1)](#v3-web-frontend-security-31-reqs-8-at-l1)
- [V4 API and Web Service (16 reqs, 2 at L1)](#v4-api-and-web-service-16-reqs-2-at-l1)
- [V5 File Handling (13 reqs, 4 at L1)](#v5-file-handling-13-reqs-4-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## V3 Web Frontend Security (31 reqs, 8 at L1)

### V3.1 Web Frontend Security Documentation

| ID | L | Requirement |
|---|---|---|
| V3.1.1 | 3 | Application documentation states the expected security features that browsers using the application must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), and other relevant HTTP security mechanisms). It must also define how the application must behave when some of these features are not available (such as warning the user or blocking access). |

### V3.2 Unintended Content Interpretation

| ID | L | Requirement |
|---|---|---|
| V3.2.1 | 1 | Security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API, a user-uploaded file or other resource is requested directly). Possible controls could include: not serving the content unless HTTP request header fields (such as Sec-Fetch-\*) indicate it is the correct context, using the sandbox directive of the Content-Security-Policy header field or using the attachment disposition type in the Content-Disposition header field. |
| V3.2.2 | 1 | Content intended to be displayed as text, rather than rendered as HTML, is handled using safe rendering functions (such as createTextNode or textContent) to prevent unintended execution of content such as HTML or JavaScript. |
| V3.2.3 | 3 | The application avoids DOM clobbering when using client-side JavaScript by employing explicit variable declarations, performing strict type checking, avoiding storing global variables on the document object, and implementing namespace isolation. |

### V3.3 Cookie Setup

| ID | L | Requirement |
|---|---|---|
| V3.3.1 | 1 | Cookies have the 'Secure' attribute set, and if the '\__Host-' prefix is not used for the cookie name, the '__Secure-' prefix must be used for the cookie name. |
| V3.3.2 | 2 | Each cookie's 'SameSite' attribute value is set according to the purpose of the cookie, to limit exposure to user interface redress attacks and browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). |
| V3.3.3 | 2 | Cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be shared with other hosts. |
| V3.3.4 | 2 | If the value of a cookie is not meant to be accessible to client-side scripts (such as a session token), the cookie must have the 'HttpOnly' attribute set and the same value (e. g. session token) must only be transferred to the client via the 'Set-Cookie' header field. |
| V3.3.5 | 3 | When the application writes a cookie, the cookie name and value length combined are not over 4096 bytes. Overly large cookies will not be stored by the browser and therefore not sent with requests, preventing the user from using application functionality which relies on that cookie. |

### V3.4 Browser Security Mechanism Headers

| ID | L | Requirement |
|---|---|---|
| V3.4.1 | 1 | A Strict-Transport-Security header field is included on all responses to enforce an HTTP Strict Transport Security (HSTS) policy. A maximum age of at least 1 year must be defined, and for L2 and up, the policy must apply to all subdomains as well. |
| V3.4.2 | 1 | The Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header field is a fixed value by the application, or if the Origin HTTP request header field value is used, it is validated against an allowlist of trusted origins. When 'Access-Control-Allow-Origin: *' needs to be used, verify that the response does not include any sensitive information. |
| V3.4.3 | 2 | HTTP responses include a Content-Security-Policy response header field which defines directives to ensure the browser only loads and executes trusted content or resources, in order to limit execution of malicious JavaScript. As a minimum, a global policy must be used which includes the directives object-src 'none' and base-uri 'none' and defines either an allowlist or uses nonces or hashes. For an L3 application, a per-response policy with nonces or hashes must be defined. |
| V3.4.4 | 2 | All HTTP responses contain an 'X-Content-Type-Options: nosniff' header field. This instructs browsers not to use content sniffing and MIME type guessing for the given response, and to require the response's Content-Type header field value to match the destination resource. For example, the response to a request for a style is only accepted if the response's Content-Type is 'text/css'. This also enables the use of the Cross-Origin Read Blocking (CORB) functionality by the browser. |
| V3.4.5 | 2 | The application sets a referrer policy to prevent leakage of technically sensitive data to third-party services via the 'Referer' HTTP request header field. This can be done using the Referrer-Policy HTTP response header field or via HTML element attributes. Sensitive data could include path and query data in the URL, and for internal non-public applications also the hostname. |
| V3.4.6 | 2 | The web application uses the frame-ancestors directive of the Content-Security-Policy header field for every HTTP response to ensure that it cannot be embedded by default and that embedding of specific resources is allowed only when necessary. Note that the X-Frame-Options header field, although supported by browsers, is obsolete and may not be relied upon. |
| V3.4.7 | 3 | The Content-Security-Policy header field specifies a location to report violations. |
| V3.4.8 | 3 | All HTTP responses that initiate a document rendering (such as responses with Content-Type text/html), include the Cross‑Origin‑Opener‑Policy header field with the same-origin directive or the same-origin-allow-popups directive as required. This prevents attacks that abuse shared access to Window objects, such as tabnabbing and frame counting. |

### V3.5 Browser Origin Separation

| ID | L | Requirement |
|---|---|---|
| V3.5.1 | 1 | If the application does not rely on the CORS preflight mechanism to prevent disallowed cross-origin requests to use sensitive functionality, these requests are validated to ensure they originate from the application itself. This may be done by using and validating anti-forgery tokens or requiring extra HTTP header fields that are not CORS-safelisted request-header fields. This is to defend against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF). |
| V3.5.2 | 1 | If the application relies on the CORS preflight mechanism to prevent disallowed cross-origin use of sensitive functionality, it is not possible to call the functionality with a request which does not trigger a CORS-preflight request. This may require checking the values of the 'Origin' and 'Content-Type' request header fields or using an extra header field that is not a CORS-safelisted header-field. |
| V3.5.3 | 1 | HTTP requests to sensitive functionality use appropriate HTTP methods such as POST, PUT, PATCH, or DELETE, and not methods defined by the HTTP specification as "safe" such as HEAD, OPTIONS, or GET. Alternatively, strict validation of the Sec-Fetch-* request header fields can be used to ensure that the request did not originate from an inappropriate cross-origin call, a navigation request, or a resource load (such as an image source) where this is not expected. |
| V3.5.4 | 2 | Separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies. |
| V3.5.5 | 2 | Messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid. |
| V3.5.6 | 3 | JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks. |
| V3.5.7 | 3 | Data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks. |
| V3.5.8 | 3 | Authenticated resources (such as images, videos, scripts, and other documents) can be loaded or embedded on behalf of the user only when intended. This can be accomplished by strict validation of the Sec-Fetch-* HTTP request header fields to ensure that the request did not originate from an inappropriate cross-origin call, or by setting a restrictive Cross-Origin-Resource-Policy HTTP response header field to instruct the browser to block returned content. |

### V3.6 External Resource Integrity

| ID | L | Requirement |
|---|---|---|
| V3.6.1 | 3 | Client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresource Integrity (SRI) is used to validate the integrity of the asset. If this is not possible, there should be a documented security decision to justify this for each resource. |

### V3.7 Other Browser Security Considerations

| ID | L | Requirement |
|---|---|---|
| V3.7.1 | 2 | The application only uses client-side technologies which are still supported and considered secure. Examples of technologies which do not meet this requirement include NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets. |
| V3.7.2 | 2 | The application will only automatically redirect the user to a different hostname or domain (which is not controlled by the application) where the destination appears on an allowlist. |
| V3.7.3 | 3 | The application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation. |
| V3.7.4 | 3 | The application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS). This ensures that the use of TLS for the application is built directly into the main browsers, rather than relying only on the Strict-Transport-Security response header field. |
| V3.7.5 | 3 | The application behaves as documented (such as warning the user or blocking access) if the browser used to access the application does not support the expected security features. |

---

## V4 API and Web Service (16 reqs, 2 at L1)

### V4.1 Generic Web Service Security

| ID | L | Requirement |
|---|---|---|
| V4.1.1 | 1 | Every HTTP response with a message body contains a Content-Type header field that matches the actual content of the response, including the charset parameter to specify safe character encoding (e.g., UTF-8, ISO-8859-1) according to IANA Media Types, such as "text/", "/+xml" and "/xml". |
| V4.1.2 | 2 | Only user-facing endpoints (intended for manual web-browser access) automatically redirect from HTTP to HTTPS, while other services or endpoints do not implement transparent redirects. This is to avoid a situation where a client is erroneously sending unencrypted HTTP requests, but since the requests are being automatically redirected to HTTPS, the leakage of sensitive data goes undiscovered. |
| V4.1.3 | 2 | Any HTTP header field used by the application and set by an intermediary layer, such as a load balancer, a web proxy, or a backend-for-frontend service, cannot be overridden by the end-user. Example headers might include X-Real-IP, X-Forwarded-*, or X-User-ID. |
| V4.1.4 | 3 | Only HTTP methods that are explicitly supported by the application or its API (including OPTIONS during preflight requests) can be used and that unused methods are blocked. |
| V4.1.5 | 3 | Per-message digital signatures are used to provide additional assurance on top of transport protections for requests or transactions which are highly sensitive or which traverse a number of systems. |

### V4.2 HTTP Message Structure Validation

| ID | L | Requirement |
|---|---|---|
| V4.2.1 | 2 | All application components (including load balancers, firewalls, and application servers) determine boundaries of incoming HTTP messages using the appropriate mechanism for the HTTP version to prevent HTTP request smuggling. In HTTP/1.x, if a Transfer-Encoding header field is present, the Content-Length header must be ignored per RFC 2616. When using HTTP/2 or HTTP/3, if a Content-Length header field is present, the receiver must ensure that it is consistent with the length of the DATA frames. |
| V4.2.2 | 3 | When generating HTTP messages, the Content-Length header field does not conflict with the length of the content as determined by the framing of the HTTP protocol, in order to prevent request smuggling attacks. |
| V4.2.3 | 3 | The application does not send nor accept HTTP/2 or HTTP/3 messages with connection-specific header fields such as Transfer-Encoding to prevent response splitting and header injection attacks. |
| V4.2.4 | 3 | The application only accepts HTTP/2 and HTTP/3 requests where the header fields and values do not contain any CR (\r), LF (\n), or CRLF (\r\n) sequences, to prevent header injection attacks. |
| V4.2.5 | 3 | If the application (backend or frontend) builds and sends requests, it uses validation, sanitization, or other mechanisms to avoid creating URIs (such as for API calls) or HTTP request header fields (such as Authorization or Cookie), which are too long to be accepted by the receiving component. This could cause a denial of service, such as when sending an overly long request (e.g., a long cookie header field), which results in the server always responding with an error status. |

### V4.3 GraphQL

| ID | L | Requirement |
|---|---|---|
| V4.3.1 | 2 | A query allowlist, depth limiting, amount limiting, or query cost analysis is used to prevent GraphQL or data layer expression Denial of Service (DoS) as a result of expensive, nested queries. |
| V4.3.2 | 2 | GraphQL introspection queries are disabled in the production environment unless the GraphQL API is meant to be used by other parties. |

### V4.4 WebSocket

| ID | L | Requirement |
|---|---|---|
| V4.4.1 | 1 | WebSocket over TLS (WSS) is used for all WebSocket connections. |
| V4.4.2 | 2 | During the initial HTTP WebSocket handshake, the Origin header field is checked against a list of origins allowed for the application. |
| V4.4.3 | 2 | If the application's standard session management cannot be used, dedicated tokens are being used for this, which comply with the relevant Session Management security requirements. |
| V4.4.4 | 2 | Dedicated WebSocket session management tokens are initially obtained or validated through the previously authenticated HTTPS session when transitioning an existing HTTPS session to a WebSocket channel. |

---

## V5 File Handling (13 reqs, 4 at L1)

### V5.1 File Handling Documentation

| ID | L | Requirement |
|---|---|---|
| V5.1.1 | 2 | The documentation defines the permitted file types, expected file extensions, and maximum size (including unpacked size) for each upload feature. Additionally, ensure that the documentation specifies how files are made safe for end-users to download and process, such as how the application behaves when a malicious file is detected. |

### V5.2 File Upload and Content

| ID | L | Requirement |
|---|---|---|
| V5.2.1 | 1 | The application will only accept files of a size which it can process without causing a loss of performance or a denial of service attack. |
| V5.2.2 | 1 | When the application accepts a file, either on its own or within an archive such as a zip file, it checks if the file extension matches an expected file extension and validates that the contents correspond to the type represented by the extension. This includes, but is not limited to, checking the initial 'magic bytes', performing image re-writing, and using specialized libraries for file content validation. For L1, this can focus just on files which are used to make specific business or security decisions. For L2 and up, this must apply to all files being accepted. |
| V5.2.3 | 2 | The application checks compressed files (e.g., zip, gz, docx, odt) against maximum allowed uncompressed size and against maximum number of files before uncompressing the file. |
| V5.2.4 | 3 | A file size quota and maximum number of files per user are enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files. |
| V5.2.5 | 3 | The application does not allow uploading compressed files containing symlinks unless this is specifically required (in which case it will be necessary to enforce an allowlist of the files that can be symlinked to). |
| V5.2.6 | 3 | The application rejects uploaded images with a pixel size larger than the maximum allowed, to prevent pixel flood attacks. |

### V5.3 File Storage

| ID | L | Requirement |
|---|---|---|
| V5.3.1 | 1 | Files uploaded or generated by untrusted input and stored in a public folder, are not executed as server-side program code when accessed directly with an HTTP request. |
| V5.3.2 | 1 | When the application creates file paths for file operations, instead of user-submitted filenames, it uses internally generated or trusted data, or if user-submitted filenames or file metadata must be used, strict validation and sanitization must be applied. This is to protect against path traversal, local or remote file inclusion (LFI, RFI), and server-side request forgery (SSRF) attacks. |
| V5.3.3 | 3 | Server-side file processing, such as file decompression, ignores user-provided path information to prevent vulnerabilities such as zip slip. |

### V5.4 File Download

| ID | L | Requirement |
|---|---|---|
| V5.4.1 | 2 | The application validates or ignores user-submitted filenames, including in a JSON, JSONP, or URL parameter and specifies a filename in the Content-Disposition header field in the response. |
| V5.4.2 | 2 | File names served (e.g., in HTTP response header fields or email attachments) are encoded or sanitized (e.g., following RFC 6266) to preserve document structure and prevent injection attacks. |
| V5.4.3 | 2 | Files obtained from untrusted sources are scanned by antivirus scanners to prevent serving of known malicious content. |

---

## Key PASS/FAIL Patterns

### V3.2.1 Content-Type and MIME Enforcement (L1)

FAIL:
```
# No X-Content-Type-Options header — browser may sniff content
```

PASS:
```javascript
app.use(helmet())  // sets X-Content-Type-Options: nosniff (and others)
// or manually:
res.setHeader('X-Content-Type-Options', 'nosniff')
```

### V3.3.1 Cookie Secure Attribute (L1)

FAIL:
```javascript
res.cookie('session', token)  // no Secure, no HttpOnly
```

PASS:
```javascript
res.cookie('session', token, { secure: true, httpOnly: true, sameSite: 'Lax' })
```

### V3.4.1 HSTS Header (L1)

FAIL: no Strict-Transport-Security header present.

PASS:
```javascript
app.use(helmet.hsts({ maxAge: 31536000, includeSubDomains: true }))
```

### V3.4.2 CORS Configuration (L1)

FAIL:
```javascript
app.use(cors({ origin: '*' }))  // allows any origin on authenticated endpoints
```

PASS:
```javascript
app.use(cors({ origin: ['https://app.example.com'], credentials: true }))
```

### V5.3.1 Uploaded Files Not Directly Executable (L1)

FAIL:
```javascript
// Files stored in public web directory
app.use('/uploads', express.static('uploads'))
const dest = path.join('uploads', req.file.originalname)  // user-controlled name
```

PASS:
```javascript
// Files stored outside web root, served through controller with auth
const dest = path.join('/var/storage', crypto.randomUUID() + ext)
app.get('/files/:id', auth, (req, res) => {
  const file = getFileRecord(req.params.id, req.user.id)  // ownership check
  res.sendFile(file.path)
})
```

### V5.3.2 Path Traversal Prevention (L1)

FAIL:
```javascript
const filepath = path.join('/uploads', req.params.filename)  // ../../../etc/passwd
```

PASS:
```javascript
const filename = path.basename(req.params.filename)  // strip path components
const filepath = path.join('/uploads', filename)
```
