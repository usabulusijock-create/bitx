# 可分发扩展仓（不进主程序 / 不进 exe）

插件、MCP、技能 **禁止打进 BitX.exe 和旁路主包**。本目录是研发货架，与 [GitHub 仓](https://github.com/usabulusijock-create/bitx) 同步，方便开源和客户查询。做完按 [14-EXTENDING.md](../docs/14-EXTENDING.md) 上架；用户装到自己的用户目录。

| 目录 | 装什么 | 用户安装位置 |
| --- | --- | --- |
| `store/plugins/` | BitX 插件包 | `%APPDATA%\BitX6-2\plugins\<id>\` |
| `store/mcp/` | MCP 服务器包 | `%APPDATA%\BitX6-2\mcp\<id>\` |
| `store/skills/` | 技能包 | `%APPDATA%\BitX6-2\skills\<id>\` |

## 和「404」的关系

404 / `spawn node ENOENT` 是 **开发事故**：主程序去拉了一个根本没打进包、本机也没有的服务。

正确做法：

1. **核心能力在引擎里就必须能用**：`fs_read` / `fs_write` / `grep` / `shell_run` 不经过 MCP，开箱即用。没有 filesystem MCP，文件照样能改。
2. **主程序不准预置** `npx @modelcontextprotocol/server-filesystem` 这类会炸的默认项。
3. **store 里的包必须自包含**：`command` 指向包内脚本或自带可执行文件；BitX 用便携 Node 去跑。开发时要能真正启动，禁止带病上架。
4. **没安装 ≠ 启动失败**：目录里没有这个包，设置里就没有这一项，不要弹「MCP 启动失败」。

Agent 默认最高权限。不要默认拦截。闸门只有用户自己打开才生效。
