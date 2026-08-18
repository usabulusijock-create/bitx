# 技能包（skills）

完整步骤见 [docs/14-EXTENDING.md](../../docs/14-EXTENDING.md)。本文件与 GitHub `store/skills/` 同步。

每个子目录一个技能，用户安装到 `%APPDATA%\BitX6-2\skills\`。

```
store/skills/<skill-id>/
  SKILL.md        # 必填（YAML 头 + 正文）
```

```markdown
---
id: my-skill
name: 显示名
description: 一句话
---

技能正文，交给模型按需加载。
```

主程序不内置技能目录。未安装任何技能时，Agent 仍用引擎工具直接干活。
