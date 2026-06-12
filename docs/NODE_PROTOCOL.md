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

