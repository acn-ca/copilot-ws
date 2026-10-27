# 00 — Prerequisites

> Complete this before the workshop starts. It takes about 10-15 minutes.

---

## Before you start

The workshop runs in GitHub Codespaces, so you do not need to install Node.js, Java, Gradle, or an editor on your computer.

You will need:
- A GitHub account with permission to use Codespaces and available Codespaces quota or billing.
- GitHub Copilot access for the Copilot activities.
- A modern web browser and an internet connection.

## Create your Codespace

1. Open [acn-ca/copilot-ws](https://github.com/acn-ca/copilot-ws) on GitHub and select **Fork** to create a copy in your account.
2. Open your fork, select **Code** → **Codespaces** → **Create codespace on main**.
3. Wait for the Codespace to finish starting, then open a terminal.

Check that the required runtimes are available:

```bash
node --version
java --version
```

Node.js should be version 24 or later, and Java should report version 25. If either check fails or you cannot create a Codespace, ask the workshop facilitator for help before proceeding.

## Start the webshop

Open two terminals in the Codespace. In the first terminal, start the backend:

```bash
cd backend
./gradlew bootRun
```

In the second terminal, start the frontend:

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

The first backend startup may take a few minutes while the Gradle Wrapper downloads Gradle and the project dependencies.

## Verify the setup

Wait for the backend log to report that `WebshopApplication` has started and for Vite to report that it is ready. In a third terminal, run:

```bash
curl -fsS http://localhost:8080/api/products
```

The command should return a JSON array of products. In the Codespace's **Ports** tab, find port **5173** and select **Open in Browser**. The address that opens is your `<frontend-codespace-url>`; use it whenever a workshop step asks you to open the frontend. Codespaces assigns a forwarded address for each Codespace, so do not type a `localhost` URL into your browser.

For backend pages, find port **8080** in the same **Ports** tab and use its forwarded address as `<backend-codespace-url>`.

Finally, open Copilot Chat in the Codespace and ask, `Explain this project in one sentence.` Confirm that Copilot responds. If you are asked to sign in or do not have Copilot access, ask the workshop facilitator for help.

Continue to Part 01 only after the API, frontend, and Copilot checks succeed. If a check fails, share the terminal error with the facilitator before continuing.

> **Note:** The backend uses the Gradle Wrapper, so you do not need a global Gradle installation.

---

## Troubleshooting

| Symptom | What to check |
|---------|---------------|
| Node.js is older than 24 or Java is not version 25 | Stop and ask the facilitator for help with the Codespace environment. |
| `curl` cannot connect to port 8080 | Check that `./gradlew bootRun` is still running and that the backend startup completed. |
| Port 5173 is missing or the page does not load | Check that Vite is still running with `--host 0.0.0.0`, then reopen port 5173 from the **Ports** tab. |
| Gradle is still downloading dependencies | Wait for the first startup to finish; it can take a few minutes. |

When the API returns products and the frontend opens, you're ready! Head to [Part 1 →](./01-copilot-instructions.md).
