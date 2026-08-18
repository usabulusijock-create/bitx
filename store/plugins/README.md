# 插件包（plugins）

完整步骤见 [docs/14-EXTENDING.md](../../docs/14-EXTENDING.md)。本文件与 GitHub `store/plugins/` 同步。

每个子目录一个插件，用户解压到 `%APPDATA%\BitX6-2\plugins\`。

```
store/plugins/<plugin-id>/
  plugin.json     # 必填
  README.md
```

`plugin.json`：

```json
{
  "id": "my-plugin",
  "name": "显示名",
  "version": "1.0.0",
  "description": "一句话",
  "contributes": {
    "skills": [],
    "mcp": []
  }
}
```

主程序不内置任何插件 id。目录为空 = 没有插件，正常。
