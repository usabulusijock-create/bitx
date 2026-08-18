# 09 Host

`@bitx/host-node` 实现完整 `BitxHost`：fs/git/shell/ide/net/memory/ui/mcp/browser 桩/隔离目录。

工作区根由 `workspace.open` 设置。闸门关闭时允许工作区外路径（与一代语义一致）。活动编辑器由工作台上报。Ask/Diff 经 RPC。
