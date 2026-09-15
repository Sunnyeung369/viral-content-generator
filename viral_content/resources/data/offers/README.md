# 产品服务库

> **v4.0** - 产品/服务配置和转化路径

---

## 目录说明

本目录存放产品/服务配置文件（YAML格式），每个文件定义一个完整的产品阶梯和转化路径。

---

## 文件列表

| 文件 | 说明 |
|------|------|
| `default_offer.yaml` | 默认产品模板 |
| `consulting.yaml` | 咨询服务示例 |
| `course.yaml` | 课程产品示例 |
| `lead_magnet.yaml` | 留资磁铁示例 |

---

## 配置结构

```yaml
offer:
  # 基本信息
  name: "产品/服务名称"
  type: "consulting"  # consulting, course, product, service
  category: "分类"

  # 价格阶梯
  pricing:
    free: "$0"
    low_ticket: "$99"
    mid_ticket: "$1999"
    high_ticket: "$30000"

  # 核心卖点
  unique_value_proposition:
    - "卖点1"
    - "卖点2"
    - "卖点3"

  # 成交门槛
  commitment_required:
    time_investment: "时间投入"
    skill_level: "技能要求"
    tools_needed: "所需工具"

  # 目标客户
  ideal_customer_profile:
    - "客户画像1"
    - "客户画像2"

  # 转化路径
  conversion_path:
    step1:
      action: "行动"
      keyword: "关键词"
      next_step: "下一步"

    # ... 更多步骤

  # 信任背书
  social_proof:
    testimonials: []
    case_studies: []
```

---

## 产品类型

### consulting（咨询服务）

- 一对一或一对多咨询
- 按小时或按项目收费
- 高客单价，高服务

### course（课程产品）

- 标准化教学内容
- 录播或直播
- 中客单价，可规模化

### product（实物/数字产品）

- 标准化产品
- 一次性销售
- 低客单价，高销量

### service（服务产品）

- 标准化服务包
- 按次或按周期收费
- 中客单价

---

## 如何创建新产品

### 1. 复制模板

```bash
cp data/offers/default_offer.yaml data/offers/my_offer.yaml
```

### 2. 编辑配置

填写你的产品信息，参考 `consulting.yaml` 示例。

### 3. 验证配置

```python
from viral_content import AccountFingerprintLoader

loader = AccountFingerprintLoader()
offer = loader.load_offer("data/offers/my_offer.yaml")
print(offer)
```

---

## 转化路径设计

### 标准转化路径

```
免费诱饵 → 低价产品 → 中价产品 → 高价服务
```

### 社群转化路径

```
关注公众号 → 加微信 → 进社群 → 购买产品
```

### 咨询转化路径

```
内容触达 → 留资 → 免费诊断 → 付费咨询
```

---

## 使用方式

### CLI

```bash
python viral_content_cli_v4.py \
  --topic "你的话题" \
  --account data/accounts/my_account.yaml \
  --offer data/offers/my_offer.yaml \
  --goal sales
```

### Python API

```python
from viral_content import PipelineBuilder

result = (PipelineBuilder()
    .with_account("data/accounts/my_account.yaml")
    .with_offer("data/offers/my_offer.yaml")
    .with_goal("sales")
    .generate("你的话题"))
```

---

## 注意事项

1. **明确价值** - 核心卖点要清晰具体
2. **合理定价** - 价格阶梯要有梯度
3. **降低门槛** - 免费诱饵要有吸引力
4. **合规宣传** - 避免过度承诺和虚假宣传

---

## 更多信息

- [API文档](../../docs/API文档.md)
- [成交目标演示](../../examples/v4_conversion_demo.md)
