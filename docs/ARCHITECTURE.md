# Architecture · 6 Layers / 14 Node Classes

Latest system audit:

- [NODE_SYSTEM_AUDIT_2026-06-12.md](NODE_SYSTEM_AUDIT_2026-06-12.md)

Super SOP Node OS turns work into node runs.

## 6 Layers

### Current v1.0 Layers

| Layer | Role | Nodes |
|---|---|---|
| Input Capture | Turn messy signals into task objects | Intake |
| Context & Memory | Load rules, history, constraints | Context / Memory |
| Cognition & Orchestration | Retrieve, normalize, model, plan, route, learn | Radar, Normalize, Data, Planning, Routing, Learning |
| Action | Make real changes through tools | Action |
| Validation & Governance | Test, score, gate, control risk | Test, Score, Check |
| Sediment Assets | Deliver and write back reusable assets | Handoff, Sediment |

### Recommended v1.1 Layers

| Layer | Role | Nodes |
|---|---|---|
| Signal & Intent | Capture messy demand and true objective | Intake |
| Context, Memory & Workspace | Load memory, skills, rules, pruning policy, and workspace boundaries | Context / Memory |
| Evidence & Data | Search, normalize, and model facts/artifacts | Radar, Evidence Normalize, Data Modeling |
| Orchestration & Learning | Plan, route, delegate, and teach unfamiliar concepts | Planning, Routing, Learning |
| Execution & Assurance | Act, test, score, and gate the work | Action, Test, Score, Check |
| Delivery & Evolution | Hand off outputs and turn learning into reusable assets | Handoff, Sediment |

The public memory hook remains:

```text
6 layers, 14 nodes
```

But the professional explanation becomes:

```text
signal -> context -> evidence/data -> orchestration -> execution/assurance -> delivery/evolution
```

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

## Cross-Cutting Rails

The 2026-06-12 audit recommends four rails that every serious node run should carry:

| Rail | Purpose |
|---|---|
| Observe / Trace | Record trace IDs, tool calls, failures, latency, cost, and artifact events. |
| Policy / Permission | Track allowed tools, identity, secrets, sandbox, approval, and rollback. |
| Artifact Registry | Give durable outputs IDs, schemas, versions, owners, source refs, and validation status. |
| Human / Team | Define reviewer, approval gate, escalation path, handoff target, and decision owner. |
