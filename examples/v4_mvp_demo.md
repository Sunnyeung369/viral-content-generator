# Viral Content Generator v4.0 MVP 演示

> **演示目标**: 展示 v4.0 的核心功能 - 从热点到高成交内容的完整流程

---

## 场景设定

**账号定位**: AI 效率咨询顾问
**目标用户**: 职场人士、自由职业者、内容创作者
**成交目标**: 获取咨询线索 (leads)
**目标平台**: 小红书

---

## 第一步：准备配置

### 1. 账号配置 (`data/accounts/ai_consultant.yaml`)

```yaml
account:
  name: "AI效率顾问"
  identity: "专注AI工具落地的实战顾问"
  target_audience:
    - "职场人士（想用AI提升效率）"
    - "内容创作者（用AI辅助创作）"
    - "自由职业者（用AI放大产出）"
  pain_points:
    - "知道AI有用，但不知道怎么用"
    - "工具太多，不知道从哪开始"
    - "学了一堆工具，还是不会工作流设计"
  authority_assets:
    - "3年AI实战经验"
    - "服务过50+企业客户"
    - "累计学员2000+"
  business_goal:
    primary: "获取咨询线索"
    secondary: "推广付费课程"
  tone_constraints:
    - "实战派，说人话"
    - "有干货不枯燥"
    - "能落地执行"
```

### 2. 产品配置 (`data/offers/consulting.yaml`)

```yaml
offer:
  name: "AI效率提升咨询"
  type: "consulting"
  pricing:
    free: "免费工具清单"
    low_ticket: "¥199"
    mid_ticket: "¥2999"
    high_ticket: "¥15000"
  unique_value_proposition:
    - "不只教工具，更教你设计AI工作流"
    - "针对你的具体场景定制方案"
    - "一对一辅导，确保落地"
```

---

## 第二步：准备热点话题

### 手动输入热点（JSON格式）

```json
{
  "trends": [
    {
      "id": "trend_001",
      "topic": "Claude发布新功能，可以分析文档",
      "description": "Claude AI推出文档分析功能，支持上传PDF、Word等文件进行分析",
      "source": "Twitter",
      "url": "https://twitter.com/...",
      "category": "科技",
      "keywords": ["Claude", "AI", "文档分析"],
      "metrics": {
        "热度": 85,
        "讨论量": 10000
      }
    }
  ]
}
```

---

## 第三步：运行生成（代码示例）

### Python API 方式

```python
from viral_content import (
    ViralContentPipeline,
    PipelineBuilder,
    ConversionGoal,
    Platform
)

# 方式1: 使用 Pipeline
pipeline = ViralContentPipeline()

result = pipeline.run(
    topic="Claude发布新功能，可以分析文档",
    account="data/accounts/ai_consultant.yaml",
    offer="data/offers/consulting.yaml",
    style_mix="global:tech_explainer",
    goal=ConversionGoal.LEADS,
    platform=Platform.XIAOHONGSHU
)

print(result.content)
print(result.scores)

# 方式2: 使用 PipelineBuilder
result = (PipelineBuilder()
    .with_account("data/accounts/ai_consultant.yaml")
    .with_offer("data/offers/consulting.yaml")
    .with_styles("global:tech_explainer")
    .with_goal(ConversionGoal.LEADS)
    .with_platform(Platform.XIAOHONGSHU)
    .generate("Claude发布新功能，可以分析文档"))
```

### CLI 方式

```bash
python viral_content_cli.py \
  --topic "Claude发布新功能，可以分析文档" \
  --account data/accounts/ai_consultant.yaml \
  --offer data/offers/consulting.yaml \
  --style-mix "global:tech_explainer" \
  --goal leads \
  --platform xiaohongshu \
  --output outputs/demo/
```

---

## 第四步：生成结果示例

### 标题建议
- "Claude偷偷更新了！这个功能太实用了"
- "打工人必看：Claude新功能让你效率翻倍"
- "终于等到你！Claude可以读文档了"

### 内容正文（小红书风格）

