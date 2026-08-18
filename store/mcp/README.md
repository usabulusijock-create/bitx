# MCP 包（mcp）

完整步骤见 [docs/14-EXTENDING.md](../../docs/14-EXTENDING.md)。本文件与 GitHub `store/mcp/` 同步。

每个子目录一个 MCP 服务器，用户安装到 `%APPDATA%\BitX6-2\mcp\`。

```
store/mcp/<server-id>/
  mcp.json        # 必填
  README.md
  server.js       # 或包内 exe；必须能启动
```

`mcp.json`：

```json
{
  "id": "my-mcp",
  "name": "显示名",
  "version": "1.0.0",
  "command": "node",
  "args": ["./server.js"],
  "disabled": false
}
```

规则：

- 主程序 **不** 预置 filesystem / browser / fetch。
- `command: "node"` 由 BitX 换成便携 Node，`args[0]` 必须是**本包内真实存在的文件**。
- 上架前必须在本机跑通 `listTools`。跑不通不准进 store。
- 文件读写用引擎工具，不要做 filesystem MCP。
