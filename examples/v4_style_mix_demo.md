# 风格混合演示

> **演示目标**: 展示如何组合多种风格基因创造独特内容风格

---

## 风格混合原理

风格不是模板，而是"风格基因"的组合。就像调色板：

```
红色 + 蓝色 = 紫色
```

同理：

```
"科技解释型" + "商业毒舌" = "犀利科技评论风格"
```

---

## 单一风格示例

### 风格1: 科技解释型 (tech_explainer_global)

**特征**：
- 语气：清晰、兴奋、未来感
- 结构：短句开场 → 中句解释 → 结尾升维
- 钩子：新技术正在改变...

**示例输出**：
```
你可能没注意到，AI正在悄悄改变我们的工作方式。

昨天我试了一下Claude的新功能，它可以直接分析PDF文档了。这听起来没什么，但想想看：以前你需要花2小时读完的行业报告，现在2分钟就能得到核心观点。

这不仅是效率提升，更是工作方式的重新定义。
```

---

### 风格2: 商业毒舌 (business_savage_china)

**特征**：
- 语气：犀利、直接、讽刺但有干货
- 结构：金句密集，短促有力
- 钩子：让我说句难听的...

**示例输出**：
```
让我说句难听的：还在用老方式做内容的人，迟早被淘汰。

时代变了！AI一天生成100篇内容，你还在那儿憋标题？

不是你不努力，是你用错了方法。把时间花在AI能做的事上，那是对你最大的浪费。
```

---

## 双风格混合示例

### 科技解释 + 商业毒舌 = 犀利科技评论

**风格组合**：`"tech_explainer_global,business_savage_china"`

**混合效果**：
- 保留科技感的清晰逻辑
- 加入商业毒舌的犀利表达
- 形成独特的"硬核科技评论"风格

**示例输出**：
```
AI正在偷走你的工作，你却还在刷抖音？

让我说句难听的：Claude刚出的文档分析功能，那些"资深分析师"再不学习就要失业了。50页的行业报告，AI 2分钟提炼核心观点，你还要熬2个通宵？

这不是效率问题，这是生存问题。要么驾驭AI，要么被AI淘汰。

想活命？先把文档上传试试。
```

---

### 科技解释 + Newsletter作者 = 深度科技周刊

**风格组合**：`"tech_explainer_global,tech_newsletter_daily"`

**混合效果**：
- 科技感的兴奋语气
- Newsletter的系统化结构
- 形成深度科技内容

**示例输出**：
```
## 本周观察

Claude发布文档分析功能，这可能是我今年见过最实用的更新。

## 深度分析

表面上这只是"可以上传PDF"的功能，但背后是对长文本理解能力的突破。我测试了几个场景：

1. 行业报告分析：准确率85%+
2. 学术文献梳理：结构清晰
3. 合同审查：风险点识别到位

## 实用建议

如果你是知识工作者，这个功能值得深入探索。我整理了10个实战提示词，下周分享给会员。
```

---

## 三风格混合示例

### 科技 + 商业 + 写作者 = 全方位科技商业评论

**风格组合**：`"tech_explainer_global,business_savage_china,tech_newsletter_daily"`

**混合效果**：
- 科技：前沿趋势感知
- 商业：犀利商业洞察
- 写作：深度系统表达

**示例输出**：
```
## 本周大事

Claude悄悄更新了文档分析功能，而90%的人还在用老方法死磕。

## 为什么这很重要

让我说句难听的：那些靠"人工整理报告"吃饭的顾问们，你们的护城河正在崩塌。

我做了个对比测试：
- 人工分析50页报告：2小时，准确率70%
- Claude分析：2分钟，准确率85%

这不仅是时间差，是能力维度的碾压。

## 商业机会

对于懂得用AI的人，这是新的套利窗口：
1. 快速响应客户咨询
2. 批量处理行业信息
3. 降低服务成本，提高利润率

## 行动建议

别再等了，明天就去试试。不会用的，下周会员课我详细讲。
```

---

## 风格混合规则

### 1. 最大混合数

系统限制最多混合 3 个风格（避免风格混乱）

```python
# ✅ 正确
style_mix = "style1,style2"

# ❌ 错误（超过3个）
style_mix = "style1,style2,style3,style4"
```

### 2. 风格兼容性

某些风格组合更自然：

```
科技类 × 商业类 = ✅ 自然
科技类 × 生活方式类 = ⚠️ 需谨慎
商业类 × 成交文案类 = ✅ 自然
```

### 3. 主次风格

可以指定主风格和辅助风格：

```python
# 主风格在前，辅助风格在后
style_mix = "tech_explainer_global:0.7,business_savage_china:0.3"
```

---

## 实用风格组合推荐

### 科技博主常用组合

```python
# 1. 犀利科技评论
"tech_explainer_global,business_savage_china"

# 2. 深度科技分析
"tech_explainer_global,tech_newsletter_daily"

# 3. 实用工具测评
"tech_explainer_global,copywriting_value_first"
```

### 商业博主常用组合

```python
# 1. 商业故事讲述
"business_savage_china,copywriting:story_sales"

# 2. 商业毒舌点评
"business_savage_china,copywriting:pas"

# 3. 商业深度分析
"business_savage_china,writers_global:business_strategy"
```

### 生活方式博主常用组合

```python
# 1. 生活美学分享
"china:lifestyle_aesthetic,writers_global:productivity"

# 2. 实用生活技巧
"china:lifestyle_aesthetic,copywriting:bab"
```

---

## 自定义风格

### 创建风格卡

在 `data/styles/global_creators.yaml` 中添加：

```yaml
styles:
  - id: my_unique_voice
    label: "我的独特风格"
    category: "custom"
    region: "custom"

    style_dna:
      tone: "温暖、专业、略带幽默"
      sentence_rhythm: "短句开场，长句展开，结尾呼应"
      vocabulary: "日常词汇+专业术语适度混合"

    hook_patterns:
      - "你是否也有这种感觉..."
      - "今天想分享一个秘密"
      - "这件事改变了我对XX的看法"

    logic_patterns:
      - "个人故事 → 通用道理 → 行动建议"

    emotion_curve:
      opening: "共鸣"
      middle: "好奇"
      ending: "行动冲动"
```

---

## 代码示例

### 使用风格混合

```python
from viral_content import (
    PipelineBuilder,
    ConversionGoal,
    Platform
)

result = (PipelineBuilder()
    .with_account("data/accounts/ai_consultant.yaml")
    .with_offer("data/offers/consulting.yaml")
    .with_styles("tech_explainer_global,business_savage_china")
    .with_goal(ConversionGoal.LEADS)
    .with_platform(Platform.XIAOHONGSHU)
    .generate("AI工具正在改变内容创作"))
```

### 批量测试不同风格组合

```python
from viral_content import StyleMixer

mixer = StyleMixer()

# 获取所有可用风格
all_styles = mixer.list_styles()

# 测试不同组合
combinations = [
    ["tech_explainer_global"],
    ["tech_explainer_global", "business_savage_china"],
    ["tech_explainer_global", "business_savage_china", "tech_newsletter_daily"]
]

for styles in combinations:
    result = pipeline.run(..., style_mix=",".join(styles))
    print(f"\n=== {', '.join(styles)} ===\n")
    print(result.content[:500])
```

---

## 总结

**风格混合的核心价值**：

1. **打破模板化** - 不再是死板的模板
2. **保持一致性** - 风格基因确保内容一致
3. **灵活组合** - 根据场景自由组合
4. **持续进化** - 可以不断添加新风格

**155个风格基因，无限组合可能**

开始创造你独特的声音吧！
