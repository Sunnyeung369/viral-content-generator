"""Run a deterministic demo without an API key."""

from viral_content.core.conversion_funnel import ConversionFunnel, ConversionGoal


def main() -> None:
    topic = "AI 工具让团队少开一半无效会议"
    funnel = ConversionFunnel(ConversionGoal.LEADS)
    guidance = funnel.get_writing_guidance()
    print("主题:", topic)
    print("目标: leads")
    print("开头建议:", guidance["opening"])
    print("主体建议:", guidance["body"])
    print("结尾建议:", guidance["closing"])
    print("\n这是本地规则演示，不会调用模型，也不会发送任何数据。")


if __name__ == "__main__":
    main()
