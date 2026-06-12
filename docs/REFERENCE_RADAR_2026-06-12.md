# Reference Radar · 2026-06-12

This radar tracks current public architecture lessons from major agent frameworks and maps them into the Super SOP Node OS.

The goal is not to copy framework names. The goal is to extract reusable node design experience: stable contracts, durable artifacts, checks, routing, learning loops, and sediment.

## Executive Confirmation

The current agent ecosystem is converging around the same architecture direction:

```text
chat answer -> tool-using agent -> persistent agent system -> node-based operating system
```

Across OpenAI, Anthropic, Google, Microsoft, LangGraph, OpenClaw, OpenMAIC, Hermes, Feishu, Coze, DeerFlow, and AgentScope, the repeated engineering primitives are:

- project instructions and skill packages
- context/session/memory management
- tool calling with permission boundaries
- orchestration, routing, handoffs, and subagents
- artifacts as durable outputs
- evaluation, tracing, scorecards, and regression checks
- sandboxes and isolation
- human-in-the-loop gates
- learning loops that turn experience into reusable skills or rules

This confirms the 6-layer / 14-node design. The node era is not just a metaphor; it is the engineering shape emerging underneath modern agent products.

## Source Radar

| Source | Current Architecture Lessons | Node Mapping | What We Should Absorb |
|---|---|---|---|
| OpenAI Codex / Agents SDK | Codex uses `AGENTS.md` for layered project guidance; Agent Skills package instructions, resources, and scripts; Agents SDK emphasizes tools, handoffs, guardrails, sessions, and tracing. | Context, Routing, Action, Check, Handoff, Sediment | Keep `AGENTS.md` as the root loader. Treat skills as sedimented node packs. Make tracing/checks first-class. |
| Anthropic Claude Code / Building Effective Agents | Effective agents are built from prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer loops. Claude Code exposes hooks, plugins, skills, subagents, MCP, and evaluation practice. | Planning, Routing, Action, Test, Score, Check | Keep workflows modular. Separate generation from evaluation. Use hooks as Check/Policy nodes. |
| Google ADK / A2A | ADK treats context like source code: sessions, memory, tool outputs, artifacts, summarization, token control. A2A standardizes inter-agent task exchange, artifacts, and enterprise interoperability. | Context, Data Modeling, Routing, Handoff, Sediment | Make task/artifact contracts explicit. Add artifact IDs and handoff payloads to node outputs. |
| Microsoft Agent Framework / Magentic-One | Agent Framework 1.0 combines AutoGen abstractions with Semantic Kernel enterprise features: session state, type safety, middleware, telemetry, graph workflows. Magentic-One uses an orchestrator to plan, delegate, track, and re-plan. | Planning, Routing, Data Modeling, Test, Score, Check | Strengthen orchestrator-worker patterns. Treat telemetry and state as required in complex runs. |
| LangGraph | LangGraph emphasizes durable execution, persistence, streaming, human-in-the-loop, interrupts, checkpointing, and stores for short/long-term memory. | Data Modeling, Routing, Action, Check, Sediment | Node runs should be resumable. Checkpoints and interrupts should be part of long-running node execution. |
| OpenClaw / ClawHub | Skills are folders with `SKILL.md` and metadata; loading is gated by environment, config, binaries, and allowlists. ClawHub adds versioned publishing, moderation, and skill registry workflows. | Context, Routing, Check, Sediment | Keep each reusable workflow as a skill-like folder. Include dependency metadata, versioning, and safety review. |
| OpenMAIC | Turns topics/documents into multi-agent classrooms with teachers, classmates, slides, quizzes, simulations, project-based learning, and real-time discussion. | Learning, Test, Score, Sediment | Learning node should not be a summary. It should produce lessons, interaction, quizzes, and transfer tasks. |
| Hermes Agent | Persistent always-on agent with memory, automated skill creation, self-improving loop, messaging gateways, and searchable past conversations. | Context, Learning, Score, Sediment | Sediment node should create reusable skills/rules from experience, not only write a recap. |
| Feishu / Aily | Enterprise AI lives inside work surfaces: IM, docs, Base, approvals, workflows, tasks. Feishu adds AI Agent nodes in workflows, AI-generated business systems in Base, and agent integration through open tools. | Data Modeling, Action, Handoff, Check | Database/Base nodes matter. Enterprise handoff must target real work surfaces and permission models. |
| Coze Studio / Coze Loop | Coze Studio uses visual workflow nodes, DAG control/data flow, plugins, knowledge bases, databases, prompts, and memory. Coze Loop covers prompt development, debugging, evaluation, observation, and trace data. | Data Modeling, Planning, Action, Test, Score, Check | Our node contracts should be visualizable and executable. Traces should feed Score and Rule Learning. |
| DeerFlow | Long-horizon super-agent harness with subagents, memory, sandboxes, skills, tools, filesystem, and multi-hour task execution. DeerFlow 2.0 is a rewrite focused on super-agent runtime infrastructure. | Radar, Planning, Routing, Action, Check, Sediment | Long tasks require sandbox, filesystem, memory, and subagent decomposition. Radar should support deep exploration. |
| AgentScope | AgentScope 2.0 emphasizes event bus, permissions, multi-tenancy, sessions, workspace/sandbox support, middleware, tracing, evaluation, memory, handoffs, A2A, and agent teams. | Context, Routing, Action, Test, Score, Check, Handoff | Production node systems need event streams, permission systems, workspace isolation, and trace/eval integration. |

