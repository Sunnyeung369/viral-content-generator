# Viral Content Generator v4.0 API 文档

> **Python API 和 CLI 使用指南**

---

## 目录

1. [快速开始](#快速开始)
2. [Python API](#python-api)
3. [CLI](#cli)
4. [数据模型](#数据模型)
5. [高级用法](#高级用法)
6. [错误处理](#错误处理)

---

## 快速开始

### 安装

```bash
git clone https://github.com/Sunnyeung369/viral-content-generator.git
cd viral-content-generator
pip install -r requirements.txt
```

### 最简单的使用

```python
from viral_content import ViralContentPipeline

pipeline = ViralContentPipeline()
result = pipeline.run(
    topic="AI正在改变内容创作",
    account="data/accounts/default_account.yaml",
    offer="data/offers/default_offer.yaml",
    style_mix="global:tech_explainer",
    goal="leads",
    platform="xiaohongshu"
)

print(result.content)
```

---

## Python API

### 核心类

#### ViralContentPipeline

主流程编排器，负责协调所有模块完成内容生成。

**初始化**

```python
from viral_content import ViralContentPipeline

pipeline = ViralContentPipeline(config=None)
```

**参数**:
- `config` (Dict[str, Any], optional): 全局配置

**run() 方法**

```python
result = pipeline.run(
    topic: str,
    account: Union[str, Account],
    offer: Union[str, Offer],
    style_mix: Union[str, List[str]],
    goal: Union[str, ConversionGoal],
    platform: Union[str, Platform],
    trend_data: Optional[Union[str, Trend, List[Trend]]] = None,
    config: Optional[GenerationConfig] = None,
) -> GenerationResult
```

**参数说明**:
| 参数 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `topic` | str | 话题/热点描述 | "AI正在改变内容创作" |
| `account` | str/Account | 账号配置或路径 | "data/accounts/ai_consultant.yaml" |
| `offer` | str/Offer | 产品配置或路径 | "data/offers/consulting.yaml" |
| `style_mix` | str/List | 风格组合 | "global:tech_explainer,china:business_savage" |
| `goal` | str/ConversionGoal | 成交目标 | ConversionGoal.LEADS |
| `platform` | str/Platform | 目标平台 | Platform.XIAOHONGSHU |
| `trend_data` | str/Trend/List | 热点数据（可选） | - |
| `config` | GenerationConfig | 生成配置（可选） | - |

**返回**: `GenerationResult` 对象

---

#### PipelineBuilder

Builder模式构建器，提供链式API。

```python
from viral_content import PipelineBuilder, ConversionGoal, Platform

result = (PipelineBuilder()
    .with_account("data/accounts/ai_consultant.yaml")
    .with_offer("data/offers/consulting.yaml")
    .with_styles("global:tech_explainer,china:business_savage")
    .with_goal(ConversionGoal.LEADS)
    .with_platform(Platform.XIAOHONGSHU)
    .generate("AI正在改变内容创作"))
```

**方法**:
| 方法 | 参数 | 说明 |
|------|------|------|
| `with_config()` | config: Dict | 设置全局配置 |
| `with_account()` | account: str/Account | 设置账号 |
| `with_offer()` | offer: str/Offer | 设置产品 |
| `with_styles()` | styles: str/List | 设置风格 |
| `with_goal()` | goal: str/ConversionGoal | 设置成交目标 |
| `with_platform()` | platform: str/Platform | 设置平台 |
| `with_generation_config()` | config: GenerationConfig | 设置生成配置 |
| `build()` | - | 构建Pipeline对象 |
| `generate()` | topic: str | 一步构建并执行 |

---

### 核心模块

#### PromptCompiler

提示词编译器。

```python
from viral_content import PromptCompiler

compiler = PromptCompiler()
prompt = compiler.compile(
    task_info={"topic": "AI工具", "category": "科技"},
    account=account_object,
    offer=offer_object,
    styles=[style_profile1, style_profile2],
    goal=ConversionGoal.LEADS,
    platform=Platform.XIAOHONGSHU
)
```

#### StyleMixer

风格混合器。

```python
from viral_content import StyleMixer

mixer = StyleMixer()

# 获取风格
style = mixer.get_style("global:tech_explainer")

# 列出所有风格
all_styles = mixer.list_styles()

# 搜索风格
results = mixer.search_styles(keyword="科技")

# 混合风格
mixed = mixer.mix_styles(["global:tech_explainer", "china:business_savage"])
```

#### PlatformAdapter

平台适配器。

```python
from viral_content import PlatformAdapter

adapter = PlatformAdapter()

# 适配内容
adapted = adapter.adapt(
    content=original_content,
    platform=Platform.XIAOHONGSHU,
    options={"add_emojis": True}
)

# 获取平台规格
spec = adapter.get_platform_spec(Platform.XIAOHONGSHU)

# 批量适配
multi = adapter.adapt_multi(
    content=original_content,
    platforms=[Platform.XIAOHONGSHU, Platform.DOUYIN]
)
```

#### QualityScorer

质量评分器。

```python
from viral_content import QualityScorer

scorer = QualityScorer()

# 评分所有维度
scores = scorer.score_all(
    content=content,
    account=account_object,
    offer=offer_object,
    goal=ConversionGoal.LEADS,
    platform=Platform.XIAOHONGSHU
)

# 获取建议
suggestions = scorer.get_improvement_suggestions(scores)

# 单独评分
hook_score = scorer.score_hook(content)
```

---

### 热点模块

#### TrendAggregator

热点聚合器。

```python
from viral_content.trends import TrendAggregator, GoogleTrendsSource

aggregator = TrendAggregator()

# 添加数据源
aggregator.add_source(GoogleTrendsSource())

# 获取热点
trends = aggregator.fetch_all(limit=20)

# 过滤热点
filtered = aggregator.filter_by_category(trends, "科技")
```

#### 热点数据源

```python
from viral_content.trends import (
    GoogleTrendsSource,
    TikTokTrendSource,
    DouyinTrendSource,
    XiaohongshuTrendSource
)

# Google Trends
source = GoogleTrendsSource()
trends = source.fetch(limit=20, category="科技")

# TikTok
source = TikTokTrendSource(config={"region": "US", "language": "en"})
trends = source.fetch(limit=20)

# 抖音
source = DouyinTrendSource()
trends = source.fetch(limit=20)

# 小红书
source = XiaohongshuTrendSource()
trends = source.fetch(limit=20)
```

---

## CLI

### 基本用法

```bash
python viral_content_cli_v4.py "你的话题"
```

### 完整参数

```bash
python viral_content_cli_v4.py \
  --topic "你的话题" \
  --account data/accounts/ai_consultant.yaml \
  --offer data/offers/consulting.yaml \
  --style-mix "global:tech_explainer,china:business_savage" \
  --goal leads \
  --platform xiaohongshu \
  --provider openai \
  --model gpt-4o \
  --temperature 0.7 \
  --output outputs/ \
  --save-meta
```

### 参数说明

| 参数 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `--topic` | 话题（必需） | - | "AI正在改变内容创作" |
| `--account` | 账号配置文件 | default_account.yaml | data/accounts/ai_consultant.yaml |
| `--offer` | 产品配置文件 | default_offer.yaml | data/offers/consulting.yaml |
| `--style-mix` | 风格组合 | tech_explainer_global | "global:tech_explainer,china:business_savage" |
| `--goal` | 成交目标 | leads | leads/comments/likes/sales |
| `--platform` | 目标平台 | xiaohongshu | wechat/douyin/tiktok/etc |
| `--provider` | AI提供商 | openai | openai/claude/gemini |
| `--model` | AI模型 | gpt-4o | gpt-4o/claude-3-5-sonnet-20241022 |
| `--temperature` | 温度参数 | 0.7 | 0.0-2.0 |
| `--max-tokens` | 最大token数 | 2000 | 1000-8000 |
| `--output` | 输出目录 | outputs/ | outputs/demo/ |
| `--save-meta` | 保存元数据 | False | - |
| `--trend-file` | 热点数据文件 | - | trends.json |
| `--batch` | 批量模式 | False | - |

### 批量生成

```bash
# 从文件读取多个热点
python viral_content_cli_v4.py \
  --trend-file trends.json \
  --account data/accounts/ai_consultant.yaml \
  --offer data/offers/consulting.yaml \
  --style-mix "global:tech_explainer" \
  --goal leads \
  --platform xiaohongshu,douyin \
  --batch
```

---

## 数据模型

### GenerationResult

生成结果对象。

```python
class GenerationResult:
    content: str              # 生成的内容
    metadata: Dict[str, Any]  # 元数据
    scores: Dict[str, float]  # 评分结果
    suggestions: List[str]    # 优化建议
    platform: Platform        # 目标平台
    goal: ConversionGoal      # 成交目标
```

### Account

账号指纹对象。

```python
class Account:
    name: str                 # 账号名称
    identity: str             # 身份定位
    target_audience: List[str] # 目标用户
    pain_points: List[str]    # 用户痛点
    authority_assets: List[str] # 权威资产
    business_goal: Dict       # 商业目标
    offer_ladder: Dict       # 产品阶梯
    tone_constraints: List[str] # 语气限制
    content_constraints: List[str] # 内容限制
```

### Offer

产品服务对象。

```python
class Offer:
    name: str              # 产品名称
    type: str              # 产品类型
    category: str          # 产品分类
    pricing: Dict          # 价格阶梯
    unique_value_proposition: List[str] # 核心卖点
    conversion_path: Dict   # 转化路径
```

### StyleProfile

风格配置对象。

```python
class StyleProfile:
    id: str                # 风格ID
    name: str              # 风格名称
    category: str          # 风格分类
    style_dna: Dict        # 风格DNA
    hook_patterns: List[str] # 钩子模式
    logic_patterns: List[str] # 逻辑模式
```

### Trend

热点数据对象。

```python
class Trend:
    id: str                # 热点ID
    topic: str             # 话题
    description: str       # 描述
    source: str            # 来源
    url: str               # 链接
    category: TrendCategory # 分类
    keywords: List[str]    # 关键词
    metrics: TrendMetrics  # 指标
    content_snippet: str   # 内容片段
```

### ConversionGoal

成交目标枚举。

```python
class ConversionGoal(Enum):
    LIKES = "likes"        # 高赞内容
    COMMENTS = "comments"  # 高互动内容
    LEADS = "leads"        # 高线索内容
    SALES = "sales"        # 高成交内容
```

### Platform

平台枚举。

```python
class Platform(Enum):
    WECHAT = "wechat"
    XIAOHONGSHU = "xiaohongshu"
    DOUYIN = "douyin"
    TIKTOK = "tiktok"
    WEIBO = "weibo"
    LINKEDIN = "linkedin"
    TWITTER = "twitter"
    ZHIHU = "zhihu"
```

---

## 高级用法

### 自定义配置

```python
from viral_content import get_settings

# 加载配置
settings = get_settings("config.yaml")

# 修改配置
settings.set("generator", "provider", "claude")
settings.set("generator", "temperature", 0.8)

# 获取配置
provider = settings.get("generator", "provider")
```

### 自定义风格

```python
from viral_content import StyleProfile

custom_style = StyleProfile(
    id="my_style",
    name="我的风格",
    category="custom",
    style_dna={
        "tone": "温暖、专业",
        "sentence_rhythm": "短句开场"
    },
    hook_patterns=["你是否也有这种感觉..."]
)
```

### 批量处理

```python
from viral_content import ViralContentPipeline

pipeline = ViralContentPipeline()

# 处理多个话题
topics = ["话题1", "话题2", "话题3"]
results = []

for topic in topics:
    result = pipeline.run(
        topic=topic,
        account="data/accounts/ai_consultant.yaml",
        offer="data/offers/consulting.yaml",
        style_mix="global:tech_explainer",
        goal="leads",
        platform="xiaohongshu"
    )
    results.append(result)
```

### 多平台批量生成

```python
from viral_content import Platform

platforms = [
    Platform.XIAOHONGSHU,
    Platform.DOUYIN,
    Platform.WECHAT
]

results = {}
for platform in platforms:
    result = pipeline.run(
        topic="AI正在改变内容创作",
        account="data/accounts/ai_consultant.yaml",
        offer="data/offers/consulting.yaml",
        style_mix="global:tech_explainer",
        goal="leads",
        platform=platform
    )
    results[platform.value] = result
```

---

## 错误处理

### 异常类型

```python
from viral_content.exceptions import (
    ValidationError,
    GenerationError,
    FileOperationError,
    ConfigurationError
)
```

### 异常处理示例

```python
try:
    result = pipeline.run(...)
except ValidationError as e:
    print(f"参数验证失败: {e}")
except GenerationError as e:
    print(f"内容生成失败: {e}")
except FileOperationError as e:
    print(f"文件操作失败: {e}")
except ConfigurationError as e:
    print(f"配置错误: {e}")
```

---

## 总结

**API 核心价值**：

1. **易用性** - 简单的API，快速上手
2. **灵活性** - 支持各种自定义配置
3. **可扩展性** - 模块化设计，易于扩展
4. **稳定性** - 完善的错误处理

**快速开始三步**：

1. 初始化 Pipeline
2. 调用 run() 方法
3. 获取生成结果

**获取帮助**：
- GitHub: https://github.com/Sunnyeung369/viral-content-generator
- Issues: 提交问题
