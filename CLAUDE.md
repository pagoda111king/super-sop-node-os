# Super SOP Node OS · Claude Code Loading Instructions

Use this repository as a node-based work protocol.

## First Behavior

When a task is complex, recurring, research-heavy, project-like, product-like, learning-oriented, or workflow-related, do not answer as a single block. Convert it into a node run.

For small one-off tasks, keep it lightweight.

## Core Mental Model

```text
6 layers:
Input -> Context -> Cognition/Orchestration -> Action -> Validation/Governance -> Sediment

14 node classes:
Intake, Context, Radar, Normalize, Data, Planning, Routing, Learning, Action, Test, Score, Check, Handoff, Sediment
```

## How To Work

1. Choose the smallest useful node chain.
2. If durable output matters, create `runs/<run_id>/`.
3. Write node outputs as files instead of keeping everything in chat.
4. Use structured artifacts when possible.
5. Always run a Check before delivery.
6. Sediment only reusable assets, not vague reflections.

## Node Output Template

```markdown
# <Node Name>

## Purpose

## Inputs

## Work

## Outputs

## Check

## Next
```

## Important Constraints

- `Radar` must produce traceable sources.
- `Normalize` must turn messy evidence into structured records.
- `Data Modeling` decides where facts live.
- `Test` verifies real behavior.
- `Score` explains whether to adopt, revise, monitor, or reject.
- `Check` gates progress.
- `Sediment` requires `source_ref` and `next_use_case`.

## Read Next

- `docs/ARCHITECTURE.md`
- `docs/NODE_PROTOCOL.md`
- `docs/MEMORY_SYMBOLS.md`

