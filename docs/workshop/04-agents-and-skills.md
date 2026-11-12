# 04 — Security Review Agents & Skills

**Time:** ~15 minutes
**Features:** Copilot Chat review, custom agent (`.github/agents/`), expert skill (`.github/skills/`)

**What you'll do:**
1. Ask Copilot for a quick security review of your changes.
2. Build your own security reviewer **agent** and give it expert knowledge through a **skill**.
3. Compare the two reviews.

> 💡 **Agents vs. skills:**
> - An **agent** (`.github/agents/`) is the reviewer. It knows its role, its steps, and that it should write a report.
> - A **skill** (`.github/skills/`) is the knowledge, like a checklist our security experts wrote for it.

> **New to this?** No experience needed. Paste the prompts into Copilot Chat (in **Agent** mode) as they are. When Copilot asks to create files or run a command, click **Allow**.

---

## Step 1 — Quick review of your changes

```
Review my changes for security issues. Save the findings to
reports/1-quick-review.md.
```

Copilot looks at the code you changed in Parts 2 and 3 and reports bugs, security problems and logic errors.

---

## Step 2 — Add the expert knowledge

Our security experts wrote a skill based on the OWASP security standards. Add it to your project:

```
Copy examples/owasp-security-assessment into .github/skills/.
```

> 💡 Take a quick look inside `.github/skills/owasp-security-assessment/`. Besides `SKILL.md`, it has a `references/` folder with OWASP checklists and a `scripts/` folder. A skill can bring its own reference material and tools, not just instructions.

---

## Step 3 — Build your security reviewer agent

1. For inspiration, open `.github/agents/todo.agent.md` and see how it describes the agent's role and steps.
2. In Copilot Chat, type:
   ```
   /create-agent Create a security reviewer for this webshop. It always uses the
   owasp-security-assessment skill in Quick Scan mode, reviews the entire app in
   backend/ and frontend/ as the files are now, and writes its report to the
   reports/ folder. It needs to read files, write files and run terminal commands.
   ```
3. Read the draft, ask about anything unfamiliar, and save it under `.github/agents/`.

---

## Step 4 — Run your agent

1. Select your new agent from the agent picker in Copilot Chat.
2. Type:
   ```
   Review the webshop from scratch and write the report to
   reports/2-security-agent.md.
   ```

---

## Step 5 — Compare

```
Compare reports/1-quick-review.md and reports/2-security-agent.md in a table:
which findings appear in which report, and which recommendations are the most
specific and actionable?
```

**Discuss:**
- What did your agent find that the quick review didn't? Were any of those issues outside the code you wrote yourself?
- Which report could you hand to an auditor? Does each finding cite evidence and a requirement?
- Same Copilot, different knowledge: where should your team put its security expertise?

> 💡 **SDLC role:** Your agent is a reusable **Application Security Engineer**, and the skill is its expertise. Improve the skill once, and every review gets better.

---

### Going further (optional)

Explore **Agent Plugins** and extension marketplaces. They offer ready-made bundles of agents, skills and tools, for security auditing for example, that you can install instead of writing your own.
