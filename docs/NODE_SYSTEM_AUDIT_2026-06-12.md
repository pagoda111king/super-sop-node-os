# Node System Audit · 2026-06-12

This audit reviews the reference projects one by one and asks:

1. Is the current 6-layer / 14-node system still enough?
2. Should the layer classification change?
3. Should any node class be redesigned?
4. What should become a cross-cutting rail instead of a new node?

## Verdict

The 14 core node classes are still valid.

The better upgrade is:

```text
Keep 14 core nodes.
Refactor the 6 layers.
Add 4 cross-cutting rails.
Add 2 optional compound nodes for production/deployment scenarios.
```

Do not expand the core taxonomy too quickly. If every new framework concept becomes a new node, the system becomes hard to remember and hard to run. The stronger design is:

```text
14 core node types + rails that every node must carry.
```

## Current Evidence Snapshot

Checked on 2026-06-12.

| Project | Current Signal | What It Proves |
|---|---|---|
| OpenAI Agents SDK | `openai/openai-agents-python` v0.17.5, active release 2026-06-11 | Tools, handoffs, guardrails, sessions, tracing, evals are central agent runtime primitives. |
| OpenAI Codex | `openai/codex` rust-v0.139.0, active release 2026-06-09 | Coding agents need project instructions, sandboxing, skills, worktrees, review, automations, and local environment awareness. |
| Microsoft Agent Framework | `microsoft/agent-framework` dotnet-1.10.0, active release 2026-06-10 | Enterprise agent systems are converging on state, telemetry, middleware, type safety, and graph workflows. |
| LangGraph | `langchain-ai/langgraph` active release 2026-06-11 | Durable execution, checkpoints, interrupts, persistence, and human-in-the-loop are now baseline runtime requirements. |
| OpenClaw / ClawHub | `openclaw/openclaw` v2026.6.6 and `openclaw/clawhub` v0.21.0, active 2026-06-12 | Skills, plugins, permission gating, registries, package trust, and moderation are becoming agent distribution infrastructure. |
| OpenMAIC | `THU-MAIC/OpenMAIC` v0.2.2, active 2026-06 | Learning needs multi-agent interaction, quizzes, simulations, slides, and project-based activities. |
| Hermes Agent | `NousResearch/hermes-agent` v2026.6.5 | Persistent agents need memory, searchable history, messaging gateways, and automated skill creation from experience. |
| Coze Studio | `coze-dev/coze-studio` v0.5.1 | Visual workflow agents need node metadata, input/output maps, DAG execution, plugins, knowledge, databases, and memory. |
| Coze Loop | `coze-dev/coze-loop` v1.5.1 | AgentOps needs prompt versioning, evaluation sets, experiments, traces, observation, and monitoring. |
| DeerFlow | `bytedance/deer-flow`, active 2026-06 | Long-horizon agents need subagents, memory, sandboxes, skills, tools, filesystem, and gateways. |
| AgentScope | `agentscope-ai/agentscope` v2.0.1 | Production agent frameworks need event streams, permissions, workspace/sandbox, middleware, multi-session service, tracing, evaluation, and agent teams. |
| Google ADK / A2A | `google/adk-python` v2.2.0 and `a2aproject/A2A` v1.0.1 | Context engineering, artifacts, sessions, memory, and inter-agent task/artifact handoff are core. |

## Project-By-Project Findings

### 1. OpenAI Codex / Agents SDK

Observed architecture primitives:

- `AGENTS.md` as layered project guidance.
- Agent Skills as packaged instructions, resources, and scripts.
- Agents SDK primitives: tools, handoffs, guardrails, sessions, tracing, state, observability, evals.
- Codex product surfaces: sandboxing, worktrees, review, automations, local environments, rules, hooks, plugins, MCP, skills, subagents.

Implication for our node system:

- Context node must load instructions, skills, local rules, and environment constraints.
- Check node must include guardrails, permission checks, and policy gates.
- Handoff node must become more protocol-like, not just a message.
- Trace/Observe should be a cross-cutting rail on every node.

### 2. Anthropic Claude Code / Building Effective Agents

Observed architecture primitives:

- Prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
- Hooks that intercept tool calls, session start/stop, and execution events.
- Plugins that bundle skills, hooks, subagents, and MCP servers.
- Agent evals with code-based, model-based, and human graders.

Implication:

- Planning and Routing should explicitly support chains, branches, parallel runs, and worker delegation.
- Score should not be a casual opinion. It should support grader types.
- Check should be hook-compatible: PreToolUse, PostToolUse, stop, session lifecycle.
- Sediment should generate skills/plugins when a pattern repeats.

### 3. Google ADK / A2A

Observed architecture primitives:

- Context is managed like source code: sessions, memory, tool outputs, artifacts, summaries, token budgets.
- Artifacts are explicit data objects.
- A2A focuses on agent discovery, secure communication, task state, messages, and artifacts.

Implication:

- Context node should include token budget, pruning policy, and lazy artifact loading.
- Data Modeling node should manage artifact schemas and storage, not only databases.
- Handoff node must include task state, artifacts, expected next action, and receiver contract.

### 4. Microsoft Agent Framework / Magentic-One

Observed architecture primitives:

- Session state, type safety, middleware, filters, telemetry, graph workflows.
- Orchestrator-workers: plan, delegate, track progress, re-plan after errors.
- Enterprise deployment and observability.

Implication:

- Planning node should maintain a live plan state, not a static list.
- Routing node should include orchestrator-worker delegation and re-planning rules.
- Data Modeling should include typed state.
- Check should read telemetry before allowing delivery.

### 5. LangGraph

Observed architecture primitives:

- Durable execution, streaming, human-in-the-loop, persistence.
- Checkpointers and stores for short-term and long-term memory.
- Interrupts that pause execution and resume later with state.

Implication:

- Node runs should be resumable.
- Every node should have state status: `pending | running | blocked | passed | returned | killed`.
- Check node should support interrupt/resume.
- Sediment should separate short-term checkpoint from long-term memory.

### 6. OpenClaw / ClawHub

Observed architecture primitives:

- Skills are folders with `SKILL.md` and metadata.
- Skills load based on environment, config, binaries, allowlists, and gating.
- ClawHub adds publishing, versioning, moderation, search, and install/update flows.
- Plugins extend channels, model providers, tools, skills, speech, realtime, memory, and web/search capabilities.

Implication:

- Sediment node should produce skill-like reusable packages.
- Check node must include trust and provenance review.
- Context node should know which skills are available and which are gated off.
- Publish/handoff workflows need version and moderation status.

### 7. OpenMAIC

Observed architecture primitives:

- Topic/document to interactive classroom.
- Multi-agent teacher, teaching assistant, classmates.
- Slides, quizzes, simulations, project-based learning, whiteboard, voice.

Implication:

- Learning node should become interactive, not only explanatory.
- Test node should include quizzes and transfer tasks.
- Score node should evaluate understanding and application.
- Sediment node should write learning cards, battle cards, and lesson templates.

### 8. Hermes Agent

Observed architecture primitives:

- Persistent always-on agent.
- Memory and searchable past conversations.
- Automated skill creation from experience.
- Messaging gateway and cross-platform continuation.

Implication:

- Sediment node is not an archive; it is skill/rule creation.
- Context node should retrieve past conversations and user/project preferences.
- Handoff node should support channel continuation.

### 9. Feishu / Aily

Observed architecture primitives:

- Enterprise AI embedded in work surfaces: IM, docs, Base, approval, tasks.
- AI Agent workflow nodes.
- AI-assisted business system creation in Base.
- Agent integration through official open tools and MCP/OpenClaw-related surfaces.

Implication:

- Data Modeling node must cover Base/database schema and business system tables.
- Handoff node should target real enterprise surfaces.
- Check node must include permission, identity, approval, and data access.

### 10. Coze Studio / Coze Loop

Observed architecture primitives:

- Visual canvas workflow nodes.
- DAG execution with control flow and data flow.
- Node type metadata, input/output maps, `Invoke(ctx, input) -> output`.
- Resources: workflows, plugins, databases, knowledge bases, prompts, variables.
- Loop: prompt debugging, evaluation sets, evaluators, experiments, trace observation.

