# 02 总架构

```mermaid
flowchart TB
  WV[WebView2 生产窗口]
  WB[apps/desktop workbench]
  RPC["HTTP JSON-RPC + SSE 127.0.0.1"]
  ORCH["@bitx/engine"]
  HOST["@bitx/host-node"]
  EXT["@bitx/extensions BitX vscode 垫片"]
  SET["@bitx/settings"]
  GAL[VS Marketplace]
  LLM[模型 API]
  WS[工作区]
  WV --> WB --> RPC
  RPC --> ORCH
  ORCH --> HOST --> WS
  ORCH --> LLM
  RPC --> EXT --> GAL
  RPC --> SET
```

依赖只向下：`apps/desktop` → engine / host-node / extensions / settings；engine 禁止反向依赖壳。模型请求由 **引擎** 发出，不经过 Host。

编辑器隔离在工作台；**Monaco 打进旁路 zip**，禁止生产走 npm/CDN。生产窗口用 WebView2 加载本机旁路页面。系统浏览器仅开发机调试。

**权限：默认最高。** 不鉴权 RPC，不默认拦写盘 / Shell / 工作区外路径。
