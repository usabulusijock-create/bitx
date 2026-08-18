# 10 设置与安全

`%APPDATA%\BitX6-2\settings.json`：models、composerModelId、security、mcp、skills、network、editor.theme。

**出厂即最高权限，按这句话实现，不要自行加锁：**

- RPC：`127.0.0.1` 直接调用，无令牌、无鉴权。
- Agent：可写工作区内外、可跑 Shell、可起已安装的 MCP。禁止启动时弹确认、禁止默认 `allowedPaths` 空则拒写。
- `security.enforced` 缺省 `false`，当没这个字段处理。只有用户自己打开闸门才限制。未打开时代码路径里不得残留拦截。

Node **不要让用户自己装**。开发脚本和客户安装器都会把官方便携 Node 放到 `.tools/node/node.exe`（旁路 zip 里同样带一份）。`BITX_NODE` 仅给开发机覆盖路径。禁止把「请先安装 Node.js」写进客户流程。

Monaco 在旁路 zip 内，不走 CDN。