## Design Lessons For Our 14 Nodes

### 1. Loader Files Are Context Nodes

`AGENTS.md`, `CLAUDE.md`, `SKILL.md`, and ClawHub skills are not documentation only. They are Context / Memory nodes that shape all later behavior.

Upgrade implication:

```text
Context node = project rules + skill loading + available tools + safety boundaries + prior sediment
```

### 2. Artifacts Are First-Class

Google ADK/A2A, LangGraph, Coze, and Microsoft all converge on durable artifacts, not chat-only output.

Upgrade implication:

```text
Every non-trivial node output should have artifact_id, owner, source_ref, validation_status, and next_use_case.
```

### 3. Check Is Not The Same As Test

Testing verifies behavior. Check gates risk, permissions, compliance, quality, and handoff readiness.

Upgrade implication:

```text
Test node = evidence.
Score node = verdict.
Check node = permission to continue.
```

### 4. Evaluation Is A Loop, Not A Report

Anthropic evaluator-optimizer, Coze Loop, LangSmith/LangGraph, OpenAI tracing, and AgentScope evaluation all point to the same pattern: observe, score, revise, retest, and block regressions.

Upgrade implication:

```text
Score node should write failure patterns into Sediment as new rules or eval cases.
```

### 5. Handoff Needs Protocol, Not Just Message

A2A, Microsoft Agent Framework, Feishu workflows, and OpenClaw plugins all show that handoff must include state, artifacts, permissions, and target runtime.

Upgrade implication:

```text
Handoff node = target + artifact bundle + state summary + permission/risk note + expected next action.
```

### 6. Learning Nodes Must Be Interactive

OpenMAIC confirms that concept learning should generate lessons, quizzes, simulations, role interaction, and project tasks before knowledge-battle review.

Upgrade implication:

```text
Learning node = explain + interact + quiz + project transfer + score.
```

### 7. Sediment Is Skill Creation

Hermes, OpenClaw Skills, Codex Skills, and ClawHub all support the idea that useful experience should become reusable skill/rule packages.

Upgrade implication:

```text
Sediment node should create durable assets: skill, SOP, eval case, pattern card, prompt, schema, or adapter.
```

### 8. Long-Horizon Work Requires Isolation

DeerFlow, AgentScope, Anthropic containment, and OpenClaw security issues all point to sandboxing and permission boundaries.

Upgrade implication:

```text
Action node should declare workspace, sandbox, permissions, rollback plan, and blast radius.
```

## Confirmed P0 Node Upgrades

