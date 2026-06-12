# Publishing

## Create GitHub Repo

From this folder:

```bash
git init
git add .
git commit -m "Initial Super SOP Node OS package"
gh repo create super-sop-node-os --public --source=. --remote=origin --push
```

Recommended metadata:

```bash
gh repo edit pagoda111king/super-sop-node-os \
  --description "6-layer, 14-node SOP/agent workflow OS for Codex, Claude Code, OpenClaw, and reusable AI work." \
  --homepage "https://github.com/pagoda111king/super-sop-node-os" \
  --add-topic agent-workflow \
  --add-topic sop \
  --add-topic codex \
  --add-topic claude-code \
  --add-topic openclaw \
  --add-topic clawhub
```

## Use As Codex Project

Open the repo in Codex. Codex reads:

```text
AGENTS.md
```

## Use As Claude Code Project

Open the repo in Claude Code. Claude reads:

```text
CLAUDE.md
```

## Install Skill Manually

Copy:

```text
codex-skill/super-sop-node-os
```

to:

```text
~/.codex/skills/super-sop-node-os
```

Then restart or reload Codex skills.

## Publish To ClawHub

ClawHub publishes a skill folder that contains `SKILL.md`.

Use ClawHub CLI `0.21.0` or newer:

```bash
pnpm add -g clawhub@latest
clawhub --cli-version
```

```bash
clawhub whoami
clawhub publish /absolute/path/to/super-sop-node-os/codex-skill/super-sop-node-os \
  --slug super-sop-node-os \
  --name "Super SOP Node OS" \
  --version 1.0.0 \
  --changelog "Initial public release: 6-layer 14-node agent workflow system." \
  --tags latest,agent-workflow,sop,codex,claude-code,openclaw
```

Marketplace copy lives in:

```text
CLAWHUB_LISTING.md
```

The first successful publish receipt lives in:

```text
PUBLISH_RECEIPT.md
```

## Optional GitHub Action

ClawHub supports GitHub Actions publishing, but pushing workflow files requires a GitHub token with the `workflow` scope. This repository publishes with the CLI by default.
