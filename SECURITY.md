# Security

Super SOP Node OS is mostly text instructions, schemas, and a small Python helper script.

## Reporting

Open a GitHub issue if you find:

- a prompt-injection risk in a loader file or skill instruction
- a script that writes outside the requested run directory
- unclear permission or credential expectations
- unsafe publishing or installation guidance

## Current Permission Model

- No external API credentials are required.
- The helper script writes markdown files into the selected `runs/` root.
- The skill declares `python3` as a required binary because the helper script uses Python.

## User Guidance

Inspect any installed agent skill before use. Treat third-party skills as code and instruction bundles that can influence agent behavior.