Implication:

- Our node contract should be closer to an executable node spec.
- Every node needs typed input/output shape.
- Test/Score/Check should consume trace data.
- Data Modeling should know resources, variables, knowledge base, and DB shape.

### 11. DeerFlow

Observed architecture primitives:

- Long-horizon super-agent harness.
- Subagents, memory, sandboxes, tools, skills, filesystem, gateways.
- Tasks lasting minutes to hours.

Implication:

- Routing should support long-horizon delegation and subagent teams.
- Action node should explicitly declare sandbox, filesystem scope, command permissions, and rollback.
- Context/Sediment should maintain task memory across long runs.

### 12. AgentScope

Observed architecture primitives:

- Event bus to frontend and human-in-the-loop.
- Permission system.
- Multi-tenancy and multi-session service.
- Workspace/sandbox support.
- Extensible middleware.
- Tracing, evaluation, memory, long-term memory, routing, handoffs, A2A, realtime agents, agent teams.

Implication:

- Trace/Observe must be a rail, not an afterthought.
- Policy/Permission must be a rail.
- Workspace isolation belongs in Context and Action.
- Handoff and Routing should support teams and A2A.

## Is 6 Layers Still Right?

Yes, but the layer naming and node placement should be improved.

The current 6-layer model is memorable, but two things are slightly awkward:

1. The Cognition & Orchestration layer is too large.
2. Handoff currently sits inside the Sediment layer, but handoff is more like delivery/interoperability.

## Recommended 6-Layer v1.1

Keep 6 layers, but rebalance them:

| Layer | New Name | Nodes | Why Better |
|---|---|---|---|
| L1 | Signal & Intent | Intake | Captures messy demand and true objective. |
| L2 | Context, Memory & Workspace | Context / Memory | Adds session pruning, memory, skills, sandbox/workspace setup. |
| L3 | Evidence & Data | Radar, Evidence Normalize, Data Modeling | Separates evidence/data work from planning. |
| L4 | Orchestration & Learning | Planning, Routing, Learning | Combines plan, branch, delegation, and concept learning. |
| L5 | Execution & Assurance | Action, Test, Score, Check | Keeps doing, proving, judging, and gating close together. |
| L6 | Delivery & Evolution | Handoff, Sediment | Separates delivery and reusable evolution from raw validation. |

This version still preserves the public memory hook:

```text
6 layers, 14 nodes
```

But it is easier to explain professionally:

```text
signal -> context -> evidence/data -> orchestration -> execution/assurance -> delivery/evolution
```

## Is Anything Missing?

One thing is truly missing if we stay strict:

```text
Observe / Trace / Monitor
```

But it should not immediately become the 15th core node. It appears in every serious framework as a cross-cutting capability:

- OpenAI tracing and observability
- Coze Loop observation
- LangSmith/LangGraph traces
- AgentScope Studio/tracing
- Microsoft telemetry
- Anthropic eval transcripts

Recommended decision:

```text
Do not add a 15th core node yet.
Add Observe/Trace as a required rail across every node.
```

For deployed products, use an optional compound node:

```text
Monitor/Ops = Trace + Test + Score + Check + Sediment
```

## Four Cross-Cutting Rails

### Rail 1: Observe / Trace

Every node should record:

- `trace_id`
- `span_id`
- `tool_calls`
- `token_cost`
- `latency`
- `failure_events`
- `artifact_events`

### Rail 2: Policy / Permission

Every node should know:

- allowed tools
- identity / account used
- secret or credential boundary
- sandbox/workspace boundary
- approval requirement
- rollback path

### Rail 3: Artifact Registry

Every durable output should have:

- `artifact_id`
- `artifact_type`
- `schema`
- `version`
- `owner`
- `source_refs`
- `validation_status`

### Rail 4: Human / Team

Every high-impact node should identify:

- reviewer
- approval gate
- escalation path
- handoff target
- decision owner

## Optional Compound Nodes

These should not be part of the base 14, but they should be recognized patterns:

