# 12 硬约束

1. 禁止将一代 `apps/bitx-ide`、`apps/VSCode-win32-x64` 作为二代运行时。
2. 禁止 VS Code 源码进本仓；禁止 `import vs/*`。
3. 禁止启动官方 `extensionHost`；禁止伪造 `product.json` 冒充发行版。
4. 禁止 `_generated/@bitx` 同步树；引擎以 workspace 包直接引用。
5. 禁止顶层出现 `apps/bitx-ide`、`out-vscode`。
6. 引擎禁止引用 desktop / DOM / Electron。
7. Host 只走 `@bitx/host-protocol`。
8. 必须尝试 `activate(main)`；失败只记日志，不得卸载。
9. API Key 不得传给 Marketplace。
10. 未列入 [03-DIRECTORY.md](03-DIRECTORY.md) 的顶层目录不得擅自创建。
11. 日常升级禁止覆盖已安装的 `BitX.exe`；只有 `exeVersion` 增加才换启动器（见 13）。
12. `docs/`、`store/`、`channels/`、根 `README.md` 改完必须推到 github.com/usabulusijock-create/bitx 同一路径；禁止只改本地不公开。
