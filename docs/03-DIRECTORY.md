# 03 目录结构

```
BitX6-2/
├── README.md                  # GitHub 首页，客户入口
├── docs/                      # 推到 GitHub，与开源查询同一份
├── channels/                  # 推到 github.com/usabulusijock-create/bitx
│   └── stable.json            # 升级清单（raw 给客户端读）
├── store/                     # 不进 exe：研发货架，上传网站后用户自装
│   ├── plugins/
│   ├── mcp/
│   └── skills/
├── scripts/
├── apps/desktop/              # 旁路：工作台 + 主进程（打进 payload zip）
└── packages/                  # 旁路：引擎/Host（打进 payload zip）
```

安装后用户机器（默认）：

```
D:\BitX\BitX.exe              # 小安装器拷过来的启动器，日常不覆盖
D:\BitX\app\<版本>\           # 安装器从 GitHub Release 拉下来的旁路
桌面\BitX.lnk                 # 启动 IDE
桌面\BitX 官网.url            # 清单 website（现为 GitHub 仓）
%APPDATA%\BitX6-2\plugins|mcp|skills
```

升级设计见 [13-UPDATES.md](13-UPDATES.md)。插件 / MCP / 技能开发见 [14-EXTENDING.md](14-EXTENDING.md)。文档必须同步到 [usabulusijock-create/bitx](https://github.com/usabulusijock-create/bitx)。
