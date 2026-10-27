# 04 — Security Review Agents & MCP

**Time:** ~15 minutes  
**Features:** Code review agent, security reviewer agent (`.github/agents/`), helper skills (`.github/skills/`), environment setup

**Learning goals:**
- Understand how the built-in code review agent can help identify security issues
- Build a custom security reviewer agent and add a helper skill with security guidance
- Observe how pre-configured environments enable complex automation

> **Note:** This part demonstrates security-focused Copilot workflows using custom agents, reusable skills, and pre-configured environments.

---

## 🔍 1. Built-in Review Agent & Custom Agents

Let's explore **Agents** — specialized AI personas equipped with instructions, tools, and multi-step processes.

> 💡 **Skills vs. Agents:**
> - **Skills** (`.github/skills/`): Reusable security expertise. They teach Copilot *what* security context, checks, and guidance to apply.
> - **Agents** (`.github/agents/`): Specialized workflow runners. They give Copilot tools and multi-step procedures to review code for security issues.

### Built-in Code Review Agent

The **code review agent** analyses your staged or unstaged changes and surfaces only issues that genuinely matter: bugs, security problems, and logic errors. It deliberately ignores style and formatting.

**Try it:**

1. Make sure you have unstaged changes from Parts 2 and 3
2. Open Copilot Chat
3. Type:
   ```
   Review my changes
   ```
   or select the `code-review` agent if available in your IDE.

**What to observe:**
- The agent looks at diffs, not just individual files
- It cross-references your changes with the rest of the codebase
- It won't comment on indentation or variable naming — only real issues

---

### Build a Custom Security Reviewer — `.github/agents/`

The built-in agent provides a general review. A custom security reviewer can apply a focused checklist tailored to your repository.

You can define **Custom Agents** in `.github/agents/name.agent.md`.

#### How custom agents work

Each agent file contains:
- **YAML Frontmatter:** Configures the agent name, description, and available tools (`codebase`, `terminal`, etc.)
- **System Instructions:** Defines the agent's specific role, checklist, prioritization rules, and output format.

**Try it:**

1. Create `.github/agents/security-reviewer.agent.md`.
2. Give the agent a security review role and a checklist relevant to this webshop, such as authorization, input validation, sensitive data exposure, and dependency risks.
3. Ask the agent to review your changes and report actionable findings with affected files and severity.

### Add a Helper Skill — `.github/skills/`

Keep reusable security review guidance separate from the agent workflow so it can be shared and improved independently.

**Try it:**

1. Create `.github/skills/security-review/SKILL.md`.
2. Add concise security review guidance for the webshop, including the checks and reporting expectations you want Copilot to follow.
3. Update the security reviewer agent instructions to use this skill when reviewing code.

> 💡 **SDLC role:** The security reviewer acts as a focused **Application Security Engineer**, while the helper skill keeps the team's review guidance reusable.

#### Agent Plugins & Extension Marketplaces

Beyond building custom agents and skills in your repository, you can also explore **Agent Plugins** and extension marketplaces. These marketplaces offer downloadable, pre-packaged bundles of agents, skills, tools, and instructions for workflows such as security auditing. Installing a suitable bundle can provide reusable security guidance without authoring every agent or skill from scratch.

---

## ⚙️ 2. Environment Setup — `copilot-setup-steps.yml`

Open `.github/copilot-setup-steps.yml` — this file pre-installs dependencies needed for testing and browser automation when agents run in automated or cloud environments.

**Current setup includes:**
- Node.js + npm (for frontend dependencies)
- JDK 25 (for backend compilation)
- Playwright browsers (for automated testing)

**Try it in Copilot Chat:**
```
Explain what dependencies are installed in copilot-setup-steps.yml and why each one matters for this webshop project.
```

Or ask:
```
Add a step to copilot-setup-steps.yml that installs Playwright system dependencies for headless testing.
```

> 💡 **SDLC role:** This is a **DevOps / Security QA** tool — ensuring the test environment is ready for repeatable security checks, just like a CI machine setup.

---

## 🎭 Bonus — Create a Security Testing Agent with Playwright MCP

Copilot can use external tools through the **Model Context Protocol (MCP)**. The Playwright MCP server (pre-configured in `.mcp.json`) lets an agent interact with the webshop in a browser and check security-relevant user flows.

**Try it:**

1. Make sure both frontend and backend are running (see [Part 00](./00-prerequisites.md)).
2. Verify the Playwright MCP server is connected in Copilot Chat.
3. Create a `security-testing.agent.md` agent that uses the Playwright MCP tools to exercise security-relevant flows, such as form validation, access boundaries, and whether sensitive data appears in the UI.
4. Ask the agent to test the webshop at `http://localhost:5173` and report reproducible findings without changing application data beyond the test flow.

> 💡 **SDLC role:** This is a **Security QA Engineer** workflow — using browser automation to check security behavior through the same interface customers use.

---

## Summary — SDLC role map

| Feature | Who benefits most | What it replaces |
|---------|-------------------|------------------|
| Code review & security reviewer agent (`.github/agents/`) | Developers, Application Security | General review without a focused security checklist |
| Security helper skill (`.github/skills/`) | Application Security, Developers | Repeating security guidance across reviews |
| Playwright security testing agent (`.mcp.json`, bonus) | Security QA | Manual browser checks of security-relevant flows |
| `copilot-setup-steps.yml` | DevOps, Security QA | Manual test environment setup |

---

**Finished the core workshop! 🎉**  
If you have time, explore the bonus tasks:

- [BONUS 01 — MCP Servers →](./BONUS-01-mcp-servers.md)
- [BONUS 02 — Testing →](./BONUS-02-testing.md)
- [BONUS 03 — CI/CD →](./BONUS-03-ci-cd.md)
- [BONUS 04 — Custom Instructions Deep Dive →](./BONUS-04-custom-instructions.md)
