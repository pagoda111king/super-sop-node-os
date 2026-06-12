# 超级 SOP 节点操作系统

Super SOP Node OS 是一套把复杂 AI 工作节点化的操作系统。

它不是普通清单，也不是一段提示词，而是一套可以被 Codex、Claude Code、OpenClaw、ClawHub 和其他 Agent 工具加载的工作协议。

核心公式：

```text
超级 SOP 节点操作系统 = 6 层 + 14 类核心节点 + 4 条横向轨道 + 节点运行产物 + Test/Score/Check/Sediment 闭环
```

## 一句话说明

过去我们靠“对话”完成 AI 工作。后来进入 Agent 时代，AI 开始调用工具、写代码、读文件、操作网页、执行任务。

再往后，OpenClaw、Hermes、Codex Skills、MCP、插件、CLI、企业工作流都说明了一件事：

```text
真正有价值的 AI 能力，都会变成可组合、可测试、可复用的节点。
```

所以这个项目的目标是：

```text
把万物重构成节点，让 AI 工作可以被计划、执行、检查、评分、交付和沉淀。
```

## 当前核心体系

目前采用：

```text
6 层 + 14 类核心节点 + 4 条横向轨道 + 2 个复合模式
```

### 6 层

| 层 | 中文含义 | 包含节点 |
|---|---|---|
| Signal & Intent | 信号与意图层 | Intake |
| Context, Memory & Workspace | 上下文、记忆与工作区层 | Context / Memory |
| Evidence & Data | 证据与数据层 | Radar, Evidence Normalize, Data Modeling |
| Orchestration & Learning | 编排与学习层 | Planning, Routing, Learning |
| Execution & Assurance | 执行与保障层 | Action, Test, Score, Check |
| Delivery & Evolution | 交付与进化层 | Handoff, Sediment |

### 14 类核心节点

| 节点 | 中文名 | 作用 |
|---|---|---|
| Intake | 接收节点 | 把混乱需求变成清晰任务对象 |
| Context / Memory | 上下文/记忆节点 | 加载规则、历史、偏好、约束、工作区 |
| Radar | 雷达节点 | 搜索足够多、可追踪、可信的资料 |
| Evidence Normalize | 证据整理节点 | 把资料整理成结构化证据 |
| Data Modeling | 数据建模节点 | 决定数据、产物、数据库、schema 怎么组织 |
| Planning | 计划节点 | 拆步骤、依赖、里程碑、停止条件 |
| Routing | 路由节点 | 决定走哪个节点链、分支、子 Agent、人工交接 |
| Learning | 学习节点 | 把不懂的概念变成可学、可测、可复习内容 |
| Action | 执行节点 | 真正改文件、写代码、操作工具、调用系统 |
| Test | 测试节点 | 产生可复现的测试证据 |
| Score | 打分节点 | 根据证据给出评分、优先级、风险判断 |
| Check | 检查节点 | 质量、权限、安全、交付门禁 |
| Handoff | 交付节点 | 把结果交给人、系统、仓库或下一个 Agent |
| Sediment | 沉淀节点 | 把有效经验沉淀为规则、技能、模板、SOP |

### 4 条横向轨道

这些不是普通节点，而是贯穿所有重要节点的工程能力。

| 轨道 | 作用 |
|---|---|
| Observe / Trace | 记录工具调用、失败、成本、trace、事件 |
| Policy / Permission | 管理权限、身份、沙箱、审批、回滚 |
| Artifact Registry | 管理产物 ID、schema、版本、来源、验证状态 |
| Human / Team | 管理评审人、决策人、升级路径、交付对象 |

### 2 个复合模式

| 复合模式 | 由哪些能力组成 |
|---|---|
| Deploy / Publish | Action + Check + Handoff |
| Monitor / Ops | Observe/Trace + Test + Score + Check + Sediment |

## 常用节点链

### 研究链

```text
Intake -> Context -> Radar -> Normalize -> Score -> Check -> Sediment
```

