# 🛒 Copilot Workshop: Webshop Showcase

An interactive workshop that teaches GitHub Copilot features — **copilot-instructions**, **agents**, **skills**, and **commands** (`/explain`, `/fix`) — using a real webshop application as the demonstration vehicle. Workshop activities run in GitHub Codespaces.

**Stack:** Vite + React + TypeScript · Kotlin + Spring Boot · H2 Database

---

## What you'll learn

This workshop focuses on **Copilot features and patterns** you can apply to any project:

| Feature | What it teaches |
|---------|---------|
| `copilot-instructions.md` | How to encode project knowledge into a persistent, reusable system prompt |
| **Skills** (`.github/skills/`) | How to package reusable domain expertise and coding guidance (frontend-engineer, backend-engineer, designer) |
| **Agents** (`.github/agents/`) | How to create autonomous task-runners (todo tracker, code review, etc.) |
| **Inline completions** | How Copilot uses instructions + context to generate code suggestions |
| **Chat commands** (`/explain`, `/fix`) | How to use Copilot for code understanding and debugging |
| **`@workspace`** | How to enable cross-file understanding in chat |
| **Code review agent** | How to automate quality gates (bugs, logic errors, regressions) |

The **webshop** is a real-world codebase used to demonstrate these features in practice — a backend API, frontend UI, and database layer that creates a need for all the Copilot patterns.

---

## How to Use This Workshop

Complete Parts 01–04 sequentially. Each part focuses on a specific Copilot capability (instructions → skills → commands → agents). The webshop stubs are your vehicle for practice.

**Key mindset:** You're not building a finished webshop. You're learning **how to make Copilot effective** across the full stack. When you finish, you'll know how to apply these patterns to your own projects.

---

## Start in GitHub Codespaces

### Before you start

- A GitHub account with permission to use Codespaces and available Codespaces quota or billing.
- GitHub Copilot access for the Copilot activities.
- A modern web browser and an internet connection.

You do not need to install Node.js, Java, Gradle, or an editor on your own computer. Codespaces provides the browser-based VS Code environment.

Follow [Part 00 — Prerequisites](docs/workshop/00-prerequisites.md) to fork the workshop repository and create your Codespace.

---

## Workshop Guide

| Part | Topic | Time | Link |
|------|-------|------|------|
| 00 | Prerequisites & setup | 10–15 min | [→](docs/workshop/00-prerequisites.md) |
| 01 | Copilot Instructions | 20 min | [→](docs/workshop/01-copilot-instructions.md) |
| 02 | Complete the Backend | 20 min | [→](docs/workshop/02-complete-the-backend.md) |
| 03 | Wire the Frontend | 20 min | [→](docs/workshop/03-wire-the-frontend.md) |
| 04 | Security Review Agents & Skills | 15 min | [→](docs/workshop/04-agents-and-skills.md) |

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
| `frontend/src/pages/ProductsPage.tsx` | 🔧 Stub | Fetching products and rendering the page are workshop tasks |
| `frontend/src/pages/CheckoutPage.tsx` | 🔧 Stub | Participants implement form + submit |