# 14 开发插件 / MCP / 技能

给开源协作者和客户：在 BitX 里加能力，**不要改 exe**。包放到本仓 `store/`，用户装进自己的用户目录。

公开约定以本文件 + `store/` 下 README 为准，与 [github.com/usabulusijock-create/bitx](https://github.com/usabulusijock-create/bitx) 同步。

## 三种东西，不要混

| 类型 | 本仓目录 | 用户安装位置 | 清单文件 |
| --- | --- | --- | --- |
| BitX 插件 | [`store/plugins/`](../store/plugins/) | `%APPDATA%\BitX6-2\plugins\<id>\` | `plugin.json` |
| MCP 服务器 | [`store/mcp/`](../store/mcp/) | `%APPDATA%\BitX6-2\mcp\<id>\` | `mcp.json` |
| 技能 | [`store/skills/`](../store/skills/) | `%APPDATA%\BitX6-2\skills\<id>\` | `SKILL.md` |

另外：VS Code 官方市场扩展走 [07](07-EXTENSION-MARKET.md) / [08](08-EXTENSION-HOST.md)，不是 `store/plugins`。

主程序 **不内置** 任何插件 id、MCP 默认项、技能目录。没装 = 没有这项能力，正常；核心 `fs_read` / `fs_write` / `grep` / `shell_run` 仍可用。

Agent 默认最高权限。闸门只在用户打开 `security.enforced` 时生效。

---

## 插件

每个子目录一个插件：

```
store/plugins/<plugin-id>/
  plugin.json     # 必填
  README.md       # 给用户看：做什么、怎么装
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

规则：

- `id` 与目录名一致，小写、短横线。
- `contributes.skills` / `contributes.mcp` 填本仓其它包的 `id`，表示「装这个插件时建议一并装这些」。不要把 MCP 源码塞进插件目录除非你同时提供完整可启动包。
- 上架前 README 必须写清依赖（Node 由 BitX 便携运行时提供，不要要求用户自己配 PATH）。

安装：把整个 `<plugin-id>` 文件夹拷到 `%APPDATA%\BitX6-2\plugins\`。BitX 启动时扫描该目录，没有则当没装。

---

## MCP

每个子目录一个服务器，**必须自包含、本机能启动**：

```
store/mcp/<server-id>/
  mcp.json        # 必填
  README.md
  server.js       # 或包内 exe；路径必须真实存在
```

`mcp.json`：

```json
{
  "id": "my-mcp",
  "name": "显示名",
  "version": "1.0.0",
  "command": "node",
  "args": ["./server.js"],
  "disabled": false
}
```

规则：

1. 主程序 **不** 预置 filesystem / browser / fetch。文件读写用引擎工具，不要做 filesystem MCP。
2. `command: "node"` 由 BitX 换成便携 Node；`args[0]` 必须是**本包内**文件（相对包根）。
3. 上架前本机跑通 MCP `listTools`。跑不通不准进 `store/mcp`。
4. 禁止依赖「系统已经装了 node / 某个全局 npm 包」。依赖打进包，或写明由 BitX 便携 Node 执行的相对路径。
5. 未安装 ≠ 启动失败：用户目录没有这个 id，设置里就没有这一项，不要弹「MCP 启动失败」。

安装：拷到 `%APPDATA%\BitX6-2\mcp\<server-id>\`。

---

## 技能

每个子目录一个技能：

```
store/skills/<skill-id>/
  SKILL.md        # 必填：YAML 头 + 正文
  README.md       # 可选，给人类；模型只读 SKILL.md
```

```markdown
---
id: my-skill
name: 显示名
description: 一句话，说明何时该用
---

技能正文，交给模型按需加载。写清步骤、禁止事项、输入输出。
```

规则：

- `id` 与目录名一致。
- `description` 会进工具/技能列表，写清楚触发条件。
- 未安装任何技能时，Agent 仍用引擎工具干活。

安装：拷到 `%APPDATA%\BitX6-2\skills\<skill-id>\`。

---

## 上架与开源同步

1. 在本地 `F:\BitX6-2\store\...` 按上面的目录做出能跑的包。
2. 改文档只改本仓 `docs/` 与 `store/**/README.md`。
3. **推到 GitHub `usabulusijock-create/bitx` 的同一路径。** 客户查文档、下载约定，都以 GitHub 为准。
4. 以后网站货架读本仓 `store/`（或后续的 `store/index.json`），不要另写一份互相打架的说明。

禁止：把插件 / MCP / 技能打进 `BitX.exe` 或旁路主包。日常升级见 [13-UPDATES.md](13-UPDATES.md)。
