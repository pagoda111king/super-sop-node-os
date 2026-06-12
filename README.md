# Super SOP Node OS · Node Era Protocol

Turn complex agent work into a reusable 6-layer, 14-node operating system for Codex, Claude Code, OpenClaw, and other coding agents.

> Chinese name: 超级 SOP 工厂节点系统

Super SOP Node OS is not a static checklist. It is a portable work protocol that makes an AI agent choose a node chain, produce node artifacts, verify the result, and sediment reusable knowledge back into the project.

```text
Super SOP Node OS = 6 layers + 14 node classes + run artifacts + Test/Score/Check/Sediment loop
```

## From Chat Era To Node Era

The first era of modern AI was the large-model conversation era: humans asked, models answered, and intelligence mostly lived inside a chat box.

The next era was the agent era: models started using tools, editing files, calling APIs, browsing, coding, and acting across real environments.

Then came OpenClaw, Hermes-style always-on agents, and other personal or enterprise agent systems: AI became less like a single answer and more like a persistent operator that can hold context, coordinate tools, and keep working.

The next unavoidable step is the node era.

In the node era, everything valuable in AI work should be rebuilt as nodes: search nodes, evidence nodes, data nodes, planning nodes, action nodes, test nodes, score nodes, check nodes, handoff nodes, and sediment nodes. A node is stronger than a prompt because it has a stable role, inputs, outputs, checks, memory, and a way to compose with other nodes.

This is the direction Super SOP Node OS takes: not "one more agent prompt", but a node-based operating system for repeatable AI work.

## Why This Exists

Most agent workflows fail in the same places:

- The agent starts acting before it understands the task.
- Research is not traceable.
- Evidence is not normalized into reusable data.
- Outputs are delivered without real checks.
- Lessons are lost after the chat ends.

Super SOP Node OS solves this by turning work into explicit nodes. Each node has a purpose, inputs, outputs, checks, and a next step.

## Core Flow

```text
Intake
-> Context / Memory
-> Radar
-> Evidence Normalize
-> Data Modeling
-> Planning
-> Routing
-> Learning
-> Action
-> Test
-> Score
-> Check
-> Handoff
-> Sediment
```

You do not need to run all 14 nodes every time. The agent chooses the smallest useful chain.

## The 6 Layers

| Layer | Role | Nodes |
|---|---|---|
| Input Capture | Convert messy signals into a task object | Intake |
| Context & Memory | Load rules, history, constraints, and reusable knowledge | Context / Memory |
| Cognition & Orchestration | Search, normalize, model, plan, route, and teach | Radar, Normalize, Data Modeling, Planning, Routing, Learning |
| Action | Make real changes through tools, files, APIs, or systems | Action |
| Validation & Governance | Prove, score, and gate the work | Test, Score, Check |
| Sediment Assets | Deliver and write back reusable assets | Handoff, Sediment |

## The 14 Node Classes

| Node | Purpose | Typical Output |
|---|---|---|
| Intake | Capture the true task from messy input | task object |
| Context / Memory | Load project rules, prior runs, constraints, and memory | context pack |
| Radar | Search for enough traceable evidence | source list / evidence set |
| Evidence Normalize | Convert messy evidence into structured records | pattern cards / JSON records |
| Data Modeling | Decide where facts live and how they can be queried | schema / storage plan |
| Planning | Turn the goal into steps, dependencies, and milestones | plan |
| Routing | Select the right chain, branch, subagent, or human handoff | route decision |
| Learning | Turn unfamiliar concepts into teachable, testable lessons | lesson / note / drills |
| Action | Execute real work with tools | code, document, UI, data, automation |
| Test | Produce reproducible evidence of behavior | test output / screenshot / benchmark |
| Score | Convert evidence into a verdict | scorecard |
| Check | Gate quality, risk, permissions, and delivery readiness | pass / fix / return |
| Handoff | Package the result for a person, system, or next agent | delivery note |
| Sediment | Store reusable assets, rules, failures, and patterns | reusable rule / SOP / memory |

## Common Node Chains

### Research

```text
Intake -> Context -> Radar -> Normalize -> Score -> Check -> Sediment
```

Use this when the agent needs to compare frameworks, collect market evidence, study a codebase, or evaluate a technical direction.

### Implementation

```text
Intake -> Context -> Planning -> Routing -> Action -> Test -> Check -> Handoff -> Sediment
```

Use this for product features, code changes, app prototypes, automation, and delivery work.

### Learning

```text
Intake -> Context -> Radar -> Normalize -> Learning -> Test -> Score -> Check -> Sediment
```

Use this when a concept must be learned before review, quizzing, knowledge battle, or customer explanation.

### Enterprise Delivery

```text
Intake -> Context -> Data Modeling -> Planning -> Action -> Check -> Handoff -> Sediment
```

Use this for customer-facing SOPs, internal operations, sales/service workflows, and reusable business systems.

## Quick Start

Clone or copy this repository into a project:

```bash
git clone https://github.com/pagoda111king/super-sop-node-os.git
cd super-sop-node-os
```

Generate a node run:

```bash
python3 scripts/create_node_run.py --goal "Build a reusable customer delivery SOP" --type implementation
```

Available run types:

