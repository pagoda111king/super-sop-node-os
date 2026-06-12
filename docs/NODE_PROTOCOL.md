# Node Protocol

## Node Definition

A node is a small verifiable machine with:

- mission
- input contract
- workspace
- tool permissions
- output schema
- check rules
- failure return path
- handoff method
- sediment path

## Node Run Folder

Recommended:

```text
runs/<run_id>/
├── run.md
├── 01_intake.md
├── 02_context.md
├── radar/
├── normalize/
├── checks/
├── scores/
└── sediment.md
```

## Node Artifact Template

```markdown
# <Node Type> · <Short Name>

## Purpose

## Inputs

## Work

## Outputs

## Check

## Next
```

## Node Envelope v1.1

For serious runs, each node should carry this envelope even if the human-facing artifact is Markdown:

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

## Cross-Cutting Rails

Every non-trivial node should carry four rails:

| Rail | Required Questions |
|---|---|
| Observe / Trace | What happened, which tools ran, what failed, what did it cost? |
| Policy / Permission | What is allowed, what identity is used, what needs approval, how can we roll back? |
| Artifact Registry | What durable outputs exist, where are they stored, what schema/version/status do they have? |
| Human / Team | Who reviews, who accepts handoff, who owns the decision, where does escalation go? |

## Check Results

Use only:

```text
pass
fix
return
escalate
kill
accept_risk
```

## Score Verdicts

Use only:

```text
adopt
revise
monitor
reject
```

## Sediment Rules

Do not sediment unless the asset has:

- source_ref
- next_use_case
- check status
- owner or downstream user

Never sediment a vague summary.
