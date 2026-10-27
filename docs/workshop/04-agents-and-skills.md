# 04 — Security Review Agents & MCP

**Time:** ~15 minutes  
**Features:** Code review agent, security reviewer agent (`.github/agents/`), helper skills (`.github/skills/`), environment setup

**Learning goals:**
- Understand how the built-in code review agent can help identify security issues
- Create a security reviewer agent and compare your own skill with an organizer-provided skill
- Observe how pre-configured environments enable complex automation

> **Note:** This part demonstrates security-focused Copilot workflows using custom agents, reusable skills, and pre-configured environments.

> **New to AI or coding tools?** No previous experience is needed. You can paste the example requests into Copilot Chat, ask it to explain unfamiliar terms, and review its suggestions before applying them. The goal is to experiment and leave with a useful deliverable, not to write everything from scratch.

---

## 🔍 1. Built-in Review Agent & Custom Agents

Let's explore **agents** and **skills**. An agent is a helper configured for a particular task; a skill gives Copilot reusable guidance it can apply while doing that task.

> 💡 **Skills vs. Agents:**
> - **Skills** (`.github/skills/`): Reusable security guidance that Copilot can apply to a task.
> - **Agents** (`.github/agents/`): Helpers configured to follow a workflow, such as reviewing code for security issues.

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

Custom agents are described in files under `.github/agents/`. You can ask Copilot to help create one rather than writing the file yourself.

#### How custom agents work

An agent file includes basic settings, such as its name and tools, followed by instructions that describe its role and workflow. You can ask Copilot to explain or draft either part.

**Try it:**

1. For inspiration, open the existing `.github/agents/todo.agent.md` and notice how it describes the agent's role and steps. You can use its structure without copying its TODO-focused task.
2. In Copilot Chat, type `/create-agent` and ask for a security reviewer for this webshop. For example:
   ```
   /create-agent Create a security reviewer for this webshop. Check authorization, input validation, sensitive data exposure, and dependency risks. Explain your choices as you go.
   ```
3. Review Copilot's draft, ask questions about anything unfamiliar, and save the agent under `.github/agents/`.
4. Ask the agent to review a small set of changes and create a `security-review-report.md` with findings, severity, affected files, and recommended next steps.

### Create and Compare a Helper Skill — `.github/skills/`

First, create and try your own security skill. Then the organizers will provide a pre-written gold-standard skill. Run both skills against the same code and prompt, and compare the results.

**Try it:**

1. In Copilot Chat, type `/create-skill` and describe the security guidance you want Copilot to reuse. For example:
   ```
   /create-skill Create a skill for reviewing this webshop for security issues. Include a short checklist and a clear format for reporting findings. Explain the steps for a beginner.
   ```
2. Review the draft, ask Copilot to explain it, and save your skill under `.github/skills/`.
3. Ask your security reviewer agent to use your skill to produce a `security-review-report.md`.
4. Get the pre-written gold-standard skill from `examples/` and add it as a separate skill. Move your own skill to `.aiignore` in the root folder of this project. 
5. Use the same review prompt and code with the gold-standard skill. Compare the two reports: which findings, explanations, or recommendations changed? You can also ask Copilot to create a small comparison dashboard or summary table.

> 💡 **SDLC role:** The security reviewer acts as a focused **Application Security Engineer**. The report and skill comparison make the agent's work visible and give you something concrete to discuss.

#### Agent Plugins & Extension Marketplaces

Beyond building custom agents and skills in your repository, you can also explore **Agent Plugins** and extension marketplaces. These marketplaces offer downloadable, pre-packaged bundles of agents, skills, tools, and instructions for workflows such as security auditing. Installing a suitable bundle can provide reusable security guidance without authoring every agent or skill from scratch.

---