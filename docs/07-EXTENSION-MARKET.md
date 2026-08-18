# 07 官方插件市场

主进程：`POST https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery`（criteria 含 `Microsoft.VisualStudio.Code`）。

下载：`GET .../publishers/{publisher}/vsextensions/{name}/{version}/vspackage`。

VSIX 为 zip，解压到 `{userData}/extensions/{publisher}.{name}-{version}/`，防 zip slip。`engines.vscode` 不拒绝安装。

`@bitx/plugins` 是 BitX 自有清单，与 VS 市场分开。