适合框架对比、技术调研、资料收集、趋势判断。

### 实施链

```text
Intake -> Context -> Planning -> Routing -> Action -> Test -> Check -> Handoff -> Sediment
```

适合写代码、改项目、做功能、做自动化。

### 学习链

```text
Intake -> Context -> Radar -> Normalize -> Learning -> Test -> Score -> Check -> Sediment
```

适合学习概念、做笔记、转成知识对战、生成复习卡。

### 企业交付链

```text
Intake -> Context -> Data Modeling -> Planning -> Action -> Check -> Handoff -> Sediment
```

适合客户交付、运营 SOP、企业内部系统、飞书/Notion/Base 这类业务系统。

## 中文阅读顺序

建议按这个顺序看：

1. 本文件：整体中文说明
2. `docs/ARCHITECTURE.md`：6 层 14 节点架构
3. `docs/NODE_PROTOCOL.md`：节点运行协议
4. `docs/NODE_SYSTEM_AUDIT_2026-06-12.md`：最新节点体系审计
5. `docs/MEMORY_SYMBOLS.md`：颜色、符号、记忆宫殿体系
6. `AGENTS.md`：Codex 加载文件
7. `CLAUDE.md`：Claude Code 加载文件
8. `codex-skill/super-sop-node-os/SKILL.md`：Codex Skill 加载文本

## 重要文件说明

| 文件 | 用途 |
|---|---|
| `README.md` | 英文总介绍 |
| `README.zh-CN.md` | 中文总介绍 |
| `AGENTS.md` | Codex 项目加载说明 |
| `CLAUDE.md` | Claude Code 项目加载说明 |
| `docs/ARCHITECTURE.md` | 架构文档 |
| `docs/NODE_PROTOCOL.md` | 节点协议 |
| `docs/NODE_SYSTEM_AUDIT_2026-06-12.md` | 逐项目审计后的 v1.1 提案 |
| `docs/REFERENCE_RADAR_2026-06-12.md` | 外部参考框架雷达 |
| `docs/COMPANY_REFERENCES.md` | OpenAI、Anthropic、Google、Microsoft 等经验映射 |
| `docs/MEMORY_SYMBOLS.md` | 颜色符号和记忆系统 |
| `schemas/node-taxonomy.v1.json` | 机器可读节点分类 |
| `schemas/node-taxonomy.v1.1-proposal.json` | v1.1 提案 schema |
| `examples/node-run-template.md` | 节点运行模板 |
| `prompts/nodeize-task.md` | 节点化任务提示 |
| `prompts/node-review.md` | 节点审查提示 |

## 如何运行一个节点任务

```bash
python3 scripts/create_node_run.py --goal "构建一个可复用客户交付 SOP" --type implementation
```

可选类型：

```text
research | implementation | learning | enterprise | full
```

生成结果会放在：

```text
runs/<run_id>/
```

## 如何给 Codex 使用

Codex 主要读取：

```text
AGENTS.md
docs/
schemas/
prompts/
scripts/
```

可以这样对 Codex 说：

```text
用 Super SOP Node OS 节点化这个任务。
先跑 Intake、Radar、Normalize、Check。
把这个项目改造成节点运行链。
```

## 如何给 Claude Code 使用

Claude Code 主要读取：

```text
CLAUDE.md
.claude/commands/nodeize.md
```

可以这样说：

```text
Run /nodeize on this feature request.
用 6 层 14 节点给这个项目做执行计划。
```

## 和节点雷达仓库的关系

这个仓库负责：

```text
定义节点操作系统本身。
```

另一个仓库负责：

```text
持续扫描外部项目，把 GitHub 项目、CLI、MCP、Skill、插件、软件归类成节点能力。
```

对应仓库：

```text
../super-sop-node-radar
```

## 最重要原则

```text
不要为了完成任务而跳过节点。
不要为了流程完整而滥用节点。
让每个节点在合适上下文中充分思考、产出、传递、检查、沉淀。
```

