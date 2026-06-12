# Super SOP Node OS · Claude Code Hard Rules

This is Claude Code's compressed long-term memory for this repo.

If a task is complex, do not answer as one block. Run the smallest useful node chain.

## Core Memory

```text
6 layers
14 core nodes
4 rails
17 SOP steps as lifecycle
```

```text
17 steps = project lifecycle
14 nodes = reusable execution parts
```

Core nodes:

```text
Intake, Context/Memory, Radar, Evidence Normalize, Data Modeling,
Planning, Routing, Learning, Action, Test, Score, Check, Handoff, Sediment
```

Rails:

```text
Observe/Trace, Policy/Permission, Artifact Registry, Human/Team
```

## When To Nodeize

Use node mode for project-like, recurring, research-heavy, workflow, product, learning, system-building, database, dashboard, visualization, or reusable-knowledge work.

For small one-off tasks, stay lightweight.

## Required Start

For complex work, start with:

```text
Selected node chain:
Why this chain:
First concrete action:
```

Never run all 14 nodes for show. Choose the smallest useful chain.

## Node Exit Ticket

Every executed node must leave:

```text
Purpose:
Input:
Work:
Output:
Evidence:
Check:
Next:
```

A node is not done without output, evidence, Check, next step, and human-visible status.

Short form:

```text
done = output + evidence + check + next + visible state
```

Allowed Check results:

```text
pass | fix | return | escalate | kill | accept_risk
```

Allowed Score verdicts:

```text
adopt | revise | monitor | reject
```

## Default Chains

```text
Research: Intake -> Context -> Radar -> Normalize -> Score -> Check -> Sediment
Implementation: Intake -> Context -> Planning -> Routing -> Action -> Test -> Check -> Handoff -> Sediment
Learning: Intake -> Context -> Radar -> Normalize -> Learning -> Test -> Score -> Check -> Sediment
SOP/Enterprise: Intake -> Context -> Data Modeling -> Planning -> Action -> Check -> Handoff -> Sediment
```

## Database And Visibility

For SOP Factory runs:

```text
Notion = human-auditable main database
local sqlite / vfs.db = truth backup and automation fallback
Feishu Base = future Chinese enterprise customer work surface
```

Every real run should be visible through:

```text
SOP Runs
SOP Step Ledger
17 step rows
node chain
status
evidence
artifact
check result
next step
sediment candidate
```

If humans cannot see progress and node state, the system is not operational enough.

## Hard Bans

- Do not create new process files just to look complete.
- Do not claim tests, database writes, or file changes without evidence.
- Do not deliver complex work without Check.
- Do not sediment vague summaries.
- Do not send unlearned concepts into review, battle, or permanent memory.

Sediment requires:

```text
source_ref + next_use_case + check_status + owner/downstream user
```

## Final Gate

Before finalizing complex work, answer:

```text
Which chain ran?
Which nodes actually executed?
What changed?
What evidence supports it?
What Check passed or failed?
What should be sedimented?
What should not be sedimented?
```

If these cannot be answered, the work is not complete.

## Read Only What Is Needed

- `README.zh-CN.md`
- `docs/ARCHITECTURE.md`
- `docs/NODE_PROTOCOL.md`
- `docs/NODE_SYSTEM_AUDIT_2026-06-12.md`
- `docs/MEMORY_SYMBOLS.md`
