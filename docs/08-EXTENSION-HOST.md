# 08 扩展宿主

安装之后必须同时启用下列能力，不再按 L0–L3 分期。

## 同时启用

| 能力 | 行为 |
| --- | --- |
| 清单 | 解压 VSIX，写入 `extensions.json`，启用/禁用 |
| 声明式贡献 | `themes`、`iconThemes`、`languages`、`grammars`、`snippets`、`configuration`、`commands`、`keybindings`、`views` |
| 语言服务器 | 扫描扩展内常见 `server.js` / `lsp` 入口并拉起；诊断进入 `BitxHost.getDiagnostics` |
| `vscode` 垫片 | 对已启用且含 `main` 的扩展调用 `activate(context)`；提供常用 `vscode.*` API |

`engines.vscode` 不阻止安装。UI 标明来源是 VS Code 市场，由 BitX 宿主加载。

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

扩展 `main` 抛错时：捕获、记日志、不卸载、不影响其它扩展与引擎。

## 中文语言包

BitX UI 本身为中文。若用户安装 `vscode-language-pack-zh-hans`，解析 `contributes.localizations` 能合并的字符串则合并，不能合并则忽略，不得崩溃。

## 验收

1. 搜索并安装官方主题，切换后工作台变色。
2. 安装含 snippets/grammars 的扩展，编辑器能用。
3. 安装含 `main` 的扩展：尝试 `activate`；失败只提示日志。
4. 能卸载、禁用、再启用。
