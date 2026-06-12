---
name: super-sop-node-os
description: Nodeize complex agent work into a 6-layer, 14-node SOP system with Radar, Normalize, Test, Score, Check, Handoff, and Sediment loops.
version: 1.0.0
metadata:
  openclaw:
    homepage: https://github.com/pagoda111king/super-sop-node-os
    requires:
      bins:
        - python3
---

# Super SOP Node OS

Use this skill to turn complex work into node runs for projects, research, learning, implementation, enterprise delivery, and reusable SOP design.

## Default Behavior

For project-like, recurring, research-heavy, workflow, product, learning, or system-building tasks:

1. Select the smallest useful node chain.
2. Run nodes in order.
3. Produce durable artifacts when useful.
4. Run Check before delivery.
5. Sediment reusable assets only when they have `source_ref` and `next_use_case`.

For simple one-off tasks, use the minimum relevant nodes and do not over-process.

## 14 Node Classes

```text
Intake, Context, Radar, Normalize, Data, Planning, Routing, Learning, Action, Test, Score, Check, Handoff, Sediment
```

## Common Chains

```text
Research:
Intake -> Context -> Radar -> Normalize -> Score -> Check -> Sediment

Implementation:
Intake -> Context -> Planning -> Routing -> Action -> Test -> Check -> Handoff -> Sediment

Learning:
Intake -> Context -> Radar -> Normalize -> Learning -> Test -> Score -> Check -> Sediment

Enterprise:
Intake -> Context -> Data -> Planning -> Action -> Check -> Handoff -> Sediment
```

## Run Folder

When a durable run is useful, run:

```bash
python3 scripts/create_node_run.py --goal "<goal>" --type research
```

Then fill the generated node files.

## Reference Loading

Read only what is needed:

- `references/architecture.md` for 6-layer / 14-node architecture.
- `references/node-protocol.md` for node artifact format.
- `references/memory-symbols.md` for colors, runes, and memory palace symbols.

## Quality Gate

Before finalizing complex work, answer:

```text
Which chain ran?
What evidence supports it?
What artifact was created?
What check passed?
What should be sedimented?
```

Do not send unlearned concepts directly into review/battle. Run Learning, enrichment, Test, Score, and Check first.

## Safety

This skill does not require external credentials. Its helper script creates local markdown run folders and should only write under the run root chosen by the user.
