# 🛒 Copilot Workshop: Webshop Showcase

An interactive workshop that teaches GitHub Copilot features — **copilot-instructions**, **agents**, **skills**, **commands** (`/explain`, `/fix`, `/tests`), and **MCP servers** — using a real webshop application as the demonstration vehicle.

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
| **Playwright MCP server** | How to connect Copilot to external tools (browser automation, testing) |
| **`copilot-setup-steps.yml`** | How to pre-configure environments for automation |

The **webshop** is a real-world codebase used to demonstrate these features in practice — a backend API, frontend UI, and database layer that creates a need for all the Copilot patterns.

---

## How to Use This Workshop

**If you're learning Copilot features:** Complete Parts 01–04 sequentially. Each part focuses on a specific Copilot capability (instructions → skills → commands → agents/MCP). The webshop stubs are your vehicle for practice.

**If you're setting up your own project:** Study how this project uses `copilot-instructions.md`, skills, and agents. Copy these patterns to your codebase — the webshop is a template, not the end goal.

**Key mindset:** You're not building a finished webshop. You're learning **how to make Copilot effective** across the full stack. When you finish, you'll know how to apply these patterns to your own projects.

---

## Quick Start

### Prerequisites
Node.js 24+, JDK 25, GitHub Copilot access. → [Detailed setup](docs/workshop/00-prerequisites.md)

### Run the frontend
```bash
cd frontend
npm install
npm run dev
# → http://localhost:5173
```

### Run the backend
```bash
cd backend
./gradlew bootRun   # or .\gradlew.bat bootRun on Windows
# → http://localhost:8080/api
# → http://localhost:8080/h2-console  (H2 database browser)
```

---

## Workshop Guide

| Part | Topic | Time | Link |
|------|-------|------|------|
| 00 | Prerequisites & setup | Pre-read | [→](docs/workshop/00-prerequisites.md) |
| 01 | Copilot Instructions | 20 min | [→](docs/workshop/01-copilot-instructions.md) |
| 02 | Complete the Backend | 20 min | [→](docs/workshop/02-complete-the-backend.md) |
| 03 | Wire the Frontend | 20 min | [→](docs/workshop/03-wire-the-frontend.md) |
| 04 | Security Review Agents & MCP | 15 min | [→](docs/workshop/04-agents-and-skills.md) |

### Bonus Tasks (self-paced)

| Bonus | Topic | Link |
|-------|-------|------|
| 01 | Security testing agent with Playwright MCP | [→](docs/workshop/04-agents-and-skills.md) |

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