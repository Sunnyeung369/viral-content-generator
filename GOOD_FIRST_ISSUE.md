# 5 分钟贡献路径

适合第一次参与的改进：

1. 在 `data/styles/` 增加一个真实、可复用的风格卡。
   可先运行 `python scripts/new_style.py your_style --label "你的风格"` 生成模板。
2. 为现有示例补充输入和输出说明。
3. 修正文档中的命令、链接或错别字。
4. 为一个评分器补充边界测试。

提交前运行：

```bash
python -m pytest -q
ruff check viral_content viral_content_cli.py viral_article_cli.py
```

请在 PR 中说明：改了什么、如何验证、是否影响已有配置格式。不要提交 API Key、账号凭据或真实用户隐私数据。
