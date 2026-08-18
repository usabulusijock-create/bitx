# 10 设置与安全

`%APPDATA%\BitX6-2\settings.json`：models、composerModelId、security、mcp、skills、network、editor.theme。

**出厂即最高权限，按这句话实现，不要自行加锁：**

- RPC：`127.0.0.1` 直接调用，无令牌、无鉴权。
- Agent：可写工作区内外、可跑 Shell、可起已安装的 MCP。禁止启动时弹确认、禁止默认 `allowedPaths` 空则拒写。
- `security.enforced` 缺省 `false`，当没这个字段处理。只有用户自己打开闸门才限制。未打开时代码路径里不得残留拦截。

Node 探测（发布包）：`BITX_NODE` → 旁路目录 `.tools/node/node.exe` → 系统 `node`。发布包必须自带 `.tools`。

Monaco 在旁路 zip 内，不走 CDN。
