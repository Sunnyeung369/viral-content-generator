# 热点数据配置

> **v4.0** - 热点源配置和禁止话题

---

## 目录说明

本目录存放热点数据相关配置文件。

---

## 文件列表

| 文件 | 说明 |
|------|------|
| `banned_topics.yaml` | 禁止话题配置 |

---

## 禁止话题配置

### 结构说明

```yaml
# 绝对禁止话题（触碰即拒绝）
absolutely_banned:
  - 色情低俗
  - 暴力恐怖
  - 违法犯罪
  # ...

# 高风险话题（需要人工审核）
high_risk:
  - category: 政治敏感
    keywords: [...]
    note: "说明"

# 需谨慎处理的话题
handle_with_care:
  - category: 医疗健康
    requirements: [...]
```

### 话题分类

#### 绝对禁止
- 色情低俗
- 暴力恐怖
- 违法犯罪
- 毒品赌博
- 自残自杀
- 极端主义
- 恐怖主义

#### 高风险
- 政治敏感
- 宗教极端
- 民族矛盾
- 群体对立

#### 需谨慎处理
- 医疗健康（需资质）
- 金融投资（需风险提示）
- 教育培训（避免夸大）
- 法律咨询（需专业提示）

---

## 热点数据源

v4.0 支持 4 个热点数据源：

### 1. Google Trends
```python
from viral_content.trends import GoogleTrendsSource

source = GoogleTrendsSource()
trends = source.fetch(limit=20)
```

### 2. TikTok
```python
from viral_content.trends import TikTokTrendSource

source = TikTokTrendSource(config={"region": "US"})
trends = source.fetch(limit=20)
```

### 3. 抖音
```python
from viral_content.trends import DouyinTrendSource

source = DouyinTrendSource()
trends = source.fetch(limit=20)
```

### 4. 小红书
```python
from viral_content.trends import XiaohongshuTrendSource

source = XiaohongshuTrendSource()
trends = source.fetch(limit=20)
```

---

## 热点数据格式

### 手动输入格式

```json
{
  "trends": [
    {
      "id": "trend_001",
      "topic": "AI Agent Runtime 崩溃问题",
      "description": "2026年6月初，多家AI Agent平台出现Runtime崩溃",
      "source": "Twitter/X",
      "url": "https://twitter.com/...",
      "metrics": {
        "热度": 86,
        "讨论量": 50000
      },
      "keywords": ["AI", "Agent", "Runtime", "崩溃"],
      "category": "技术"
    }
  ]
}
```

### CLI 使用

```bash
python viral_content_cli_v4.py \
  --topic "你的话题" \
  --trend-file trends.json \
  --batch
```

---

## 合规检查

系统会自动检查生成内容是否涉及禁止话题：

```python
from viral_content.scorers import ComplianceScorer

scorer = ComplianceScorer()
result = scorer.score_compliance(content, banned_topics_file="data/trends/banned_topics.yaml")
```

---

## 注意事项

1. **遵守法律法规** - 内容必须符合当地法律
2. **尊重平台规则** - 遵守各平台内容规范
3. **保护用户权益** - 不做虚假宣传
4. **履行社会责任** - 传播积极正能量

---

## 更多信息

- [合规检查模板](../../prompts/compliance.md)
- [API文档](../../docs/API文档.md)
