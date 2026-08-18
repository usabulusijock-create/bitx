# 10 设置与安全

`%APPDATA%\BitX6-2\settings.json`：models、composerModelId、security、mcp、skills、network、editor.theme。

Agent 默认 **最高权限**：`security.enforced` 缺省 `false`。闸门只在用户打开时生效；打开后写盘必须契约 `allowedPaths`，Shell/MCP 按开关与名单。

RPC 鉴权与 Agent 闸门无关：即使闸门关闭，没有会话令牌也不能从本机其它进程调 `/rpc`。

Node 探测（发布包）：`BITX_NODE` → 旁路目录 `.tools/node/node.exe` → 系统 `node`。发布包必须自带 `.tools`。禁止把开发机盘符写进产品规格。

Monaco 在旁路 zip 内，不走 CDN。
