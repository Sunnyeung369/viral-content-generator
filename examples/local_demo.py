"""Run a deterministic demo without an API key."""

from viral_content.core.conversion_funnel import ConversionFunnel, ConversionGoal


def main() -> None:
    topic = "AI 工具让团队少开一半无效会议"
    funnel = ConversionFunnel(ConversionGoal.LEADS)
    print("主题:", topic)
    print("目标: leads")
    print("结构:", funnel.get_content_structure())
    print("CTA 建议:", funnel.get_cta_suggestions()[:2])
    print("质量标准:", funnel.get_quality_standards())
    print("\n这是本地规则演示，不会调用模型，也不会发送任何数据。")


if __name__ == "__main__":
    main()
