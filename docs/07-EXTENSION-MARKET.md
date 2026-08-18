# 07 官方插件市场

目标：客户在 BitX 扩展页 **搜索、安装、卸载、启用/禁用** VS Code 官方市场插件。不启动官方 `extensionHost`，由 BitX 宿主加载（见 08）。

主进程：`POST https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery`（criteria 含 `Microsoft.VisualStudio.Code`）。

下载：`GET .../publishers/{publisher}/vsextensions/{name}/{version}/vspackage`。

VSIX 为 zip，解压到 `%APPDATA%\BitX6-2\extensions/{publisher}.{name}-{version}/`，防 zip slip。`engines.vscode` **不拒绝安装**（兼容宿主自己消化，不拿 VS Code 版本卡客户）。

UI 标明：来源是 VS Code 市场，由 **BitX 兼容宿主** 加载，不是 VS Code。

`@bitx/plugins` / `store/plugins` 是 BitX 自有货架，与 VS 市场分开。
