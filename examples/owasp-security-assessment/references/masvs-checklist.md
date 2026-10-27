# MASVS 2.1.0 Mobile Application Security

Load when: a mobile app is detected (React Native, Flutter, Ionic/Capacitor, .NET MAUI, Kotlin Multiplatform, native iOS or Android).
8 control groups, 24 controls. Control statements are verbatim from OWASP_MASVS.yaml; descriptions from controls/*.md. MASVS has no numbered sub-requirements; MASWE weaknesses and MASTG tests (mas.owasp.org) give test-level detail.
Cite controls by their full ID, e.g. MASVS-STORAGE-1. Look up one control: `grep -F "| MASVS-STORAGE-1 |" references/masvs-checklist.md`

The backend a mobile app talks to is assessed under ASVS, not here.

## Contents

- [MASVS-STORAGE Storage (2 controls)](#masvs-storage-storage-2-controls)
- [MASVS-CRYPTO Cryptography (2 controls)](#masvs-crypto-cryptography-2-controls)
- [MASVS-AUTH Authentication and Authorization (3 controls)](#masvs-auth-authentication-and-authorization-3-controls)
- [MASVS-NETWORK Network Communication (2 controls)](#masvs-network-network-communication-2-controls)
- [MASVS-PLATFORM Platform Interaction (3 controls)](#masvs-platform-platform-interaction-3-controls)
- [MASVS-CODE Code Quality (4 controls)](#masvs-code-code-quality-4-controls)
- [MASVS-RESILIENCE Resilience Against Reverse Engineering and Tampering (4 controls)](#masvs-resilience-resilience-against-reverse-engineering-and-tampering-4-controls)
- [MASVS-PRIVACY Privacy (4 controls)](#masvs-privacy-privacy-4-controls)

---

## MASVS-STORAGE Storage (2 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-STORAGE-1 | The app securely stores sensitive data. | Apps handle sensitive data coming from many sources such as the user, the backend, system services or other apps on the device and usually need to store it locally. The storage locations may be private to the app (e.g. its internal storage) or be public and therefore accessible by the user or other installed apps (e.g. public folders such as Downloads). This control ensures that any sensitive data that is intentionally stored by the app is properly protected independently of the target location. |
| MASVS-STORAGE-2 | The app prevents leakage of sensitive data. | There are cases when sensitive data is unintentionally stored or exposed to publicly accessible locations; typically as a side-effect of using certain APIs, system capabilities such as backups or logs. This control covers this kind of unintentional leaks where the developer actually has a way to prevent it. |

### What to check

Map to controls: insecure stores and backups -> STORAGE-1; logs, clipboard, screenshots, keyboard caches, shared/public folders -> STORAGE-2.

FAIL (plaintext stores for tokens, credentials, PII):
```javascript
await AsyncStorage.setItem('authToken', token)            // React Native: plaintext on disk
```
```swift
UserDefaults.standard.set(token, forKey: "authToken")     // iOS: plaintext, included in backups
```
```kotlin
getSharedPreferences("prefs", MODE_PRIVATE).edit().putString("token", token).apply()   // Android
```
```dart
final prefs = await SharedPreferences.getInstance(); prefs.setString('token', token);   // Flutter
```

PASS:
```javascript
await Keychain.setGenericPassword('user', token)          // react-native-keychain / expo-secure-store
```
```kotlin
EncryptedSharedPreferences.create(ctx, "secure_prefs", masterKey, AES256_SIV, AES256_GCM)   // or Keystore-wrapped keys
```
```dart
await const FlutterSecureStorage().write(key: 'token', value: token)
```

STORAGE-2 red flags: `Log.d`/`NSLog`/`console.log`/`print` with tokens or PII in release paths; `android:allowBackup="true"` without backup rules excluding sensitive files; files written to external storage; no `FLAG_SECURE` / screenshot protection on sensitive screens.

---

## MASVS-CRYPTO Cryptography (2 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-CRYPTO-1 | The app employs current strong cryptography and uses it according to industry best practices. | Cryptography plays an especially important role in securing the user's data - even more so in a mobile environment, where attackers having physical access to the user's device is a likely scenario. This control covers general cryptography best practices, which are typically defined in external standards. |
| MASVS-CRYPTO-2 | The app performs key management according to industry best practices. | Even the strongest cryptography would be compromised by poor key management. This control covers the management of cryptographic keys throughout their lifecycle, including key generation, storage and protection. |

### What to check

FAIL: hardcoded keys or IVs, `Cipher.getInstance("AES/ECB/...")`, `DES`/`RC4`/`MD5`/`SHA1` for security purposes, `java.util.Random`/`Math.random()` for secrets, key material stored next to the data it protects.
PASS: keys generated and held in Android Keystore / iOS Secure Enclave or Keychain (CRYPTO-2); AES-GCM or ChaCha20-Poly1305, SecureRandom / `SecRandomCopyBytes` (CRYPTO-1).
Cross-reference ASVS V11 when the same crypto code is shared with a backend.

---

## MASVS-AUTH Authentication and Authorization (3 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-AUTH-1 | The app uses secure authentication and authorization protocols and follows the relevant best practices. | Most apps connecting to a remote endpoint require user authentication and also enforce some kind of authorization. While the enforcement of these mechanisms must be on the remote endpoint, the apps also have to ensure that it follows all the relevant best practices to ensure a secure use of the involved protocols. |
| MASVS-AUTH-2 | The app performs local authentication securely according to the platform best practices. | Many apps allow users to authenticate via biometrics or a local PIN code. These authentication mechanisms need to be correctly implemented. Additionally, some apps might not have a remote endpoint, and rely fully on local app authentication. |
| MASVS-AUTH-3 | The app secures sensitive operations with additional authentication. | Some additional form of authentication is often desirable for sensitive actions inside the app. This can be done in different ways (biometric, pin, MFA code generator, email, deep links, etc) and they all need to be implemented securely. |

### What to check

AUTH-1 (remote auth/authz): tokens issued and enforced by the backend; client-side role or feature checks are not authorization. Token storage itself is STORAGE-1.
AUTH-2 (local auth: biometrics, PIN): the local check must unlock a cryptographic secret, not just flip a boolean.

FAIL (AUTH-2: event-bound biometric, bypassable with instrumentation):
```swift
context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: r) { ok, _ in
    if ok { self.proceedToApp() }
}
```

PASS (AUTH-2: biometric gates access to a Keychain item; backend validates what it unlocks):
```swift
let access = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly, .biometryCurrentSet, nil)
// store refresh token with this access control; read it after biometric prompt and send it to the server
```
Android equivalent: `BiometricPrompt` with a `CryptoObject` bound to a Keystore key created with `setUserAuthenticationRequired(true)`.

AUTH-3 (step-up): sensitive operations (payments, credential or e-mail change, device enrollment) require re-authentication or an extra factor, enforced server-side.

---

## MASVS-NETWORK Network Communication (2 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-NETWORK-1 | The app secures all network traffic according to the current best practices. | Ensuring data privacy and integrity of any data in transit is critical for any app that communicates over the network. This is typically done by encrypting data and authenticating the remote endpoint, as TLS does. However, there are many ways for a developer to disable the platform secure defaults, or bypass them completely by using low-level APIs or third-party libraries. This control ensures that the app is in fact setting up secure connections in any situation. |
| MASVS-NETWORK-2 | The app performs identity pinning for all remote endpoints under the developer's control. | Instead of trusting all the default root CAs of the framework or device, this control will make sure that only very specific CAs are trusted. This practice is typically called certificate pinning or public key pinning. |

### What to check

FAIL (NETWORK-1):
```xml
<application android:usesCleartextTraffic="true">                       <!-- AndroidManifest.xml -->
```
```xml
<key>NSAppTransportSecurity</key><dict><key>NSAllowsArbitraryLoads</key><true/></dict>   <!-- Info.plist -->
```
Also FAIL: custom `TrustManager`/`HostnameVerifier` that accepts all, `onReceivedSslError` calling `handler.proceed()`, Dart `badCertificateCallback = (...) => true`.

PASS (NETWORK-1 + NETWORK-2):
```xml
<network-security-config>
  <domain-config cleartextTrafficPermitted="false">
    <domain includeSubdomains="true">api.example.com</domain>
    <pin-set expiration="2027-01-01"><pin digest="SHA-256">...</pin><pin digest="SHA-256">...backup...</pin></pin-set>
  </domain-config>
</network-security-config>
```
iOS: `NSPinnedDomains` in Info.plist or TrustKit; OkHttp `CertificatePinner`. NETWORK-2 applies only to endpoints the developer controls.

---

## MASVS-PLATFORM Platform Interaction (3 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-PLATFORM-1 | The app uses IPC mechanisms securely. | Apps typically use platform provided IPC mechanisms to intentionally expose data or functionality. Both installed apps and the user are able to interact with the app in many different ways. This control ensures that all interactions involving IPC mechanisms happen securely. |
| MASVS-PLATFORM-2 | The app uses WebViews securely. | WebViews are typically used by apps that have a need for increased control over the UI. This control ensures that WebViews are configured securely to prevent sensitive data leakage as well as sensitive functionality exposure (e.g. via JavaScript bridges to native code). |
| MASVS-PLATFORM-3 | The app uses the user interface securely. | Sensitive data has to be displayed in the UI in many situations (e.g. passwords, credit card details, OTP codes in notifications). This control ensures that this data doesn't end up being unintentionally leaked due to platform mechanisms such as auto-generated screenshots or accidentally disclosed via e.g. shoulder surfing or sharing the device with another person. |

### What to check

PLATFORM-1 (IPC): exported Activities/Services/Receivers/Providers without permissions; implicit intents carrying sensitive data; `FileProvider` with broad paths; iOS URL schemes and universal links handled without validating the source/parameters; App Groups / pasteboard sharing secrets.
PLATFORM-2 (WebViews):
```kotlin
webView.settings.javaScriptEnabled = true
webView.addJavascriptInterface(Bridge(), "Android")   // FAIL when combined with:
webView.loadUrl(intent.getStringExtra("url"))          // attacker-controlled URL
webView.settings.allowFileAccessFromFileURLs = true     // FAIL
```
PASS: load only allow-listed origins, JS bridge exposed only to trusted content, file access disabled.
PLATFORM-3 (UI): sensitive screens protected from screenshots/screen recording and overlays (tapjacking: `filterTouchesWhenObscured`), sensitive fields masked, no secrets in notifications.

Deep-link parameters used without validation (e.g. setting an auth token from a link) are a PLATFORM-1 finding and also CODE-4.

---

## MASVS-CODE Code Quality (4 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-CODE-1 | The app requires an up-to-date platform version. | Every release of the mobile OS includes security patches and new security features. By supporting older versions, apps stay vulnerable to well-known threats. This control ensures that the app is running on an up-to-date platform version so that users have the latest security protections. |
| MASVS-CODE-2 | The app has a mechanism for enforcing app updates. | Sometimes critical vulnerabilities are discovered in the app when it is already in production. This control ensures that there is a mechanism to force the users to update the app before they can continue using it. |
| MASVS-CODE-3 | The app only uses software components without known vulnerabilities. | To be truly secure, a full whitebox assessment should have been performed on all app components. However, as it usually happens with e.g. for third-party components this is not always feasible and not typically part of a penetration test. This control covers "low-hanging fruit" cases, such as those that can be detected just by scanning libraries for known vulnerabilities. |
| MASVS-CODE-4 | The app validates and sanitizes all untrusted inputs. | Apps have many data entry points including the UI, IPC, the network, the file system, etc. This incoming data might have been inadvertently modified by untrusted actors and may lead to bypass of critical security checks as well as classical injection attacks such as SQL injection, XSS or insecure deserialization. This control ensures that this data is treated as untrusted input and is properly verified and sanitized before it's used. |

### What to check

CODE-1: platform floor. Check `minSdkVersion`/`minSdk` in Gradle, `IPHONEOS_DEPLOYMENT_TARGET` / `platform :ios` in Podfile, Flutter/React Native min versions. FAIL when it permits OS versions without current security patches and no documented rationale.
CODE-2: forced update mechanism. PASS: backend minimum-version check or Play In-App Updates (immediate) that blocks outdated clients. NOT VERIFIED is common when this is server-driven and the server is out of scope.
CODE-3: vulnerable components. Check Gradle/CocoaPods/SPM/pub/npm lock files against known CVEs; note native libraries vendored in the repo.
CODE-4: untrusted input. Deep links, intents, IPC, WebView messages, files, QR codes, push payloads; unsafe deserialization (`ObjectInputStream`, `NSKeyedUnarchiver` without secure coding); SQL built by string concatenation in local SQLite.

---

## MASVS-RESILIENCE Resilience Against Reverse Engineering and Tampering (4 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-RESILIENCE-1 | The app validates the integrity of the platform. | Running on a platform that has been tampered with can be very dangerous for apps, as this may disable certain security features, putting the data of the app at risk. Trusting the platform is essential for many of the MASVS controls relying on the platform being secure (e.g. secure storage, biometrics, sandboxing, etc.). This control tries to validate that the OS has not been compromised and its security features can thus be trusted. |
| MASVS-RESILIENCE-2 | The app implements anti-tampering mechanisms. | Apps run on a user-controlled device, and without proper protections it's relatively easy to run a modified version locally (e.g. to cheat in a game, or enable premium features without paying), or upload a backdoored version of it to third-party app stores. This control tries to ensure the integrity of the app's intended functionality by preventing modifications to the original code and resources. |
| MASVS-RESILIENCE-3 | The app implements anti-static analysis mechanisms. | Understanding the internals of an app is typically the first step towards tampering with it (either dynamically, or statically). This control tries to impede comprehension by making it as difficult as possible to figure out how an app works using static analysis. |
| MASVS-RESILIENCE-4 | The app implements anti-dynamic analysis techniques. | Sometimes pure static analysis is very difficult and time consuming so it typically goes hand in hand with dynamic analysis. Observing and manipulating an app during runtime makes it much easier to decipher its behavior. This control aims to make it as difficult as possible to perform dynamic analysis, as well as prevent dynamic instrumentation which could allow an attacker to modify the code at runtime. |

### What to check

Assess only when the depth tier includes resilience (see level-selection.md); otherwise mark N/A with that reason.
RESILIENCE-1: root/jailbreak/emulator detection, Play Integrity / App Attest.
RESILIENCE-2: signature/integrity checks, tamper response.
RESILIENCE-3: obfuscation (R8/ProGuard `minifyEnabled true` with non-trivial rules, string encryption).
RESILIENCE-4: anti-debugging, `android:debuggable` not set in release, Frida/hook detection.
These raise attacker cost; they never replace server-side enforcement.

---

## MASVS-PRIVACY Privacy (4 controls)

| ID | Control | What it covers |
|---|---|---|
| MASVS-PRIVACY-1 | The app minimizes access to sensitive data and resources. | Apps should only request access to the data they absolutely need for their functionality and always with informed consent from the user. This control ensures that apps practice data minimization and restricts access control, reducing the potential impact of data breaches or leaks. Furthermore, apps should share data with third parties only when necessary, and this should include enforcing that third-party SDKs operate based on user consent, not by default or without it. Apps should prevent third-party SDKs from ignoring consent signals or from collecting data before consent is confirmed. Additionally, apps should be aware of the 'supply chain' of SDKs they incorporate, ensuring that no data is unnecessarily passed down their chain of dependencies. This end-to-end responsibility for data aligns with recent SBOM regulatory requirements, making apps more accountable for their data practices. |
| MASVS-PRIVACY-2 | The app prevents identification of the user. | Protecting user identity is crucial. This control emphasizes the use of unlinkability techniques like data abstraction, anonymization and pseudonymization to prevent user identification and tracking. Another key aspect addressed by this control is to establish technical barriers when employing complex 'fingerprint-like' signals (e.g. device IDs, IP addresses, behavioral patterns) for specific purposes. For instance, a fingerprint used for fraud detection should be isolated and not repurposed for audience measurement in an analytics SDK. This ensures that each data stream serves its intended function without risking user privacy. |
| MASVS-PRIVACY-3 | The app is transparent about data collection and usage. | Users have the right to know how their data is being used. This control ensures that apps provide clear information about data collection, storage, and sharing practices, including any behavior a user wouldn't reasonably expect, such as background data collection. Apps should also adhere to platform guidelines on data declarations. |
| MASVS-PRIVACY-4 | The app offers user control over their data. | Users should have control over their data. This control ensures that apps provide mechanisms for users to manage, delete, and modify their data, and change privacy settings as needed (e.g. to revoke consent). Additionally, apps should re-prompt for consent and update their transparency disclosures when they require more data than initially specified. |

### What to check

PRIVACY-1: permissions in AndroidManifest/Info.plist justified by features; least-privilege variants (approximate location, photo picker).
PRIVACY-2: no persistent device identifiers (IMEI, MAC, Android ID used for tracking), IDFA/GAID only with consent (ATT on iOS).
PRIVACY-3: privacy manifest (`PrivacyInfo.xcprivacy`), Data safety declarations, and in-app disclosure match what code and SDKs actually collect.
PRIVACY-4: in-app consent controls, opt-out, data export and deletion paths.
Inventory third-party SDKs (analytics, ads, crash reporting) and what each receives.

