# 11 交付范围

不分一期二期。下列能力在本仓一次做齐，缺一不可。

## 必须同时存在

1. 自研窗口与工作台（文件树、编辑器、对话、终端、设置、扩展页）
2. 官方 Marketplace 搜索 / 下载 / 安装 / 卸载 / 启用
3. 扩展宿主：`contributes`（主题、语法、片段、语言、命令、配置、视图声明）+ 执行 `main` 的 `vscode` 垫片 + LSP 拉起
4. 一代引擎闭环：对齐、工具、写盘、验证、安全闸门
5. Node `BitxHost`：文件、Git、Shell、诊断、MCP 子进程、Diff/Ask
6. 用户数据目录与 settings.json
7. `python scripts/dev.py` 一键启动
8. 小安装器：默认装到 `D:\BitX`，从 GitHub 拉旁路；桌面创建 BitX 与官网快捷方式。日常只换旁路，EXE 仅 `exeVersion` 变化时更（见 13）

## 明确不做（产品边界，不是分期）

- 不拷贝 VS Code 源码、不启动官方 extensionHost
- 不冒充 VS Code 发行版
- 不做 Microsoft 账号 Settings Sync
- 不保证 **每一个** 官方扩展的 `main` 都能跑通（垫片会尽量实现常用 API；失败时记录日志，扩展仍保持已安装，主题/语法/LSP 仍可用）

## 与一代

一代 `F:\BitX6` 继续作为 VS Code 发行版。二代是独立产品，禁止把二代嵌回 `vs/workbench`。
