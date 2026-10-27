# 🛒 Copilot Workshop: Webshop Showcase

An interactive workshop that teaches GitHub Copilot features — **copilot-instructions**, **agents**, **skills**, and **commands** (`/explain`, `/fix`, `/tests`) — using a real webshop application as the demonstration vehicle. Workshop activities run in GitHub Codespaces.

**Stack:** Vite + React + TypeScript · Kotlin + Spring Boot · H2 Database

---

## What you'll learn

This workshop focuses on **Copilot features and patterns** you can apply to any project:

| Feature | What it teaches |
|---------|---------|
| `copilot-instructions.md` | How to encode project knowledge into a persistent, reusable system prompt |
| **Skills** (`.github/skills/`) | How to package domain knowledge into specialized personas (frontend-engineer, backend-engineer, designer) |
| **Agents** (`.github/agents/`) | How to create autonomous task-runners (todo tracker, code review, etc.) |
| **Inline completions** | How Copilot uses instructions + context to generate code suggestions |
| **Chat commands** (`/explain`, `/fix`, `/tests`) | How to use Copilot for code understanding, debugging, and test generation |
| **`@workspace`** | How to enable cross-file understanding in chat |
| **Code review agent** | How to automate quality gates (bugs, logic errors, regressions) |
| **Browser-based security testing** | How to test security-relevant user flows |
| **`copilot-setup-steps.yml`** | How to pre-configure environments for automation |

The **webshop** is a real-world codebase used to demonstrate these features in practice — a backend API, frontend UI, and database layer that creates a need for all the Copilot patterns.

---

## How to Use This Workshop

**If you're learning Copilot features:** Complete Parts 01–04 sequentially. Each part focuses on a specific Copilot capability (instructions → skills → commands → agents). The webshop stubs are your vehicle for practice.

**If you're setting up your own project:** Study how this project uses `copilot-instructions.md`, skills, and agents. Copy these patterns to your codebase — the webshop is a template, not the end goal.

**Key mindset:** You're not building a finished webshop. You're learning **how to make Copilot effective** across the full stack. When you finish, you'll know how to apply these patterns to your own projects.

---

## Start in GitHub Codespaces

### Before you start

- A GitHub account with permission to use Codespaces and available Codespaces quota or billing.
- GitHub Copilot access for the Copilot activities.
- A modern web browser and an internet connection.

You do not need to install Node.js, Java, Gradle, or an editor on your own computer. Codespaces provides the browser-based VS Code environment.

### Create your Codespace

1. Open the workshop repository on GitHub.
2. Select **Code** → **Codespaces** → **Create codespace on main**.
3. Wait for the Codespace to finish starting, then open a terminal in the Codespace.

Before starting the workshop, confirm the required runtimes are available:

```bash
node --version
java --version
```

Node.js should be version 24 or later, and Java should report version 25. If either check fails, or Codespaces is unavailable for your account, ask the workshop facilitator for help before proceeding.

### Start the webshop

Use two terminals in the Codespace. In the first terminal, start the backend:

```bash
cd backend
./gradlew bootRun
```

In a second terminal, start the frontend:

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

The first backend startup may take a few minutes while Gradle downloads dependencies.

### Verify everything is ready

Wait for the backend log to report that `WebshopApplication` has started and for Vite to report that it is ready. Then, in another terminal, check the API:

```bash
curl -fsS http://localhost:8080/api/products
```

The command should return a JSON array of products. In the Codespace's **Ports** tab, find port **5173** and select **Open in Browser**; the webshop frontend should load. The address that opens is your `<frontend-codespace-url>`. Use the **Ports** tab to find the forwarded address for any other port you need, such as **8080** for backend pages; do not type `localhost` URLs into your browser. Continue to Part 01 only after the API check succeeds and the frontend page opens. If either check fails, share the terminal error with the facilitator before continuing.

For more setup details, see [Part 00 — Prerequisites](docs/workshop/00-prerequisites.md).

---

## Workshop Guide

| Part | Topic | Time | Link |
|------|-------|------|------|
| 00 | Prerequisites & setup | Pre-read | [→](docs/workshop/00-prerequisites.md) |
| 01 | Copilot Instructions | 20 min | [→](docs/workshop/01-copilot-instructions.md) |
| 02 | Complete the Backend | 20 min | [→](docs/workshop/02-complete-the-backend.md) |
| 03 | Wire the Frontend | 20 min | [→](docs/workshop/03-wire-the-frontend.md) |
| 04 | Security Review Agents | 15 min | [→](docs/workshop/04-agents-and-skills.md) |

### Bonus Tasks (self-paced)

| Bonus | Topic | Link |
|-------|-------|------|
| 01 | Security testing agent with browser automation | [→](docs/workshop/04-agents-and-skills.md) |

---

## Architecture

```
browser
  └── frontend/          Vite + React + TypeScript  :5173
        └── fetch
              └── backend/   Kotlin + Spring Boot    :8080
                    └── JPA
                          └── H2 (in-memory)
```

### What's given vs. what participants build

| File | Status | Notes |
|------|--------|-------|
| `backend/model/`, `repository/` | ✅ Complete | JPA entities and Spring Data repos |
| `backend/controller/ProductController.kt` | 🔧 Partial | GET works; POST is a stub |
| `backend/controller/OrderController.kt` | 🔧 Stub | All endpoints are TODOs |
| `backend/service/` | 🔧 Stub | Participants implement with Copilot |
| `frontend/src/types/index.ts` | ✅ Complete | All shared TypeScript types |
| `frontend/src/components/Header.tsx` | ✅ Complete | Navigation bar |
| `frontend/src/services/api.ts` | 🔧 Partial | `fetchProducts` works; `createOrder` is a stub |
| `frontend/src/components/ProductCard.tsx` | 🔧 Stub | Participants build with Copilot |
| `frontend/src/pages/ProductsPage.tsx` | 🔧 Partial | State wired; fetch not connected |
| `frontend/src/pages/CheckoutPage.tsx` | 🔧 Stub | Participants implement form + submit |