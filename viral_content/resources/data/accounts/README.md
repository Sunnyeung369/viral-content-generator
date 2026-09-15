# 账号指纹库

> **v4.0** - 账号定位和成交目标配置

---

## 目录说明

本目录存放账号指纹配置文件（YAML格式），每个文件定义一个账号的完整画像。

---

## 文件列表

| 文件 | 说明 |
|------|------|
| `default_account.yaml` | 默认账号模板 |
| `ai_consultant.yaml` | AI咨询顾问示例 |
| `crypto_analyst.yaml` | 加密分析师示例 |
| `ecommerce_service.yaml` | 电商服务商示例 |

---

## 配置结构

```yaml
account:
  # 基本信息
  name: "账号名称"
  identity: "一句话定位"

  # 目标用户
  target_audience:
    - "目标用户1"
    - "目标用户2"

  # 用户痛点
  pain_points:
    - "痛点1"
    - "痛点2"

  # 权威资产
  authority_assets:
    - "资产1"
    - "资产2"

  # 商业目标
  business_goal:
    primary: "主要目标"
    secondary: "次要目标"

  # 产品阶梯
  offer_ladder:
    free: "免费诱饵"
    low_ticket: "低价产品"
    mid_ticket: "中价产品"
    high_ticket: "高价服务"

  # 语气限制
  tone_constraints:
    - "限制1"
    - "限制2"

  # 内容限制
  content_constraints:
    - "限制1"
    - "限制2"

  # 平台偏好
  platform_preferences:
    primary: ["主平台1", "主平台2"]
    secondary: ["次平台1"]
```

---

## 如何创建新账号

### 1. 复制模板

```bash
cp data/accounts/default_account.yaml data/accounts/my_account.yaml
```

### 2. 编辑配置

填写你的账号信息，参考 `ai_consultant.yaml` 示例。

### 3. 验证配置

```python
from viral_content import AccountFingerprintLoader

loader = AccountFingerprintLoader()
account = loader.load_account("data/accounts/my_account.yaml")
print(account)
```

---

## 使用方式

### CLI

```bash
python viral_content_cli.py \
  --topic "你的话题" \
  --account data/accounts/my_account.yaml \
  --offer data/offers/my_offer.yaml \
  --goal leads
```

### Python API

```python
from viral_content import PipelineBuilder

result = (PipelineBuilder()
    .with_account("data/accounts/my_account.yaml")
    .with_offer("data/offers/my_offer.yaml")
    .with_styles("global:tech_explainer")
    .with_goal("leads")
    .generate("你的话题"))
```

---

## 注意事项

1. **保持真实性** - 权威资产必须真实可验证
2. **精准定位** - 目标用户描述要具体
3. **明确目标** - 商业目标要清晰可衡量
4. **合规意识** - 内容限制要考虑平台规则

---

## 更多信息

- [账号配置指南](../../docs/账号配置指南.md)
- [API文档](../../docs/API文档.md)
