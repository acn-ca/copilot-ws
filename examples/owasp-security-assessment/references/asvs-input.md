# ASVS 5.0.0: V1, V2

Load when: Always when ASVS applies
Total: 43 requirements (L1: 12, L2: 26, L3: 5). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.
Requirement text is verbatim from the official ASVS 5.0.0 CSV with the leading "Verify that" removed. Cite IDs in reports as v5.0.0-<number> (V1.2.4 -> v5.0.0-1.2.4).
Look up one row: `grep -F "| V1.1.1 |" references/<this file>`

## Contents

- [V1 Encoding and Sanitization (30 reqs, 8 at L1)](#v1-encoding-and-sanitization-30-reqs-8-at-l1)
- [V2 Validation and Business Logic (13 reqs, 4 at L1)](#v2-validation-and-business-logic-13-reqs-4-at-l1)
- [Key PASS/FAIL Patterns](#key-passfail-patterns)

---

## V1 Encoding and Sanitization (30 reqs, 8 at L1)

### V1.1 Encoding and Sanitization Architecture

| ID | L | Requirement |
|---|---|---|
| V1.1.1 | 2 | Input is decoded or unescaped into a canonical form only once, it is only decoded when encoded data in that form is expected, and that this is done before processing the input further, for example it is not performed after input validation or sanitization. |
| V1.1.2 | 2 | The application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself. |

### V1.2 Injection Prevention

| ID | L | Requirement |
|---|---|---|
| V1.2.1 | 1 | Output encoding for an HTTP response, HTML document, or XML document is relevant for the context required, such as encoding the relevant characters for HTML elements, HTML attributes, HTML comments, CSS, or HTTP header fields, to avoid changing the message or document structure. |
| V1.2.2 | 1 | When dynamically building URLs, untrusted data is encoded according to its context (e.g., URL encoding or base64url encoding for query or path parameters). Ensure that only safe URL protocols are permitted (e.g., disallow javascript: or data:). |
| V1.2.3 | 1 | Output encoding or escaping is used when dynamically building JavaScript content (including JSON), to avoid changing the message or document structure (to avoid JavaScript and JSON injection). |
| V1.2.4 | 1 | Data selection or database queries (e.g., SQL, HQL, NoSQL, Cypher) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from SQL Injection and other database injection attacks. This is also relevant when writing stored procedures. |
| V1.2.5 | 1 | The application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding. |
| V1.2.6 | 2 | The application protects against LDAP injection vulnerabilities, or that specific security controls to prevent LDAP injection have been implemented. |
| V1.2.7 | 2 | The application is protected against XPath injection attacks by using query parameterization or precompiled queries. |
| V1.2.8 | 2 | LaTeX processors are configured securely (such as not using the "--shell-escape" flag) and an allowlist of commands is used to prevent LaTeX injection attacks. |
| V1.2.9 | 2 | The application escapes special characters in regular expressions (typically using a backslash) to prevent them from being misinterpreted as metacharacters. |
| V1.2.10 | 3 | The application is protected against CSV and Formula Injection. The application must follow the escaping rules defined in RFC 4180 sections 2.6 and 2.7 when exporting CSV content. Additionally, when exporting to CSV or other spreadsheet formats (such as XLS, XLSX, or ODF), special characters (including '=', '+', '-', '@', '\t' (tab), and '\0' (null character)) must be escaped with a single quote if they appear as the first character in a field value. |

### V1.3 Sanitization

| ID | L | Requirement |
|---|---|---|
| V1.3.1 | 1 | All untrusted HTML input from WYSIWYG editors or similar is sanitized using a well-known and secure HTML sanitization library or framework feature. |
| V1.3.2 | 1 | The application avoids the use of eval() or other dynamic code execution features such as Spring Expression Language (SpEL). Where there is no alternative, any user input being included must be sanitized before being executed. |
| V1.3.3 | 2 | Data being passed to a potentially dangerous context is sanitized beforehand to enforce safety measures, such as only allowing characters which are safe for this context and trimming input which is too long. |
| V1.3.4 | 2 | User-supplied Scalable Vector Graphics (SVG) scriptable content is validated or sanitized to contain only tags and attributes (such as draw graphics) that are safe for the application, e.g., do not contain scripts and foreignObject. |
| V1.3.5 | 2 | The application sanitizes or disables user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar. |
| V1.3.6 | 2 | The application protects against Server-side Request Forgery (SSRF) attacks, by validating untrusted data against an allowlist of protocols, domains, paths and ports and sanitizing potentially dangerous characters before using the data to call another service. |
| V1.3.7 | 2 | The application protects against template injection attacks by not allowing templates to be built based on untrusted input. Where there is no alternative, any untrusted input being included dynamically during template creation must be sanitized or strictly validated. |
| V1.3.8 | 2 | The application appropriately sanitizes untrusted input before use in Java Naming and Directory Interface (JNDI) queries and that JNDI is configured securely to prevent JNDI injection attacks. |
| V1.3.9 | 2 | The application sanitizes content before it is sent to memcache to prevent injection attacks. |
| V1.3.10 | 2 | Format strings which might resolve in an unexpected or malicious way when used are sanitized before being processed. |
| V1.3.11 | 2 | The application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection. |
| V1.3.12 | 3 | Regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks. |

### V1.4 Memory, String, and Unmanaged Code

| ID | L | Requirement |
|---|---|---|
| V1.4.1 | 2 | The application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. |
| V1.4.2 | 2 | Sign, range, and input validation techniques are used to prevent integer overflows. |
| V1.4.3 | 2 | Dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities. |

### V1.5 Safe Deserialization

| ID | L | Requirement |
|---|---|---|
| V1.5.1 | 1 | The application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks. |
| V1.5.2 | 2 | Deserialization of untrusted data enforces safe input handling, such as using an allowlist of object types or restricting client-defined object types, to prevent deserialization attacks. Deserialization mechanisms that are explicitly defined as insecure must not be used with untrusted input. |
| V1.5.3 | 3 | Different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks. |

---

## V2 Validation and Business Logic (13 reqs, 4 at L1)

### V2.1 Validation and Business Logic Documentation

| ID | L | Requirement |
|---|---|---|
| V2.1.1 | 1 | The application's documentation defines input validation rules for how to check the validity of data items against an expected structure. This could be common data formats such as credit card numbers, email addresses, telephone numbers, or it could be an internal data format. |
| V2.1.2 | 2 | The application's documentation defines how to validate the logical and contextual consistency of combined data items, such as checking that suburb and ZIP code match. |
| V2.1.3 | 2 | Expectations for business logic limits and validations are documented, including both per-user and globally across the application. |

### V2.2 Input Validation

| ID | L | Requirement |
|---|---|---|
| V2.2.1 | 1 | Input is validated to enforce business or functional expectations for that input. This should either use positive validation against an allow list of values, patterns, and ranges, or be based on comparing the input to an expected structure and logical limits according to predefined rules. For L1, this can focus on input which is used to make specific business or security decisions. For L2 and up, this should apply to all input. |
| V2.2.2 | 1 | The application is designed to enforce input validation at a trusted service layer. While client-side validation improves usability and should be encouraged, it must not be relied upon as a security control. |
| V2.2.3 | 2 | The application ensures that combinations of related data items are reasonable according to the pre-defined rules. |

### V2.3 Business Logic Security

| ID | L | Requirement |
|---|---|---|
| V2.3.1 | 1 | The application will only process business logic flows for the same user in the expected sequential step order and without skipping steps. |
| V2.3.2 | 2 | Business logic limits are implemented per the application's documentation to avoid business logic flaws being exploited. |
| V2.3.3 | 2 | Transactions are being used at the business logic level such that either a business logic operation succeeds in its entirety or it is rolled back to the previous correct state. |
| V2.3.4 | 2 | Business logic level locking mechanisms are used to ensure that limited quantity resources (such as theater seats or delivery slots) cannot be double-booked by manipulating the application's logic. |
| V2.3.5 | 3 | High-value business logic flows require multi-user approval to prevent unauthorized or accidental actions. This could include but is not limited to large monetary transfers, contract approvals, access to classified information, or safety overrides in manufacturing. |

### V2.4 Anti-automation

| ID | L | Requirement |
|---|---|---|
| V2.4.1 | 2 | Anti-automation controls are in place to protect against excessive calls to application functions that could lead to data exfiltration, garbage-data creation, quota exhaustion, rate-limit breaches, denial-of-service, or overuse of costly resources. |
| V2.4.2 | 3 | Business logic flows require realistic human timing, preventing excessively rapid transaction submissions. |

---

## Key PASS/FAIL Patterns

### V1.2.4 Parameterized Queries (L1)

FAIL:
```javascript
// String concatenation — SQL injection
db.query("SELECT * FROM users WHERE id = " + req.params.id)
db.query(`SELECT * FROM users WHERE id = ${req.params.id}`)
```
```python
# f-string in SQL — SQL injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

PASS:
```javascript
// Parameterized query
db.query("SELECT * FROM users WHERE id = $1", [req.params.id])
// ORM
const user = await User.findByPk(req.params.id)
```
```python
# Parameterized
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
# ORM
user = User.objects.get(pk=user_id)
```

PHP and C#:
```php
mysqli_query($conn, "SELECT * FROM users WHERE id = '" . $_GET['id'] . "'");   // FAIL
$stmt = $conn->prepare("SELECT * FROM users WHERE id = ?");                     // PASS
$stmt->bind_param("i", $_GET['id']); $stmt->execute();
```
```csharp
db.Users.FromSqlRaw($"SELECT * FROM Users WHERE Id = {id}");      // FAIL (string interpolation into raw SQL)
db.Users.FromSqlInterpolated($"SELECT * FROM Users WHERE Id = {id}"); // PASS (parameterized by EF Core)
new NpgsqlCommand("SELECT ... WHERE id = @id", conn) { Parameters = { new("id", id) } };  // PASS
```

Framework defaults:
- Django ORM: PASS by default. `.raw()` and `.extra()` need manual check
- SQLAlchemy ORM: PASS with model queries. `text()` with f-strings is FAIL
- Prisma/TypeORM: PASS by default. `$queryRaw`/`query()` with interpolation is FAIL
- ActiveRecord: PASS with model queries. `.where("name = '#{name}'")` is FAIL

### V1.2.5 OS Command Injection (L1)

FAIL:
```javascript
const { exec } = require('child_process');
exec("convert " + req.body.filename + " output.png")  // command injection
```

PASS:
```javascript
const { execFile } = require('child_process');
execFile("convert", [req.body.filename, "output.png"])  // parameterized
```

PHP: `shell_exec("ping " . $_GET['ip'])`, `system()`, `exec()`, `passthru()`, backticks with request data are FAIL. `escapeshellarg()` per argument plus an allow-list is the minimum; avoid the shell where possible.
PHP file inclusion: `include($_GET['page'])` / `require` with request data is FAIL under V1.3.2 (dynamic code execution: the included file runs as code) and V5.3.2 (path built from user input). Map page names through a fixed array.
PHP output encoding (V1.2.1): `echo $_GET['q']` is FAIL; `echo htmlspecialchars($q, ENT_QUOTES, 'UTF-8')` is PASS. Plain PHP has no auto-escaping; Twig and Blade (`{{ }}`) do, but `{!! !!}` / `|raw` break it.

### V1.3.2 No eval() or Dynamic Code Execution (L1)

FAIL:
```javascript
eval(req.body.expression)
new Function(req.body.code)()
```

PASS:
```javascript
// Use a safe expression parser like mathjs
const result = math.evaluate(req.body.expression)
```

### V2.2.1 Server-side Input Validation (L1)

FAIL:
```javascript
// No validation — raw input used directly
app.post('/users', (req, res) => {
  db.query("INSERT INTO users (email) VALUES ($1)", [req.body.email])
})
```

PASS:
```javascript
// Zod validation before processing
const schema = z.object({ email: z.string().email() });
app.post('/users', (req, res) => {
  const data = schema.parse(req.body);  // throws on invalid
  db.query("INSERT INTO users (email) VALUES ($1)", [data.email])
})
```

Framework defaults:
- Django forms/serializers: PASS when used. Direct request.POST access without form is FAIL
- Spring @Valid + Bean Validation: PASS. Missing @Valid annotation is FAIL
- NestJS + class-validator: PASS with ValidationPipe. Missing decorators is FAIL
- Express: no built-in validation. Must use joi/zod/express-validator
