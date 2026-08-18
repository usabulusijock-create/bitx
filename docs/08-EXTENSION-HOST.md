# 08 扩展宿主（BitX 兼容，非官方 extensionHost）

禁止启动微软 `extensionHost`。BitX 自己实现一份 **vscode 兼容层**：能搜、能装官方 VSIX，再按 contributes + `main` 尽量跑起来。

安装之后必须同时具备搜索 / 安装 / 卸载 / 启用，不再按 L0–L3 分期。

## 同时启用

| 能力 | 行为 |
| --- | --- |
| 市场 | 扩展页搜索官方 Gallery，下载 VSIX，写入 `extensions.json` |
| 声明式贡献 | `themes`、`iconThemes`、`languages`、`grammars`、`snippets`、`configuration`、`commands`、`keybindings`、`views` |
| `vscode` 垫片 | 已启用且含 `main` 的扩展调用 `activate(context)`；补齐常用 `vscode.*` |
| 语言服务 | 由扩展 `main` 按 vscode API（含 LanguageClient）拉起；诊断进入 `BitxHost.getDiagnostics`。禁止只按文件名扫描 `server.js` 就 spawn |

`engines.vscode` 不阻止安装。UI 标明来源是 VS Code 市场，由 BitX 宿主加载。

不保证每一个官方 `main` 都能跑通（微软 API 面无界）。失败：捕获、记日志、**保持已安装**、声明式贡献（主题/语法/片段）仍可用，不得卸载。

## 主题

读 theme JSONC → 工作台 CSS 变量 + 编辑器 token。切换不重装。

## `vscode` 垫片范围

必须实现并接到 Host / 工作台：

- `Uri` `EventEmitter` `Disposable` `Position` `Range` `Selection` `Location`
- `window`：消息、输出通道、状态栏、进度、活动编辑器、选区
- `workspace`：`workspaceFolders`、`fs`、`openTextDocument`、`getConfiguration`、文档变更事件
- `languages`：补全、悬停、定义、诊断集合、格式化
- `commands.registerCommand` / `executeCommand`
- `extensions.getExtension` / `all`
- `env` / `version`（报告 BitX 兼容标识，不是 VS Code 冒充发行版）

## 中文语言包

BitX UI 本身为中文。若用户安装 `vscode-language-pack-zh-hans`，解析 `contributes.localizations` 能合并的字符串则合并，不能合并则忽略，不得崩溃。

## 验收

1. 扩展页能搜索官方市场，能安装 / 卸载 / 启用 / 禁用。
2. 安装官方主题，切换后工作台变色。
3. 安装含 snippets/grammars 的扩展，编辑器能用。
4. 含 `main` 的扩展：尝试 `activate`；失败只提示日志，扩展仍留在已安装列表。
