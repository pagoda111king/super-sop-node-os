# Architecture · 6 Layers / 14 Node Classes

Super SOP Node OS turns work into node runs.

## 6 Layers

| Layer | Role | Nodes |
|---|---|---|
| Input Capture | Turn messy signals into task objects | Intake |
| Context & Memory | Load rules, history, constraints | Context / Memory |
| Cognition & Orchestration | Retrieve, normalize, model, plan, route, learn | Radar, Normalize, Data, Planning, Routing, Learning |
| Action | Make real changes through tools | Action |
| Validation & Governance | Test, score, gate, control risk | Test, Score, Check |
| Sediment Assets | Deliver and write back reusable assets | Handoff, Sediment |

## 14 Node Classes

| Node | Eats | Produces |
|---|---|---|
| Intake | messy input | task object |
| Context / Memory | task + history | context pack |
| Radar | questions | traceable evidence |
| Evidence Normalize | messy evidence | structured records |
| Data Modeling | expected queries | schema/storage plan |
| Planning | goal | steps/dependencies |
| Routing | task state | selected path |
| Learning | unfamiliar concept | teachable lesson |
| Action | plan | real artifact/change |
| Test | claim/artifact | reproducible evidence |
| Score | evidence + tests | score/verdict |
| Check | artifact + risk rules | pass/fix/return |
| Handoff | artifact | delivery package |
| Sediment | validated learning | reusable asset |

## Relationship To 17-Step SOPs

The 17-step SOP lifecycle is a route through the node system.

```text
17 steps = project lifecycle
14 nodes = reusable machine parts
```

One SOP step can call many node classes. One node class can appear across many SOP steps.

## P0 Compound Nodes

Prioritize:

```text
Radar
Evidence Normalize
Data Modeling
Test
Score
Check
Rule Learning
Sediment
```

`Rule Learning` is implemented under the Sediment family but kept as its own P0 practice because it updates rollback-safe rules from test/score/check feedback.

