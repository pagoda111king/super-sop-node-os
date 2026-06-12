# Contributing

Super SOP Node OS is a workflow protocol. Contributions should improve the clarity, safety, portability, or testability of the node system.

## Good Contributions

- Better node definitions.
- Better Check / Score / Test criteria.
- More examples of node runs.
- Better adapters for Codex, Claude Code, OpenClaw, and other agents.
- Safer or clearer scripts.
- More precise memory symbols and visual explanations.

## Rules

- Keep nodes explicit: purpose, inputs, outputs, check, next.
- Do not add vague motivational process text as a reusable rule.
- Prefer portable markdown, JSON, and Python standard library scripts.
- If a feature writes files, document where it writes and how to test it.

## Validation

Run:

```bash
python3 -m py_compile scripts/create_node_run.py
python3 scripts/create_node_run.py --goal "validation" --type learning --root /tmp/super-sop-node-os-runs
```
