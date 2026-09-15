# 🚀 热点风格成交引擎 v4.0.1

<div align="center">

![Version](https://img.shields.io/badge/version-4.0.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Platform](https://img.shields.io/badge/platform-全平台-orange)

**热点与账号信息 × 风格约束 × 成交目标 = 可测试的内容草案**

[快速开始](#快速开始) • [核心功能](#核心功能) • [使用文档](#使用文档) • [更新日志](./CHANGELOG.md) • [贡献指南](./CONTRIBUTING.md)

</div>

---

## 📖 简介

热点风格成交引擎是一个基于深度研究的**热点风格成交系统**，整合了 **155+ 风格基因卡**，支持热点情报、账号指纹、成交目标、多平台适配的全流程内容作战系统。

### 核心公式

```
热点、账号、目标和平台约束可以组合生成草案；实际表现需要发布后验证
```

### 从 v3.1 到 v4.0 的重大升级

| 特性 | v3.1.2 | v4.0 |
|------|--------|------|
| 定位 | 爆款内容生成器 | 热点风格成交引擎 |
| 风格库 | 8种硬编码风格 | 155+ 外置风格基因卡 |
| 账号配置 | 无 | YAML 账号指纹系统 |
| 成交目标 | 无 | 4种成交目标模式 |
| 热点输入 | 无 | 支持热点情报导入 |
| 平台适配 | 硬编码 | 动态模板系统 |
| 系统提示词 | 单文件 | 模块化编译系统 |

---

## 🎯 核心功能

### 1. 风格基因库（155+ 风格卡）⭐⭐⭐⭐⭐

**分层架构：**
- **A类 - 全球创作者风格（40个）**：科技解释型、商业播客主持、创业Vlog、科技测评等
- **B类 - 国内创作者风格（40个）**：商业毒舌博主、小红书种草、B站知识UP主等
- **C类 - 全球写作者风格（30个）**：科技Newsletter、商业战略洞见、文化评论等
- **D类 - 中文写作者风格（20个）**：商业评论、股市分析、文化随笔等
- **E类 - 成交文案风格（20个）**：AIDA、PAS、故事销售等经典框架

**每个风格基因卡包含：**
- `style_dna`: 语气、句式节奏、词汇偏好
- `hook_patterns`: 钩子模式列表
- `logic_patterns`: 逻辑模式
- `emotion_curve`: 情绪曲线
- `avoid`: 避免事项
- `conversion_fit`: 成交适配性

---

### 2. 账号指纹系统

**账号配置文件结构：**
```yaml
account:
  name: "账号名称"
  identity: "专业定位"
  target_audience: ["目标用户1", "目标用户2"]
  pain_points: ["痛点1", "痛点2"]
  authority_assets: ["权威资产1", "权威资产2"]
  business_goal:
    primary: "主要目标"
    secondary: "次要目标"
  offer_ladder:
    free: "免费诱饵"
    low_ticket: "低价产品"
    mid_ticket: "中价产品"
    high_ticket: "高价服务"
```

**功能：**
- 理解账号定位和目标用户
- 匹配内容风格与账号人设
- 支持多级产品阶梯
- 自动生成账号提示词上下文

---

### 3. 成交目标系统

**4种成交目标模式：**

| 目标 | 适用场景 | 结构特点 | CTA 风格 |
|------|---------|---------|----------|
| **likes** | 互动目标内容 | 观点冲击 + 情绪共鸣 | 认同的点个赞 |
| **comments** | 高互动内容 | 争议问题 + 讨论空间 | 评论区留下观点 |
| **leads** | 高线索内容 | 痛点诊断 + 解决方案预告 | 评论「咨询」获取方案 |
| **sales** | 转化目标内容 | 问题放大 + 稀缺性紧迫感 | 限时优惠，仅剩X名额 |

**每种目标包含：**
- 内容结构建议（开头/主体/结尾字数分配）
- CTA 建议列表
- 质量标准检查清单

---

### 4. 多平台适配系统

**支持平台：**
- 公众号、视频号、小红书、知乎、抖音、B站、微博

**平台适配特点：**
- 字数/时长自动调整
- 特定平台钩子建议
- 互动方式优化

---

### 5. 风格混合引擎

**功能：**
- 支持 1-3 个风格混合
- 自动兼容性检查
- 权重可配置
- 生成混合风格提示词上下文

---

### 6. 热点情报输入

**支持方式：**
- 手动文本输入
- JSON/YAML 文件导入
- 批量热点处理

**热点数据结构：**
```json
{
  "trends": [
    {
      "id": "trend_001",
      "topic": "AI Agent Runtime 崩溃问题",
      "description": "详细描述",
      "source": "来源",
      "metrics": {"热度": 86, "讨论量": 50000}
    }
  ]
}
```

---

## 🚀 快速开始

### 方式1：使用 CLI 工具

**安装依赖**
```bash
pip install -r requirements.txt
```

**基本使用**
```bash
# 列出所有可用风格
python viral_content_cli.py --list-styles

# 基础用法（向后兼容 v3.1）
python viral_content_cli.py "AI Agent Runtime崩溃" --style tech_explainer_global

# v4.0 完整用法
python viral_content_cli.py \
  --topic "AI Agent Runtime崩溃" \
  --account data/accounts/ai_consultant.yaml \
  --offer data/offers/consulting.yaml \
  --goal leads \
  --platform xiaohongshu \
  --style-mix "tech_explainer_global,business_savage_china" \
  --output outputs/
```

**批量生成**
```bash
python viral_content_cli.py \
  --trends-file hot_topics.json \
  --account data/accounts/ai_consultant.yaml \
  --goal leads \
  --output outputs/
```

---

### 方式2：作为 Python 库使用

```python
from viral_content.core import (
    PromptCompiler,
    StyleMixer,
    AccountFingerprint,
    ConversionFunnel,
    ConversionGoal,
)

# 初始化组件
compiler = PromptCompiler()
mixer = StyleMixer()
account = AccountFingerprint.load_default()
funnel = ConversionFunnel(ConversionGoal.LEADS)

# 混合风格
mixed_style = mixer.mix_styles([
    "tech_explainer_global",
    "business_savage_china"
])

# 构建系统提示词
system_prompt = compiler.build_system_prompt(
    topic="2026年AI行业最大趋势",
    style_config=mixed_style,
    account_config=account.to_dict(),
    goal="leads",
    platform="xiaohongshu",
)

print(system_prompt)
```

---

## 📚 使用文档

### 核心文档

| 文档 | 说明 | 适合人群 |
|------|------|---------|
| [README.md](./README.md) | 项目说明 | 所有人 |
| [CHANGELOG.md](./CHANGELOG.md) | 版本历史 | 所有用户 |
| [data/styles/README.md](./data/styles/README.md) | 风格库说明 | 高手 |
| [data/accounts/README.md](./data/accounts/README.md) | 账号配置指南 | 运营者 |
| [data/offers/README.md](./data/offers/README.md) | 产品配置指南 | 商业用户 |

### 数据文件

- `data/styles/` - 155+ 风格基因卡
- `data/accounts/` - 账号指纹模板
- `data/offers/` - 产品服务模板
- `prompts/` - 提示词模板库

---

## 🎓 使用示例

### 示例1：生成高线索内容

**输入：**
```bash
python viral_content_cli.py \
  --topic "AI Agent Runtime崩溃问题" \
  --account data/accounts/ai_consultant.yaml \
  --offer data/offers/consulting.yaml \
  --goal leads \
  --platform xiaohongshu \
  --style-mix "tech_explainer_global,business_savage_china"
```

**输出：**
- 完整的小红书风格内容
- 优化后的 CTA：「评论「AI资料」获取诊断清单」
- 符合 AI 咨询师账号定位
- 针对线索成交目标优化

---

### 示例2：批量生成多平台内容

**输入：**
```bash
python viral_content_cli.py \
  --topic "马斯克2026访谈" \
  --platforms douyin,xiaohongshu,wechat \
  --goal likes \
  --style podcast_host
```

**输出：**
- 抖音短视频脚本（60秒）
- 小红书图文（500-1000字）
- 公众号长文（3000+字）

---

### 示例3：风格混合

```python
from viral_content.core import StyleMixer

mixer = StyleMixer()

# 检查兼容性
compat = mixer.check_compatibility("tech_explainer_global", "business_podcast_host")
print(f"兼容性: {compat}")

# 混合风格
mixed = mixer.mix_styles([
    "tech_explainer_global",
    "business_podcast_host"
], weights={"tech_explainer_global": 0.6, "business_podcast_host": 0.4})

# 获取提示词上下文
context = mixer.get_prompt_context(mixed)
print(context)
```

---

## 🔧 架构设计

### 核心模块

```
viral_content/
├── core/              # 核心引擎
│   ├── prompt_compiler.py      # 提示词编译器
│   ├── style_mixer.py          # 风格混合器
│   ├── account_fingerprint.py  # 账号指纹引擎
│   └── conversion_funnel.py    # 成交漏斗写作器
├── models/            # 数据模型
├── generators/        # AI 生成器
└── utils/             # 工具函数
```

### 数据文件

```
data/
├── styles/            # 155+ 风格基因卡
├── accounts/          # 账号指纹模板
└── offers/            # 产品服务模板
```

---

## 📊 版本历史

### v4.0.0 (2026-06-03) - 重大升级

**架构重构：**
- ✨ 从 v3.1.2 升级到 v4.0
- ✨ 重定位：爆款内容生成器 → 热点风格成交引擎
- ✨ 新增模块化架构（8个核心模块）

**新功能：**
- ✨ 155+ 外置风格基因卡系统
- ✨ 账号指纹配置系统
- ✨ 成交目标输出模式（4种）
- ✨ 热点情报输入系统
- ✨ 多平台动态适配
- ✨ 风格混合引擎
- ✨ 提示词编译器

**数据文件：**
- 📦 5个风格库文件（155+ 风格卡）
- 📦 账号配置模板
- 📦 产品服务模板
- 📦 提示词模板库

**CLI 升级：**
- ✨ 新参数：--account, --offer, --goal, --style-mix
- ✨ 批量生成支持
- ✨ 多平台输出
- ✨ 向后兼容 v3.1 基本用法

### v3.1.2 (2026-01-28)

- ✨ 强调 SKILL 独立性和通用性
- ✨ 明确可配合任何 AI 工具使用

详见：[CHANGELOG.md](./CHANGELOG.md)

---

## 🤝 贡献

我们欢迎所有形式的贡献！

### 如何贡献

1. Fork 本项目
2. 创建你的分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

详见：[CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📝 许可证

本项目采用 [MIT License](./LICENSE)

---

## 🙏 致谢

- 155+ 风格基因卡基于全球顶级创作者的公开风格特征
- 所有平台的算法公开信息
- 所有使用和反馈的用户

---

## 📞 联系我们

- **GitHub Issues：** [提交问题](https://github.com/Sunnyeung369/viral-content-generator/issues)
- **GitHub Discussions：** [参与讨论](https://github.com/Sunnyeung369/viral-content-generator/discussions)

---

## 🌟 Star History

如果这个项目对你有帮助，请给我们一个Star！⭐

[![Star History Chart](https://api.star-history.com/svg?repos=Sunnyeung369/viral-content-generator&type=Date)](https://star-history.com/#Sunnyeung369/viral-content-generator&Date)

---

<div align="center">

Made with ❤️ by [Sunnyeung](https://github.com/Sunnyeung369)

[⬆ 回到顶部](#-热点风格成交引擎-v40)

</div>
