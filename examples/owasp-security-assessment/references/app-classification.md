# Application Classification

Detect components, map each to a standard, and decide what is out of scope.

## Stack Detection

### Ecosystem

| File present | Ecosystem | Lock / resolved versions |
|---|---|---|
| `go.mod` | Go | `go.sum` |
| `pom.xml` / `build.gradle(.kts)` | Java/Kotlin | `gradle.lockfile`, effective POM |
| `*.sln`, `*.csproj`, `Directory.Packages.props` | .NET | `packages.lock.json` (often absent: then central package versions in `Directory.Packages.props`) |
| `Cargo.toml` | Rust | `Cargo.lock` |
| `pyproject.toml` / `requirements.txt` / `Pipfile` | Python | `poetry.lock` / `Pipfile.lock` / `uv.lock` |
| `Gemfile` | Ruby | `Gemfile.lock` |
| `composer.json` | PHP | `composer.lock` |
| `*.php` with no `composer.json` | PHP without dependency manager | none; inspect includes |
| `package.json` | Node.js | `package-lock.json` / `yarn.lock` / `pnpm-lock.yaml` |
| `pubspec.yaml` | Dart/Flutter | `pubspec.lock` |
| `CMakeLists.txt`, `meson.build`, `vcpkg.json`, `conanfile.*`, `Externals/` | C/C++ | vendored sources, submodules, `vcpkg.json` |
| `Dockerfile`, `docker-compose*.yml`, `*.bicep`, `*.tf`, Helm charts | Deployment / IaC | evidence for ASVS V12/V13, not a component |

### Component Type Detection

| Signal | Component | Standard |
|---|---|---|
| express, fastify, koa, NestJS, Django, Flask, FastAPI, Rails, Spring, ASP.NET Core, Laravel, Gin, Axum | Web/API | ASVS |
| Deployed service whose input is a message queue or event stream (Kafka, RabbitMQ, SQS/SNS, Pub/Sub, Service Bus; rapids-and-rivers, Spring Cloud Stream, MassTransit), usually with an embedded health/metrics HTTP server | Event-driven backend | ASVS (see assessment-rules.md "Event-driven services") |
| Server-side PHP pages (`$_GET`, `$_POST`, `$_REQUEST`, `mysqli_*`) | Web app | ASVS |
| Identity server / OAuth / OIDC endpoints (`/authorize`, `/token`, `.well-known/openid-configuration`, OpenIddict, Duende IdentityServer) | Authorization server / OpenID provider | ASVS incl. V10.4, V10.6 |
| react (without react-native), vue, angular, svelte | SPA frontend | ASVS V3 |
| Next.js, Nuxt, SvelteKit | Hybrid SSR + API | ASVS V3 + V4 |
| react-native, Flutter, Ionic, Capacitor, .NET MAUI, Kotlin Multiplatform | Mobile (cross-platform) | MASVS |
| `*.xcodeproj`, SwiftUI, UIKit | iOS native | MASVS |
| `AndroidManifest.xml`, Android Gradle plugin, Jetpack Compose | Android native | MASVS |
| torch, tensorflow, scikit-learn, transformers | ML training / inference | AISVS |
| openai, anthropic, langchain, llamaindex, semantic-kernel | LLM integration | AISVS |
| chromadb, pinecone, weaviate, pgvector | RAG / vector store | AISVS (C8) |
| crewai, autogen, agent frameworks, MCP servers or clients | Agentic AI | AISVS (C9, C10) |

React Native, Flutter, Ionic and Capacitor produce mobile apps: apply MASVS, not ASVS V3.
An Android or iOS app found inside a larger repo (e.g. `Source/Android/`) is its own MASVS component even when the rest of the repo is not.

## Out-of-scope components

None of the three standards covers native desktop applications, games, emulators, CLIs, drivers, firmware, or general-purpose libraries. Do not force-fit them.

- Say which components are out of scope and why, in the scope table and in Limitations.
- If such a component has network features (HTTP client, update checker, online service integration, embedded web server), you may report a short "informative" list mapping those features to the closest ASVS requirements (typically V12 TLS, V15 dependencies, V1.5 deserialization, V13.3 secrets). Label it informative, keep it out of the ASVS dashboard, and do not assign a level or score.
- If no component maps to any standard, stop after Phase 0: report the classification and recommend the threat-modeling skill or a secure-code review instead.

## Monorepo Handling

Detection: multiple manifests in subdirectories, workspace configs (`pnpm-workspace.yaml`, `settings.gradle`, `.sln` with many projects), docker-compose with multiple services.

1. Classify each service directory independently
2. Identify shared libraries (`packages/`, `libs/`, `common/`, `shared/`, `src/Common*`)
3. Shared libraries inherit the strictest consumer level and the union of applicable standards
4. Map cross-service dependencies

Flag: inconsistent auth, shared secrets, missing inter-service TLS, divergent dependency versions.

## Hybrid Patterns

| Pattern | Standards |
|---|---|
| SPA + API backend | ASVS (V3 for frontend, V4 for API, the rest for both) |
| Mobile app + API backend | MASVS (mobile) + ASVS (API) |
| Web app with AI features | ASVS (web) + AISVS (AI components) |
| Full-stack monorepo | Potentially all three |
| Electron/Tauri | ASVS V3 + V15 for the web layer; note nodeIntegration/contextIsolation risks |
| Native desktop app or engine with a mobile port | MASVS for the mobile app, including the shared native code it executes; desktop-only code out of scope (assessment-rules.md) |

When the codebase is an API backend serving a mobile app (mobile code not in repo), note mobile-relevant API concerns: token refresh, certificate pinning support, device binding.
