# 🚀 爆款内容生成器 v3.1

<div align="center">

![Version](https://img.shields.io/badge/version-3.1.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Platform](https://img.shields.io/badge/platform-全平台-orange)

**全平台内容创作系统 - 让爆款内容创作变得简单**

[快速开始](#快速开始) • [核心功能](#核心功能) • [使用文档](#使用文档) • [更新日志](./CHANGELOG.md) • [贡献指南](./CONTRIBUTING.md)

</div>

---

## 📖 简介

爆款内容生成器是一个基于深度研究的全平台内容创作系统，整合了50+现象级创作者的方法论，支持图文、短视频、长视频、音频等多种内容形式的创作。

### 💡 核心理念

> **所有优质短视频的底层都是爆款文案**  
> **所有爆款内容的本质都是注意力管理**

### ✨ 为什么选择我们？

- 🎯 **科学方法论**：基于用户决策的4次判断模型
- 🌐 **全平台支持**：一套系统，适配8大主流平台
- 📊 **数据驱动**：完整的数据分析与优化体系
- 🎨 **灵活定制**：8种预设风格 + 自定义风格系统
- 📚 **详尽文档**：10+文档文件，126KB+内容
- 🔧 **开箱即用**：提供CLI工具和完整模板

---

## 🎯 核心功能

### 1. 用户决策4次判断模型 ⭐⭐⭐⭐⭐

```
判断1：前3秒/前3句 → 跟我有关吗？（相关性）
判断2：前20秒/前20行 → 值不值得继续？（信任度）
判断3：看完整条内容 → 有没有真价值？（价值感）
判断4：看完之后 → 要不要关注你？（利用价值）
```

**适用于：** 所有平台的内容创作

---

### 2. 全平台内容矩阵 🌐

| 平台 | 形式 | 时长/字数 | 核心要素 | 优化重点 |
|------|------|----------|---------|---------|
| 抖音/快手 | 短视频 | 30-60秒 | 前3秒钩子 | 完播率 |
| 视频号 | 短视频 | 1-3分钟 | 传播价值 | 转发率 |
| B站 | 长视频 | 5-15分钟 | 章节设计 | 播放时长 |
| 小红书 | 图文/短视频 | 500-1000字 | 实用价值 | 收藏率 |
| 知乎 | 长文 | 3000-8000字 | 深度价值 | 点赞+收藏 |
| 公众号 | 长文 | 3000-10000字 | 系统价值 | 转发+在看 |
| 微博 | 短文 | 200-500字 | 观点鲜明 | 转发+评论 |
| 播客 | 音频 | 30-60分钟 | 深度对话 | 完播率 |

---

### 3. 8种预设风格 🎨

1. **老司机风格** - 接地气、犀利、反常识
2. **专业导师风格** - 系统化、有深度、温和
3. **故事叙述风格** - 情节丰富、画面感强
4. **数据分析风格** - 客观理性、数据驱动
5. **反常识风格** - 颠覆认知、引发思考
6. **清单工具风格** - 条理清晰、易于扫读
7. **对话问答风格** - 互动感强、针对性强
8. **诗意哲思风格** - 文笔优美、意境深远

---

### 4. 完整的创作流程 📝

```
选题分析（平台适配）
  ↓
大纲生成（4次判断检查）
  ↓
内容创作（简化原则）
  ↓
质量检查（综合评分）
  ↓
优化迭代（数据驱动）
```

---

### 5. 数据分析与优化 📊

**核心指标：**
- 完播率/阅读完成率
- 平均播放时长/阅读时长
- 互动率（点赞+评论+转发）
- 关注转化率

**优化策略：**
- 冷启动优化
- 完播率优化
- 互动率优化

---

## 🚀 快速开始

### ️⃣ 重要说明

本项目包含两个独立部分：

1. **skill_v3.0.md** - 纯粹的创作方法论（通用，不依赖任何AI）
2. **viral_article_cli.py** - CLI工具（辅助工具，方便调用AI）

**SKILL可以独立使用于：**
- 任何AI创作工具（Claude、ChatGPT、Gemini、DeepSeek等）
- 人工创作
- 团队协作标准

---

### 方式1：直接使用Skill文件（通用）

1. **下载Skill文件**
   ```bash
   git clone https://github.com/Sunnyeung369/viral-content-generator.git
   cd viral-content-generator
   ```

2. **阅读核心文档**
   - 📖 [skill_v3.0.md](./skill_v3.0.md) - 核心方法论（通用，可配合任何AI使用）
   - 📚 [使用手册.md](./使用手册.md) - 详细教程
   - 🎨 [风格配置模板.md](./风格配置模板.md) - 风格定制

3. **使用SKILL进行创作**

   **配合AI工具（推荐）：**
   - 复制 skill_v3.0.md 的内容
   - 粘贴到任意AI工具（Claude、ChatGPT、Gemini、DeepSeek等）的系统提示词
   - 开始创作

   **人工创作：**
   - 按照6次判断模型创作
   - 使用评分工具自我评估
   - 按照检查清单优化内容

---

### 方式2：使用CLI工具（辅助）

CLI工具是一个**辅助工具**，方便你配合AI使用：

**安装依赖**
```bash
pip install -r requirements.txt
```

**基本使用**
```bash
# 使用默认模型生成
python viral_article_cli.py "AI工具使用技巧"

# 指定AI平台
python viral_article_cli.py "AI工具使用技巧" --platform claude

# 流式输出（实时显示生成过程）
python viral_article_cli.py "AI工具使用技巧" --stream

# 自定义模型
python viral_article_cli.py "AI工具使用技巧" --platform claude --model claude-3-5-sonnet-20241022
```

**注意：** CLI工具只是调用AI的便捷方式，SKILL方法论可以配合任何AI工具使用。

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **设置API Key**
   ```bash
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="your-key"
   
   # Mac/Linux
   export OPENAI_API_KEY="your-key"
   ```

3. **生成内容**
   ```bash
   # 基本使用
   python viral_article_cli.py "AI工具使用技巧"
   
   # 指定风格和字数
   python viral_article_cli.py "AI工具使用技巧" \
     --style 老司机风格 \
     --words 6000 \
     --output article.md
   ```

---

### 方式3：在AI工具中使用（通用）

#### Claude Desktop
```bash
# 复制到Skills目录
cp skill_v3.0.md ~/.claude/skills/viral-content.md

# 使用
在Claude中输入：用爆款内容生成器帮我创作...
```

#### 任何AI平台使用（通用方法）
```
1. 复制 skill_v3.0.md 的全部内容
2. 粘贴到AI工具的系统提示词（System Prompt）
3. 开始创作

支持的AI工具（不限于）：
- Claude Desktop / Claude.ai
- ChatGPT / OpenAI
- Gemini / Google AI
- DeepSeek
- 文心一言
- Kimi 月之暗面
- 等等...

#### Cursor/VSCode（开发者）
```bash
# 创建.cursorrules文件
cp skill_v3.0.md .cursorrules

# Cursor会自动加载
```

详见：[跨平台使用指南](./跨平台使用指南.md)

---

## 📚 使用文档

### 核心文档

| 文档 | 说明 | 适合人群 |
|------|------|---------|
| [skill_v3.0.md](./skill_v3.0.md) | 核心方法论（45KB） | 所有人 |
| [使用手册.md](./使用手册.md) | 详细教程（15KB） | 新手 |
| [快速参考卡.md](./快速参考卡.md) | 速查卡片（9KB） | 进阶者 |
| [风格配置模板.md](./风格配置模板.md) | 风格定制（11KB） | 高手 |
| [跨平台使用指南.md](./跨平台使用指南.md) | 跨平台教程（11KB） | 开发者 |

### 辅助文档

- [v3.0升级说明.md](./v3.0升级说明.md) - 升级详情
- [CHANGELOG.md](./CHANGELOG.md) - 版本历史
- [CONTRIBUTING.md](./CONTRIBUTING.md) - 贡献指南
- [GitHub发布指南.md](./GitHub发布指南.md) - 发布教程

---

## 🎓 使用示例

### 示例1：创作短视频脚本

**输入：**
```
主题：短视频不爆的原因
平台：抖音
时长：60秒
风格：老司机风格
```

**输出：**
完整的60秒短视频脚本，包含：
- 0-3秒：相关性建立
- 3-20秒：信任度建立
- 20-55秒：3个价值点
- 55-60秒：引导关注

详见：[examples/短视频脚本示例.md](./examples/短视频脚本示例.md)

---

### 示例2：创作长文

**输入：**
```
主题：马斯克2026访谈解读
平台：公众号
字数：10000字
风格：老司机风格
目标用户：打工人+老板
```

**输出：**
10,847字的深度长文，包含：
- 12个脑洞金句
- 双视角解读
- 实用建议

详见：[examples/长文创作示例.md](./examples/长文创作示例.md)

---

## 📊 效果展示

### 实战案例

**案例1：马斯克访谈解读**
- 字数：10,847字
- 金句：12个
- 阅读时长：35分钟
- 评分：9.5/10

**案例2：短视频爆款真相**
- 字数：8,234字
- 金句：12个
- 阅读时长：25分钟
- 评分：9.0/10

---

## 🎯 适用场景

### 内容创作者

- ✅ 提升内容质量
- ✅ 提高创作效率
- ✅ 增加爆款概率
- ✅ 建立个人品牌

### 企业/团队

- ✅ 标准化创作流程
- ✅ 培训新人
- ✅ 提升团队产出
- ✅ 优化内容策略

### 个人IP

- ✅ 快速起号
- ✅ 稳定输出
- ✅ 多平台分发
- ✅ 商业变现

---

## 🔧 技术栈

- **语言：** Markdown + Python
- **AI支持：** OpenAI, Claude, Gemini
- **平台：** 全平台通用
- **许可证：** MIT License

---

## 📈 版本历史

### v3.1.2 (2026-01-28) - 当前版本

**通用性优化：**
- ✨ 强调SKILL的独立性和通用性
- ✨ 明确可配合任何AI工具使用
- ✨ 添加适用范围说明
- ✨ 优化使用方式分类

### v3.1.1 (2026-01-28)

**高级创作模型：**
- ✨ 用户决策6次判断模型（扩展4次为6次）
- ✨ 私域转化模型（加微信/商业变现）
- ✨ 平台推荐2阶段逻辑（互动者+完播者）
- ✨ 泛粉 vs 精准粉丝策略
- ✨ 高赞视频创作价值线路
- ✨ 用户价值深层逻辑（3种反应+4个条件）
- ✨ 轻松易理解的具体技巧
- ✨ 直播/视频完整转化漏斗（8层）
- ✨ 实战检查清单（完整版）

### v3.1.0 (2026-01-28)

**代码重构：**
- ✨ 代码架构重构（抽象基类、工厂模式）
- ✨ Skill缓存机制（单例模式）
- ✨ 流式输出支持（--stream）
- ✨ API重试机制（指数退避）
- ✨ 配置文件支持（config.yaml）

**内容完善：**
- 📝 补充完整的8种风格详细描述
- 📝 添加统一评分工具模板
- 📝 添加快速检查清单模板
- 🐛 修复内容错误

### v3.0.0 (2026-01-28)

**重大更新：**
- ✨ 新增用户决策4次判断模型
- ✨ 新增全平台内容矩阵
- ✨ 新增短视频创作模块
- ✨ 新增数据分析系统
- 📦 文件大小从16KB增加到45KB

详见：[CHANGELOG.md](./CHANGELOG.md)

---

## 🤝 贡献

我们欢迎所有形式的贡献！

### 如何贡献

1. Fork本项目
2. 创建你的分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

详见：[CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📝 许可证

本项目采用 [MIT License](./LICENSE)

这意味着你可以：
- ✅ 商业使用
- ✅ 修改
- ✅ 分发
- ✅ 私人使用

唯一要求：保留原作者信息

---

## 🙏 致谢

### 感谢

- 50+现象级内容创作者的实践经验
- 所有平台的算法公开信息
- 所有使用和反馈的用户

### 特别感谢

- [@StepFun-AI](https://github.com/stepfun-ai) - 核心开发
- 所有贡献者和支持者

---

## 📞 联系我们

### 问题反馈

- **GitHub Issues：** [提交问题](https://github.com/Sunnyeung369/viral-content-generator/issues)
- **GitHub Discussions：** [参与讨论](https://github.com/Sunnyeung369/viral-content-generator/discussions)

### 社区

- **GitHub：** [项目主页](https://github.com/Sunnyeung369/viral-content-generator)
- **文档：** [在线文档](https://github.com/Sunnyeung369/viral-content-generator/wiki)

---

## 🌟 Star History

如果这个项目对你有帮助，请给我们一个Star！⭐

[![Star History Chart](https://api.star-history.com/svg?repos=Sunnyeung369/viral-content-generator&type=Date)](https://star-history.com/#Sunnyeung369/viral-content-generator&Date)

---

## 📊 项目统计

![GitHub stars](https://img.shields.io/github/stars/Sunnyeung369/viral-content-generator?style=social)
![GitHub forks](https://img.shields.io/github/forks/Sunnyeung369/viral-content-generator?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Sunnyeung369/viral-content-generator?style=social)

![GitHub issues](https://img.shields.io/github/issues/Sunnyeung369/viral-content-generator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Sunnyeung369/viral-content-generator)
![GitHub last commit](https://img.shields.io/github/last-commit/Sunnyeung369/viral-content-generator)

---

## 🎁 福利

### 免费资源

- 📚 完整的方法论文档（126KB+）
- 🎨 8种预设风格模板
- 📝 实战案例（2篇，19000+字）
- 🔧 CLI工具源码
- 📊 数据分析模板

### 持续更新

- 🔄 定期更新方法论
- ✨ 新增更多平台支持
- 📈 优化算法和模型
- 🎓 更多实战案例

---

## 🚀 路线图

### v3.1.0（计划中）

- 🤖 AI辅助创作功能
- ⚙️ 自动化工具
- 📊 数据看板

### v3.2.0（计划中）

- 👥 团队协作功能
- 📁 内容管理系统
- 🔐 权限管理

### v3.3.0（计划中）

- 💰 商业化模块
- 📖 案例库（100+）
- 🎓 在线课程

---

## ❓ 常见问题

### Q1：这个工具适合我吗？

**适合：**
- 内容创作者（个人/团队）
- 短视频创作者
- 自媒体运营者
- 企业新媒体部门
- 想做内容的任何人

**不适合：**
- 完全不做内容的人
- 只想一夜暴富的人

---

### Q2：需要付费吗？

**完全免费！**
- ✅ 所有文档免费
- ✅ 所有模板免费
- ✅ 所有工具免费
- ✅ MIT开源协议

**注意：** 如果使用CLI工具调用AI API，需要自己的API Key（需付费）

---

### Q3：如何获得最佳效果？

**建议：**
1. 先完整阅读核心文档
2. 从一个场景开始实践
3. 严格按照4次判断模型
4. 收集数据并优化
5. 持续学习和迭代

---

### Q4：遇到问题怎么办？

**步骤：**
1. 查看[使用手册](./使用手册.md)
2. 搜索[已有Issues](https://github.com/Sunnyeung369/viral-content-generator/issues)
3. 在[Discussions](https://github.com/Sunnyeung369/viral-content-generator/discussions)提问
4. 创建新的Issue

---

## 💪 开始使用

**现在就开始创作你的爆款内容！**

1. ⭐ Star本项目
2. 📥 Clone到本地
3. 📖 阅读文档
4. ✍️ 开始创作
5. 📊 收集数据
6. 🔄 持续优化

**祝你创作愉快！** 🎉

---

<div align="center">

Made with ❤️ by [Sunnyeung](https://github.com/Sunnyeung369)

[⬆ 回到顶部](#-爆款内容生成器-v30)

</div>
