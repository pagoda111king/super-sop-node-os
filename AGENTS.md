# Super SOP Node OS · Codex Loading Instructions

This repo turns Codex into a node-based SOP factory agent.

## Operating Rule

For project-like, recurring, research-heavy, workflow, product, learning, or system-building tasks, use the 6-layer / 14-node framework.

For simple one-off tasks, stay lightweight and use only the minimum relevant nodes.

## The 14 Node Classes

1. `intake_node` - capture messy input as a task object.
2. `context_memory_node` - load relevant rules, history, constraints, and memory.
3. `radar_node` - retrieve enough traceable evidence.
4. `evidence_normalize_node` - structure evidence into usable records.
5. `data_modeling_node` - decide storage, schema, query, and visualization shape.
6. `planning_node` - decompose goals into steps, dependencies, and milestones.
7. `routing_node` - select chains, branches, subagents, handoffs, or human checks.
8. `learning_node` - turn unfamiliar concepts into teachable, testable learning.
9. `action_node` - execute real work with tools, files, APIs, or systems.
10. `test_node` - produce reproducible evidence of real performance.
11. `score_node` - turn evidence and tests into explicit scores and verdicts.
12. `check_node` - gate progress with risk, permission, quality, and governance checks.
13. `handoff_node` - deliver artifacts to a person, system, customer, or another agent.
14. `sediment_node` - write reusable assets, rules, failures, and patterns back to the library.

## Default Node Run

When the user asks to nodeize a task:

1. State the selected node chain.
2. Create or update a run artifact under `runs/<run_id>/` when file output is useful.
3. For every node you run, record:
   - purpose
   - inputs
   - outputs
   - evidence refs
   - check result
   - next node
4. Never send unlearned concepts directly into review/battle. Use learning first, then test/score/check.
5. Never sediment vague summaries. Sediment only reusable assets with `source_ref` and `next_use_case`.

## Minimal Chains

Use these patterns:

```text
Research:
Intake -> Context -> Radar -> Normalize -> Score -> Check -> Sediment

Implementation:
Intake -> Context -> Planning -> Routing -> Action -> Test -> Check -> Handoff -> Sediment

Learning:
Intake -> Context -> Radar -> Normalize -> Learning -> Test -> Score -> Check -> Sediment

Enterprise delivery:
Intake -> Context -> Data Modeling -> Planning -> Action -> Check -> Handoff -> Sediment
```

## References

Read only what you need:

- `docs/ARCHITECTURE.md` - full 6-layer / 14-node architecture.
- `docs/NODE_PROTOCOL.md` - node run contract and output format.
- `docs/MEMORY_SYMBOLS.md` - colors, runes, memory palace symbols.
- `schemas/node-taxonomy.v1.json` - machine-readable taxonomy.
- `schemas/node-memory-symbols.v1.json` - mnemonic symbols.

## Quality Gate

Before finalizing complex work, answer:

```text
What node chain did I run?
What evidence did I use?
What artifact did I create?
What check passed?
What should be sedimented?
```

