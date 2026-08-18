# 04 进程

Node 主进程绑 `127.0.0.1:17322`（占用则递增）：静态页 + `POST /rpc` + `GET /events` SSE。

`python scripts/dev.py` 探测便携 Node → 编译 → 起服务 → 打开浏览器或 WebView2。

Workbench 禁止直连 Marketplace。MCP/Shell 的 PATH 必须前置便携 Node。
