# 风格基因库 - v4.0

本目录包含 Viral Content Generator v4.0 的风格基因库。

## 设计理念

每个风格都是"风格基因卡"，描述**可观察的风格特征**，而非具体创作者的复刻。

### 风格基因卡结构

```yaml
- id: unique_id
  label: "风格名称"
  category: "风格类别"
  region: "global|china"
  reference_level: "publicly observable style traits only"
  
  style_dna:
    tone: "语气"
    sentence_rhythm: "句式节奏"
    vocabulary: "词汇特征"
    emoji_usage: "表情使用"
    
  hook_patterns:
    - "钩子模式1"
    - "钩子模式2"
    
  logic_patterns:
    - "逻辑模式1"
    
  emotion_curve:
    opening: "开头情绪"
    middle: "中段情绪"
    ending: "结尾情绪"
    
  avoid:
    - "避免事项"
    
  conversion_fit:
    best_for: ["适用场景"]
    cta_style: "行动召唤风格"
```

## 文件说明

- `global_creators.yaml` - 全球创作者风格（40个）
- `china_creators.yaml` - 国内创作者风格（40个）
- `writers_global.yaml` - 全球写作者风格（30个）
- `writers_china.yaml` - 中文写作者风格（20个）
- `copywriting_masters.yaml` - 成交文案风格（20个）

## 使用方式

通过 CLI 的 `--style-mix` 参数组合风格：

```bash
--style-mix "global:tech_explainer,china:business_savage,writer:newsletter_operator"
```

## 注意事项

⚠️ **重要**: 本风格库描述的是"风格特征"和"创作模式"，并非模仿具体创作者的独特表达。
使用时应保持原创性，避免直接复刻任何在世创作者的个人特色。