| Compound Node | Composed From | Use When |
|---|---|---|
| Deploy / Publish | Action + Check + Handoff | Publishing GitHub, ClawHub, app store, production releases. |
| Monitor / Ops | Trace + Test + Score + Check + Sediment | Tracking production behavior, regressions, cost, user feedback, failures. |

## Per-Node Redesign Suggestions

| Node | Keep? | Upgrade |
|---|---|---|
| Intake | Yes | Add `intent`, `stakes`, `deadline`, `source_channel`, `verbatim_snapshot`, and ambiguity list. |
| Context / Memory | Yes | Add skill loading, session pruning, workspace isolation, token budget, memory search, and policy context. |
| Radar | Yes | Add source freshness, breadth target, confidence level, contradiction capture, and source quality score. |
| Evidence Normalize | Yes | Add conflict resolution, schema mapping, pattern extraction, and reusable record format. |
| Data Modeling | Yes | Expand from database schema to artifact registry, Base tables, variable stores, eval datasets, and trace stores. |
| Planning | Yes | Make plans live and revisable; include dependencies, stop conditions, and checkpoint points. |
| Routing | Yes | Add branch routing, parallel routing, subagent/team routing, A2A handoff routing, and human review routing. |
| Learning | Yes | Upgrade to interactive lesson: explain, example, debate, quiz, simulation, project transfer. |
| Action | Yes | Add sandbox scope, filesystem scope, command permissions, rollback path, and evidence capture. |
| Test | Yes | Add deterministic tests, screenshots, traces, eval datasets, and golden cases. |
| Score | Yes | Add grader type: code-based, model-based, human, business, risk, repeatability. |
| Check | Yes | Add policy gate, permission gate, regression gate, safety gate, artifact gate, and publish gate. |
| Handoff | Yes | Add receiver, artifact bundle, state summary, next action, protocol, and acceptance criteria. |
| Sediment | Yes | Upgrade to skill/rule/eval-case creation with source_ref, next_use_case, owner, and expiry/review date. |

## Proposed Node Envelope v1.1

Every node output should eventually support:

```yaml
run_id:
node_id:
node_type:
layer:
status: pending | running | passed | fix | return | blocked | killed
purpose:
inputs:
outputs:
artifact_ids:
evidence_refs:
trace:
  trace_id:
  span_id:
  tool_calls:
  failures:
policy:
  workspace:
  allowed_tools:
  approval_required:
  rollback:
check:
  result:
  criteria:
  reviewer:
next:
  next_node:
  handoff_target:
sediment:
  candidate: true | false
  source_ref:
  next_use_case:
```

## Final Recommendation

Move to:

```text
Super SOP Node OS v1.1
= 6 rebased layers
+ 14 core nodes
+ 4 cross-cutting rails
+ 2 optional compound nodes
```

This keeps the system memorable while making it closer to real production agent architecture.

## Primary Sources Checked

- OpenAI Agents SDK: https://developers.openai.com/api/docs/guides/agents
- OpenAI Codex AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- OpenAI Codex Skills: https://developers.openai.com/codex/skills
- Anthropic Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- Anthropic Agent Evals: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Claude Code Hooks: https://code.claude.com/docs/en/agent-sdk/hooks
- Google ADK: https://adk.dev/
- Google A2A: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- Microsoft Agent Framework: https://learn.microsoft.com/en-us/agent-framework/overview/
- Microsoft Magentic-One: https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/
- LangGraph Overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph Persistence: https://docs.langchain.com/oss/python/langgraph/persistence
- OpenClaw Skills: https://docs.openclaw.ai/tools/skills
- ClawHub Skill Format: https://docs.openclaw.ai/clawhub/skill-format
- OpenMAIC: https://github.com/THU-MAIC/OpenMAIC
- Hermes Agent: https://hermes-agent.nousresearch.com/docs/
- Feishu Aily: https://www.feishu.cn/hc/en-US/articles/790732948604-get-started-with-feishu-aily
- Coze Studio: https://github.com/coze-dev/coze-studio
- Coze Loop: https://github.com/coze-dev/coze-loop
- DeerFlow: https://github.com/bytedance/deer-flow
- AgentScope: https://doc.agentscope.io/