| P0 Node | Confirmed Upgrade |
|---|---|
| Radar | Add source quality, breadth target, freshness, and trace refs. |
| Evidence Normalize | Normalize into pattern cards, schema records, and conflict notes. |
| Data Modeling | Treat database/Base/artifact storage as a node, not a side effect. |
| Test | Add reproducible command/screenshot/trace/eval dataset evidence. |
| Score | Score adoption, reliability, business value, risk, and repeatability. |
| Check | Add permission, safety, regression, handoff, and publication gates. |
| Rule Learning | Convert repeated failures and successful fixes into rules/eval cases. |
| Sediment | Package reusable knowledge as skills, SOPs, schemas, prompts, adapters, or visual memory assets. |

## Primary Source Links

- OpenAI Agents SDK: https://developers.openai.com/api/docs/guides/agents
- OpenAI Codex AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- OpenAI Codex Skills: https://developers.openai.com/codex/skills
- OpenAI Agents Python SDK: https://openai.github.io/openai-agents-python/agents/
- Anthropic Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- Anthropic agent evals: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Claude Code Hooks: https://code.claude.com/docs/en/agent-sdk/hooks
- Claude Code extensions/plugins: https://code.claude.com/docs/en/features-overview
- Google ADK: https://adk.dev/
- Google ADK artifacts: https://adk.dev/artifacts/
- Google A2A announcement: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- Microsoft Agent Framework overview: https://learn.microsoft.com/en-us/agent-framework/overview/
- Microsoft Agent Framework 1.0: https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/
- Microsoft Magentic-One: https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/
- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph persistence: https://docs.langchain.com/oss/python/langgraph/persistence
- LangGraph interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts
- OpenClaw skills: https://docs.openclaw.ai/tools/skills
- OpenClaw plugins: https://docs.openclaw.ai/tools/plugin
- ClawHub: https://docs.openclaw.ai/clawhub
- ClawHub skill format: https://docs.openclaw.ai/clawhub/skill-format
- OpenMAIC GitHub: https://github.com/THU-MAIC/OpenMAIC
- OpenMAIC website: https://openmaic.chat/
- Hermes Agent docs: https://hermes-agent.nousresearch.com/docs/
- Hermes Agent architecture: https://hermes-agent.nousresearch.com/docs/developer-guide/architecture
- Hermes Agent GitHub: https://github.com/nousresearch/hermes-agent
- Feishu Aily: https://www.feishu.cn/hc/en-US/articles/790732948604-get-started-with-feishu-aily
- Feishu AI Agent workflow node: https://www.feishu.cn/hc/en-US/articles/643175485940-use-the-ai-agent-node-in-workflow
- Feishu Base AI systems: https://www.feishu.cn/hc/en-US/articles/882125125335-use-ai-to-build-business-systems-in-base
- Feishu agent integration: https://open.feishu.cn/document/mcp_open_tools/integrating-agents-with-feishu/overview
- Coze Studio GitHub: https://github.com/coze-dev/coze-studio
- Coze Studio workflow docs: https://www.coze.com/open/docs/guides/workflow
- Coze custom workflow nodes: https://github.com/coze-dev/coze-studio/wiki/11.-Add-new-workflow-node-types-%28backend%29
- Coze Loop GitHub: https://github.com/coze-dev/coze-loop
- Coze Loop overview: https://github.com/coze-dev/coze-loop/wiki/1.-what-is-coze-loop
- DeerFlow GitHub: https://github.com/bytedance/deer-flow
- DeerFlow website: https://deerflow.tech/
- AgentScope docs: https://doc.agentscope.io/
- AgentScope website: https://agentscope.io/
- AgentScope GitHub: https://github.com/agentscope-ai/agentscope
- AgentScope paper: https://arxiv.org/html/2508.16279v1

## Radar Status

```text
status: confirmed
date: 2026-06-12
confidence: high for architecture direction; medium for product-specific implementation details that may change quickly
next_refresh: monthly or before major release
```
