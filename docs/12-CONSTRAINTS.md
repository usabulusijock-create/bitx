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
13. 客户拿到的 EXE 是小安装器：读清单再下 zip，禁止 git clone 源码到客户机。默认目录 `D:\BitX`（无 D 盘则 `C:\BitX`），用户可改。装完创建桌面「BitX」快捷方式；**官网快捷方式不强制、默认不创建**。安装源只信 GitHub 本仓，并预留官方网站域名（后补，见 13）。
14. 发给客户的 EXE 必须 Authenticode 签名（优先 EV）+ 时间戳。禁止加壳/免杀/让用户关杀毒。Defender 或 SmartScreen 报威胁则停发（见 13）。
15. **默认最高权限**：RPC 绑 `127.0.0.1`，禁止加会话令牌/默认鉴权；Agent 禁止默认拦写盘、Shell、工作区外路径。Monaco 打进旁路包。禁止官方 `extensionHost`；必须能搜索并安装 VS Code 官方市场插件。
