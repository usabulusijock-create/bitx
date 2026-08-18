# 04 进程

旁路 Node 主进程绑 `127.0.0.1`（默认 17322，占用则递增，实际端口写入 `app/current.json`）。

提供：静态页 + `POST /rpc` + `GET /events` SSE。本机可调，**不加会话令牌、不鉴权**。这就是最高权限：工作台和 Agent 都能直接用。

Agent 写盘、Shell、工作区外路径默认全部放行。禁止出厂拦截。

`python scripts/dev.py`：探测便携 Node → 编译 → 起服务 → 开 WebView2（调试可用浏览器）。

Workbench 禁止直连 Marketplace。MCP/Shell 的 PATH 必须前置便携 Node。
