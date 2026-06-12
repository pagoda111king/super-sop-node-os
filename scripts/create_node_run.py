#!/usr/bin/env python3
"""Create a Super SOP Node OS run folder."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


CHAINS = {
    "research": ["intake", "context", "radar", "normalize", "score", "check", "sediment"],
    "implementation": ["intake", "context", "planning", "routing", "action", "test", "check", "handoff", "sediment"],
    "learning": ["intake", "context", "radar", "normalize", "learning", "test", "score", "check", "sediment"],
    "enterprise": ["intake", "context", "data", "planning", "action", "check", "handoff", "sediment"],
    "full": ["intake", "context", "radar", "normalize", "data", "planning", "routing", "learning", "action", "test", "score", "check", "handoff", "sediment"],
}


NODE_TITLES = {
    "intake": "Intake 输入捕获",
    "context": "Context / Memory 上下文记忆",
    "radar": "Radar 雷达检索",
    "normalize": "Evidence Normalize 证据标准化",
    "data": "Data Modeling 数据建模",
    "planning": "Planning 计划拆解",
    "routing": "Routing 路由编排",
    "learning": "Learning 学习互动",
    "action": "Action 行动执行",
    "test": "Test 测试仿真",
    "score": "Score 评分评估",
    "check": "Check 检查治理",
    "handoff": "Handoff 交付交接",
    "sediment": "Sediment 沉淀规则学习",
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:80] or "node-run"


def node_file(index: int, node: str) -> str:
    return f"{index:02d}_{node}.md"


def node_template(index: int, node: str) -> str:
    title = NODE_TITLES[node]
    return f"""# N{index:02d} · {title}

## Purpose

## Inputs

## Work

## Outputs

## Check

- result:
- evidence_ref:
- return_target:

## Next

"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a node run folder.")
    parser.add_argument("--goal", required=True, help="Human-readable goal")
    parser.add_argument("--type", choices=sorted(CHAINS), default="research", help="Run type / default chain")
    parser.add_argument("--root", default="runs", help="Runs root directory")
    parser.add_argument("--run-id", default=None, help="Optional run id")
    args = parser.parse_args()

    today = dt.date.today().isoformat()
    run_id = args.run_id or f"{today}-{slugify(args.goal)}"
    root = Path(args.root)
    run_dir = root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    chain = CHAINS[args.type]
    (run_dir / "run.md").write_text(
        f"""# Node Run · {args.goal}

**run_id**: `{run_id}`  
**type**: `{args.type}`  
**created_at**: `{today}`  

## Chain

```text
{" -> ".join(chain)}
```

## Goal

{args.goal}

## Status

| Node | File | Status |
|---|---|---|
"""
        + "\n".join(
            f"| {node} | [{node_file(i + 1, node)}]({node_file(i + 1, node)}) | pending |"
            for i, node in enumerate(chain)
        )
        + "\n",
        encoding="utf-8",
    )

    for i, node in enumerate(chain, start=1):
        (run_dir / node_file(i, node)).write_text(node_template(i, node), encoding="utf-8")

    print(run_dir)


if __name__ == "__main__":
    main()

