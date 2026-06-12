# Company References

Latest tracked radar:

- [REFERENCE_RADAR_2026-06-12.md](REFERENCE_RADAR_2026-06-12.md)

The node system was informed by public agent patterns from:

| Source | What To Learn | Primary URL |
|---|---|
| OpenAI Codex / Agents SDK | AGENTS.md, skills, tools, handoffs, guardrails, tracing | https://developers.openai.com/codex/guides/agents-md |
| Anthropic Building Effective Agents | workflow patterns, routing, parallelization, evaluator-optimizer | https://www.anthropic.com/research/building-effective-agents |
| Google ADK / A2A | context engineering, sessions, memory, artifacts, agent interoperability | https://adk.dev/ |
| Microsoft Agent Framework / Magentic-One | orchestrator-workers, state, telemetry, enterprise governance | https://learn.microsoft.com/en-us/agent-framework/overview/ |
| LangGraph | durable execution, persistence, human-in-the-loop, interrupts | https://docs.langchain.com/oss/python/langgraph/overview |
| OpenClaw / ClawHub | skills/plugins, registry, gating, package trust | https://docs.openclaw.ai/clawhub |
| OpenMAIC | multi-agent classroom, interactive learning, quizzes, simulations | https://github.com/THU-MAIC/OpenMAIC |
| Hermes Agent | persistent memory, automated skill creation, always-on gateway | https://hermes-agent.nousresearch.com/docs/ |
| Feishu / Aily | China enterprise work surface: IM, docs, Base, approval, tasks | https://www.feishu.cn/hc/en-US/articles/790732948604-get-started-with-feishu-aily |
| Coze Studio / Loop | low-code workflow nodes, DAG execution, prompt/eval/trace AgentOps | https://github.com/coze-dev/coze-studio |
| DeerFlow | long-horizon agent harness, memory, filesystem, sandbox, skills | https://github.com/bytedance/deer-flow |
| AgentScope | production multi-agent runtime, permissions, workspace, memory, evaluation | https://doc.agentscope.io/ |

Rule:

```text
Do not copy framework terminology blindly.
Map each pattern to a node contract, test it, score it, then sediment it.
```

Confirmed direction:

```text
conversation -> agent -> persistent agent system -> node-based operating system
```
