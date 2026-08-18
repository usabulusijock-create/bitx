# 10 设置与安全

`%APPDATA%\BitX6-2\settings.json`：models、composerModelId、security、mcp、skills、network、editor.theme。

`security.enforced=true` 时写盘必须契约 allowedPaths，Shell/MCP 按开关与名单。

Node 探测：`BITX_NODE` → `BitX6-2/.tools/node/node.exe` → `F:\BitX6\.tools\node-v20.18.0-win-x64\node.exe`（仅开发机）→ 系统 node。发布包必须自带 .tools。
