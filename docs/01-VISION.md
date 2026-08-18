# 01 产品目标

BitX 第二代是 **AI 原生、可装官方插件的独立 IDE**：打开工作区、编辑、终端、对话改代码；在 BitX 内 **搜索并安装** VS Code 官方市场插件；整条链不经过 VS Code 窗口、不启动官方 `extensionHost`。

离开一代是因为壳绑死在 `apps/bitx-ide` / `vs/*`。二代拆开：脑可复用，壳重写。插件兼容靠 **自研 `vscode` 垫片 + 声明式 contributes**，不是微软那份宿主。

| 允许 | 禁止 |
| --- | --- |
| Marketplace 公开 HTTP、搜、下、装 VSIX；contributes；LSP；自研 `vscode` 垫片 | 拷贝 VS Code 源码、跑官方 extensionHost、`import 'vs/...'` |
| Monaco（MIT，打进旁路包） | 把 Monaco 说成「我们是 VS Code」；生产走 CDN |

成功标准：启动路径没有 VS Code workbench；扩展页能搜、装、卸官方市场插件并由 BitX 宿主加载；引擎委托闭环在自研 Host 上跑通。
