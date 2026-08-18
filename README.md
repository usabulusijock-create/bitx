# BitX

独立 AI IDE。打开工作区、编辑、终端、对话改代码；可搜索安装 VS Code 官方市场扩展。壳不是 VS Code，引擎自研。

公开仓：[github.com/usabulusijock-create/bitx](https://github.com/usabulusijock-create/bitx)

**本仓是文档与扩展货架的公开源。** 本地改完文档必须推到这里，客户与开源协作者只认 GitHub 上的版本。

## 客户从这里查

| 你要做什么 | 打开 |
| --- | --- |
| 产品是什么、怎么分层 | [docs/01-VISION.md](docs/01-VISION.md) · [docs/02-ARCHITECTURE.md](docs/02-ARCHITECTURE.md) |
| 全部设计文档目录 | [docs/README.md](docs/README.md) |
| **写 BitX 插件** | [docs/14-EXTENDING.md](docs/14-EXTENDING.md#插件) · [store/plugins/](store/plugins/) |
| **写 MCP 服务器** | [docs/14-EXTENDING.md](docs/14-EXTENDING.md#mcp) · [store/mcp/](store/mcp/) |
| **写技能** | [docs/14-EXTENDING.md](docs/14-EXTENDING.md#技能) · [store/skills/](store/skills/) |
| 官方 VS 市场扩展怎么进 BitX | [docs/07-EXTENSION-MARKET.md](docs/07-EXTENSION-MARKET.md) · [docs/08-EXTENSION-HOST.md](docs/08-EXTENSION-HOST.md) |
| 装完以后怎么在线升级 | [docs/13-UPDATES.md](docs/13-UPDATES.md) |

扩展货架总说明：[store/README.md](store/README.md)

## 仓库里有什么

```
docs/                 产品与架构（开源 / 客户查询）
store/plugins|mcp|skills   扩展约定与示例包（不进 exe）
channels/stable.json  客户端升级清单
```

插件、MCP、技能 **不打进 BitX.exe**。用户装到 `%APPDATA%\BitX6-2\{plugins,mcp,skills}\`。核心读写由引擎工具完成，不依赖默认 filesystem MCP。

## 状态

二代实现进行中。文档先行；有 payload 后再填 `channels/stable.json` 的版本与 sha256。