```text
research | implementation | learning | enterprise | full
```

The script creates a `runs/<run_id>/` folder with one markdown file per selected node.

## Use With Codex

Open this repository, or copy these files into another repository:

```text
AGENTS.md
docs/
schemas/
prompts/
scripts/
```

Codex reads `AGENTS.md` and can then respond to prompts such as:

```text
Use Super SOP Node OS to run this task.
Nodeize this project and start with Intake, Radar, Normalize, and Check.
Create a reusable node run for this implementation.
```

## Use With Claude Code

Claude Code reads:

```text
CLAUDE.md
```

The repository also includes a Claude command template:

```text
.claude/commands/nodeize.md
```

Use prompts like:

```text
Run /nodeize on this feature request.
Turn this repo into a node-based execution plan.
```

## Use As A Codex Skill

The installable skill lives at:

```text
codex-skill/super-sop-node-os
```

Copy install:

```bash
mkdir -p ~/.codex/skills
cp -R codex-skill/super-sop-node-os ~/.codex/skills/
```

Symlink install, useful during development:

```bash
mkdir -p ~/.codex/skills
ln -s "$PWD/codex-skill/super-sop-node-os" ~/.codex/skills/super-sop-node-os
```

Trigger examples:

```text
Nodeize this task with Super SOP Node OS.
Design Radar / Normalize / Check / Sediment nodes for this project.
Turn this concept into a learn-test-score-sediment workflow.
```

## Publish To ClawHub

ClawHub publishes text-based agent skills from folders that contain `SKILL.md`.

The skill folder is:

```text
codex-skill/super-sop-node-os
```

Publish command:

```bash
clawhub publish /absolute/path/to/super-sop-node-os/codex-skill/super-sop-node-os \
  --slug super-sop-node-os \
  --name "Super SOP Node OS: Node Era Protocol" \
  --version 1.0.2 \
  --changelog "Add architecture reference radar and company pattern mapping." \
  --tags latest,agent-workflow,sop,codex,claude-code,openclaw
```

See `CLAWHUB_LISTING.md` for the marketplace copy.

The initial ClawHub publish receipt is recorded in `PUBLISH_RECEIPT.md`.

## Repository Layout

```text
.
├── AGENTS.md
├── CLAUDE.md
├── CLAWHUB_LISTING.md
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── NODE_PROTOCOL.md
│   ├── MEMORY_SYMBOLS.md
│   ├── COMPANY_REFERENCES.md
│   └── ROADMAP.md
├── schemas/
│   ├── node-taxonomy.v1.json
│   ├── node-taxonomy.v1.1-proposal.json
│   ├── node-visual-system.v1.json
│   └── node-memory-symbols.v1.json
├── visuals/
│   └── super_sop_factory_14_nodes_animated.html
├── examples/
│   ├── node-run-template.md
│   └── learning-run-example.md
├── prompts/
│   ├── nodeize-task.md
│   └── node-review.md
├── scripts/
│   └── create_node_run.py
└── codex-skill/
    └── super-sop-node-os/
        ├── SKILL.md
        ├── references/
        └── scripts/
```

## Visual Memory System

The project includes a color and symbol system for the 14 nodes:

```text
visuals/super_sop_factory_14_nodes_animated.html
```

The visual system is designed as a memory palace: each node has a rune, color, metaphor, and motion pattern so the workflow is easier to recall under pressure.

## Design Influences

This project synthesizes practical ideas from:

- OpenAI Codex and Agents SDK: project instructions, tools, guardrails, tracing, handoffs.
- Anthropic Claude Code and Building Effective Agents: workflows, subagents, hooks, evaluator-optimizer loops.
- Google ADK and A2A: enterprise agent development and agent-to-agent communication.
- Microsoft Agent Framework and Magentic-One: orchestrator patterns, telemetry, state, replanning.
- LangGraph: durable graph execution, persistence, human-in-the-loop.
- OpenClaw / ClawHub: portable text-based skills and skill registries.
- OpenMAIC: concept learning before review or knowledge battle.
- Hermes Agent, Feishu/Aily, Coze Studio/Loop, DeerFlow, and AgentScope: persistent memory, enterprise work surfaces, visual workflow nodes, sandboxed long-horizon execution, and production agent lifecycle.

The goal is not to copy any one framework. The goal is to make their best patterns operational for repeatable real work.

The latest tracked architecture radar is in `docs/REFERENCE_RADAR_2026-06-12.md`.

The latest system audit is in `docs/NODE_SYSTEM_AUDIT_2026-06-12.md`. Its current recommendation is:

```text
6 rebased layers + 14 core nodes + 4 cross-cutting rails + 2 optional compound nodes
```

## Safety And Quality Rules

- Radar must provide traceable sources.
- Normalize must turn evidence into structured records.
- Test must verify real behavior when a claim is testable.
- Score must explain the adoption verdict.
- Check must run before delivery.
- Sediment must include `source_ref` and `next_use_case`.
- No vague summary should be stored as a reusable rule.

## Status

Current release: `1.0.3`

This is an early public package. The core protocol, loader files, skill package, schemas, and scaffold script are ready. Future work will add richer adapters, a visual run dashboard, and more automated evaluation.

## License

MIT
