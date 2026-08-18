# 04 进程

旁路 Node 主进程绑 `127.0.0.1`（默认 17322，占用则递增，**实际端口写入 `app/current.json`**）。

提供：静态页 + `POST /rpc` + `GET /events` SSE。

**鉴权与权限分开：**

| 项 | 默认 | 含义 |
| --- | --- | --- |
| Agent 闸门 `security.enforced` | `false` | 对话改代码、Shell、写盘按最高权限 |
| RPC 会话令牌 | 每次启动随机 | 只有本窗口 WebView2 能调 RPC；本机其它进程不能指挥 Agent |

令牌由启动器注入 WebView2（query 或 header）。无令牌的请求一律拒绝。开发机可用浏览器，但必须带同一令牌。

`python scripts/dev.py`：探测便携 Node → 编译 → 起服务 → 开 WebView2（调试才开浏览器）。

Workbench 禁止直连 Marketplace。MCP/Shell 的 PATH 必须前置便携 Node。
