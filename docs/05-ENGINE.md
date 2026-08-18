# 05 引擎

收编一代 `@bitx/engine` 及 host-protocol/memory/skills/mcp/agents/plugins/browser。desktop 只装配 `RealOrchestrator`，禁止复制 `toolLoop`。

`postJson` 用 Node fetch。诊断来自扩展宿主/LSP。设置走 `@bitx/settings`。发送模型前必须 `sanitizeChatMessages`。
