# GitHub 仓库维护清单

每次发布前检查一次。仓库页面元数据不由 Git 文件自动同步。

## About

- Description 与 README 首屏定位一致。
- 不使用“保证爆款”“保证成交”等无法验证的承诺。

## Topics

建议使用小写、短横线分隔的准确关键词（不超过 20 个）：

`python` `llm` `content-generation` `copywriting` `social-media` `ai-agent` `cli` `prompt-engineering` `content-marketing`

## Social Preview

使用包含项目名、核心公式和 GitHub URL 的 1280×640 PNG/JPG，文件小于 1 MB。避免把“爆款保证”放进图片。

## Release

1. 更新 `pyproject.toml`、README 和 CHANGELOG 版本号。
2. 运行测试、lint、文档检查和配置校验。
3. 使用 `RELEASE_TEMPLATE.md` 创建 Release。
4. 在 Release 正文放入 30 秒 Demo 和已知边界。