```
姐妹们！Claude刚刚偷偷更新了一个功能，我试了一下，真的太香了！🔥

现在可以直接上传PDF、Word这些文档给它分析，不用再复制粘贴了。

我做了个测试，上传了一份50页的行业报告，它不仅总结了核心观点，还给出了我没想到的分析角度。这在之前需要我花2小时才能做完！

如果你是：
👉 做市场分析的：可以快速提炼报告重点
👉 做学术研究的：可以快速梳理文献
👉 做内容创作的：可以快速提炼素材

用起来很简单，3步就会：
1. 打开Claude
2. 点击附件图标上传文件
3. 问你想了解的问题

我整理了一份《AI文档分析实战指南》，包含10个常用提示词模板，想要的姐妹评论区扣「文档」自取～❤️

#AI工具 #效率提升 #Claude #打工人必备
```

---

## 第五步：评分结果

### 质量评分

| 维度 | 得分 | 说明 |
|------|------|------|
| 钩子评分 | 8.5/10 | "Claude偷偷更新"制造好奇心 |
| 信任评分 | 7.5/10 | 展示实际使用体验 |
| 价值评分 | 8.0/10 | 提供可操作的方法 |
| 互动评分 | 9.0/10 | 评论区扣关键词引导互动 |
| 转化评分 | 8.5/10 | 免费资料作为诱饵 |
| **综合得分** | **8.3/10** | 良好 |

### 优化建议

1. **可以增加**：具体的使用截图（视觉化更强）
2. **可以补充**：与其他AI工具的对比（增加价值感）
3. **可以优化**：结尾可以加一句紧迫感（"资料限前100名"）

---

## 关键功能展示

### 1. 风格混合

```python
# 混合多种风格
style_mix = "global:tech_explainer,china:business_savage"
result = pipeline.run(..., style_mix=style_mix)
```

### 2. 多平台适配

```python
# 一键生成多平台版本
platforms = [Platform.XIAOHONGSHU, Platform.DOUYIN, Platform.WECHAT]
for platform in platforms:
    result = pipeline.run(..., platform=platform)
```

### 3. 批量生成

```python
# 批量处理多个热点
trends = [trend1, trend2, trend3]
results = pipeline.run_batch(trends=trends, ...)
```

---

## 完整工作流图示

```
┌─────────────────┐
│   输入热点话题    │
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  加载账号配置    │ ← data/accounts/*.yaml
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  加载产品配置    │ ← data/offers/*.yaml
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  加载风格配置    │ ← data/styles/*.yaml
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  编译提示词      │ ← PromptCompiler
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  AI生成内容     │ ← OpenAI/Claude/Gemini
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  质量评分优化   │ ← QualityScorer
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│  平台格式适配   │ ← PlatformAdapter
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│   输出内容包    │
└─────────────────┘
```

---

## 常见问题

### Q1: 如何自定义风格？

编辑 `data/styles/global_creators.yaml`，添加你的风格卡：

```yaml
styles:
  - id: my_custom_style
    label: "我的风格"
    category: "custom"
    style_dna:
      tone: "你的语气"
      sentence_rhythm: "你的句子节奏"
    hook_patterns:
      - "你的钩子模式1"
      - "你的钩子模式2"
```

### Q2: 如何批量生成？

```python
from viral_content.trends import GoogleTrendsSource

# 获取热点
source = GoogleTrendsSource()
trends = source.fetch(limit=10)

# 批量生成
results = pipeline.run_batch(
    trends=trends,
    account="data/accounts/ai_consultant.yaml",
    offer="data/offers/consulting.yaml",
    style_mix="global:tech_explainer",
    goal=ConversionGoal.LEADS,
    platforms=[Platform.XIAOHONGSHU, Platform.DOUYIN]
)
```

### Q3: 如何使用不同的AI模型？

```python
config = GenerationConfig(
    provider="claude",  # 或 "gemini"
    model="claude-3-5-sonnet-20241022",
    temperature=0.7
)
result = pipeline.run(..., config=config)
```

---

## 总结

v4.0 MVP 核心价值：

1. **热点驱动** - 实时捕捉热点话题
2. **账号定位** - 保持内容一致性
3. **成交导向** - 每篇内容都有转化目标
4. **风格可组** - 155+风格基因自由组合
5. **多平台适配** - 一次生成，多平台使用
6. **质量保障** - 内置评分系统确保质量

**开始使用**: `python viral_content_cli.py --help`
