#!/usr/bin/env python3
"""
爆款内容生成器 - 命令行工具 v3.0
支持多个AI平台：OpenAI, Claude, Gemini

作者: Sunnyeung
版本: 3.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('viral_content_generator.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 常量定义
SKILL_PATH = Path(__file__).parent / "skill_v3.0.md"
FALLBACK_SKILL_PATH = Path(__file__).parent / "skill.md"
SUPPORTED_PLATFORMS = ['openai', 'claude', 'gemini']
SUPPORTED_STYLES = [
    '老司机风格', '专业导师风格', '故事叙述风格', '数据分析风格',
    '反常识风格', '清单工具风格', '对话问答风格', '诗意哲思风格'
]
MIN_WORD_COUNT = 500
MAX_WORD_COUNT = 20000


class SkillLoadError(Exception):
    """Skill文件加载错误"""
    pass


class APIError(Exception):
    """API调用错误"""
    pass


class ValidationError(Exception):
    """参数验证错误"""
    pass


def load_skill() -> str:
    """
    加载Skill内容
    
    Returns:
        str: Skill文件内容
        
    Raises:
        SkillLoadError: 当Skill文件不存在或无法读取时
    """
    try:
        # 优先加载v3.0版本
        if SKILL_PATH.exists():
            with open(SKILL_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
                logger.info(f"成功加载Skill文件: {SKILL_PATH}")
                return content
        # 回退到v2.0版本
        elif FALLBACK_SKILL_PATH.exists():
            with open(FALLBACK_SKILL_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
                logger.warning(f"使用回退Skill文件: {FALLBACK_SKILL_PATH}")
                return content
        else:
            raise SkillLoadError("找不到Skill文件")
    except Exception as e:
        logger.error(f"加载Skill文件失败: {e}")
        raise SkillLoadError(f"加载Skill文件失败: {e}")


def validate_parameters(
    topic: str,
    style: str,
    word_count: int,
    platform: str
) -> None:
    """
    验证输入参数
    
    Args:
        topic: 文章主题
        style: 写作风格
        word_count: 目标字数
        platform: AI平台
        
    Raises:
        ValidationError: 当参数无效时
    """
    # 验证主题
    if not topic or len(topic.strip()) == 0:
        raise ValidationError("主题不能为空")
    if len(topic) > 200:
        raise ValidationError("主题长度不能超过200字符")
    
    # 验证风格
    if style not in SUPPORTED_STYLES:
        logger.warning(f"使用自定义风格: {style}")
    
    # 验证字数
    if not isinstance(word_count, int):
        raise ValidationError("字数必须是整数")
    if word_count < MIN_WORD_COUNT:
        raise ValidationError(f"字数不能少于{MIN_WORD_COUNT}")
    if word_count > MAX_WORD_COUNT:
        raise ValidationError(f"字数不能超过{MAX_WORD_COUNT}")
    
    # 验证平台
    if platform not in SUPPORTED_PLATFORMS:
        raise ValidationError(f"不支持的平台: {platform}，支持的平台: {SUPPORTED_PLATFORMS}")
    
    logger.info(f"参数验证通过: topic={topic[:20]}..., style={style}, words={word_count}, platform={platform}")


def generate_with_openai(
    topic: str,
    style: str,
    word_count: int,
    api_key: str
) -> str:
    """
    使用OpenAI生成内容
    
    Args:
        topic: 文章主题
        style: 写作风格
        word_count: 目标字数
        api_key: OpenAI API密钥
        
    Returns:
        str: 生成的文章内容
        
    Raises:
        APIError: 当API调用失败时
    """
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=api_key)
        skill_content = load_skill()
        
        prompt = f"""
请用{style}风格，写一篇关于"{topic}"的文章，目标字数：{word_count}字。

要求：
1. 严格按照Skill中的方法论创作
2. 应用用户决策4次判断模型
3. 确保内容质量达到HKR评分标准
4. 字数控制在{word_count}字左右（误差±10%）
"""
        
        logger.info(f"开始调用OpenAI API...")
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": skill_content},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=16384
        )
        
        content = response.choices[0].message.content
        logger.info(f"OpenAI API调用成功，生成内容长度: {len(content)}字")
        
        return content
        
    except ImportError:
        error_msg = "未安装openai库，请运行: pip install openai"
        logger.error(error_msg)
        raise APIError(error_msg)
    except Exception as e:
        error_msg = f"OpenAI API调用失败: {e}"
        logger.error(error_msg)
        raise APIError(error_msg)


def generate_with_claude(
    topic: str,
    style: str,
    word_count: int,
    api_key: str
) -> str:
    """
    使用Claude生成内容
    
    Args:
        topic: 文章主题
        style: 写作风格
        word_count: 目标字数
        api_key: Anthropic API密钥
        
    Returns:
        str: 生成的文章内容
        
    Raises:
        APIError: 当API调用失败时
    """
    try:
        import anthropic
        
        client = anthropic.Anthropic(api_key=api_key)
        skill_content = load_skill()
        
        prompt = f"""
请用{style}风格，写一篇关于"{topic}"的文章，目标字数：{word_count}字。

要求：
1. 严格按照Skill中的方法论创作
2. 应用用户决策4次判断模型
3. 确保内容质量达到HKR评分标准
4. 字数控制在{word_count}字左右（误差±10%）
"""
        
        logger.info(f"开始调用Claude API...")
        
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16384,
            system=skill_content,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        content = message.content[0].text
        logger.info(f"Claude API调用成功，生成内容长度: {len(content)}字")
        
        return content
        
    except ImportError:
        error_msg = "未安装anthropic库，请运行: pip install anthropic"
        logger.error(error_msg)
        raise APIError(error_msg)
    except Exception as e:
        error_msg = f"Claude API调用失败: {e}"
        logger.error(error_msg)
        raise APIError(error_msg)


def generate_with_gemini(
    topic: str,
    style: str,
    word_count: int,
    api_key: str
) -> str:
    """
    使用Gemini生成内容
    
    Args:
        topic: 文章主题
        style: 写作风格
        word_count: 目标字数
        api_key: Google API密钥
        
    Returns:
        str: 生成的文章内容
        
    Raises:
        APIError: 当API调用失败时
    """
    try:
        import google.generativeai as genai
        
        genai.configure(api_key=api_key)
        skill_content = load_skill()
        
        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash-exp',
            system_instruction=skill_content
        )
        
        prompt = f"""
请用{style}风格，写一篇关于"{topic}"的文章，目标字数：{word_count}字。

要求：
1. 严格按照Skill中的方法论创作
2. 应用用户决策4次判断模型
3. 确保内容质量达到HKR评分标准
4. 字数控制在{word_count}字左右（误差±10%）
"""
        
        logger.info(f"开始调用Gemini API...")
        
        response = model.generate_content(prompt)
        content = response.text
        
        logger.info(f"Gemini API调用成功，生成内容长度: {len(content)}字")
        
        return content
        
    except ImportError:
        error_msg = "未安装google-generativeai库，请运行: pip install google-generativeai"
        logger.error(error_msg)
        raise APIError(error_msg)
    except Exception as e:
        error_msg = f"Gemini API调用失败: {e}"
        logger.error(error_msg)
        raise APIError(error_msg)


def save_output(
    content: str,
    output_path: Optional[str] = None,
    topic: str = "article"
) -> str:
    """
    保存生成的内容
    
    Args:
        content: 生成的内容
        output_path: 输出文件路径（可选）
        topic: 文章主题（用于自动命名）
        
    Returns:
        str: 保存的文件路径
    """
    try:
        if output_path:
            file_path = Path(output_path)
        else:
            # 自动生成文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_'))[:30]
            filename = f"{safe_topic}_{timestamp}.md"
            file_path = Path(filename)
        
        # 确保目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 保存文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"内容已保存到: {file_path.absolute()}")
        return str(file_path.absolute())
        
    except Exception as e:
        logger.error(f"保存文件失败: {e}")
        raise


def main() -> int:
    """
    主函数
    
    Returns:
        int: 退出码（0表示成功，非0表示失败）
    """
    parser = argparse.ArgumentParser(
        description='爆款内容生成器 - 命令行工具 v3.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本使用
  %(prog)s "AI工具使用技巧"
  
  # 指定风格和字数
  %(prog)s "AI工具使用技巧" --style 老司机风格 --words 6000
  
  # 使用Claude平台
  %(prog)s "AI工具使用技巧" --platform claude
  
  # 保存到指定文件
  %(prog)s "AI工具使用技巧" -o article.md
  
  # 完整示例
  %(prog)s "AI工具使用技巧" \\
    --style 老司机风格 \\
    --words 6000 \\
    --platform openai \\
    --output article.md

支持的风格:
  """ + "\n  ".join(SUPPORTED_STYLES) + """

环境变量:
  OPENAI_API_KEY      - OpenAI API密钥
  ANTHROPIC_API_KEY   - Anthropic API密钥
  GOOGLE_API_KEY      - Google API密钥
        """
    )
    
    parser.add_argument(
        'topic',
        help='文章主题'
    )
    parser.add_argument(
        '--style',
        default='老司机风格',
        choices=SUPPORTED_STYLES,
        help='写作风格（默认: 老司机风格）'
    )
    parser.add_argument(
        '--words',
        type=int,
        default=6000,
        help=f'目标字数（默认: 6000，范围: {MIN_WORD_COUNT}-{MAX_WORD_COUNT}）'
    )
    parser.add_argument(
        '--platform',
        default='openai',
        choices=SUPPORTED_PLATFORMS,
        help='AI平台（默认: openai）'
    )
    parser.add_argument(
        '--api-key',
        help='API Key（或设置对应的环境变量）'
    )
    parser.add_argument(
        '--output', '-o',
        help='输出文件路径（不指定则自动生成）'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 3.0.0'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='显示详细日志'
    )
    
    args = parser.parse_args()
    
    # 设置日志级别
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    try:
        logger.info("=" * 60)
        logger.info("爆款内容生成器 v3.0 启动")
        logger.info("=" * 60)
        
        # 验证参数
        validate_parameters(args.topic, args.style, args.words, args.platform)
        
        # 获取API Key
        api_key = args.api_key
        if not api_key:
            env_var_map = {
                'openai': 'OPENAI_API_KEY',
                'claude': 'ANTHROPIC_API_KEY',
                'gemini': 'GOOGLE_API_KEY'
            }
            env_var = env_var_map[args.platform]
            api_key = os.getenv(env_var)
            
            if not api_key:
                error_msg = f"错误：请提供API Key或设置环境变量 {env_var}"
                logger.error(error_msg)
                print(f"\n{error_msg}\n", file=sys.stderr)
                return 1
        
        # 生成内容
        print(f"\n正在使用 {args.platform} 生成内容...")
        print(f"主题：{args.topic}")
        print(f"风格：{args.style}")
        print(f"字数：{args.words}")
        print("-" * 60)
        
        generator_map = {
            'openai': generate_with_openai,
            'claude': generate_with_claude,
            'gemini': generate_with_gemini
        }
        
        generator = generator_map[args.platform]
        content = generator(args.topic, args.style, args.words, api_key)
        
        # 保存内容
        output_path = save_output(content, args.output, args.topic)
        
        # 输出结果
        print("\n" + "=" * 60)
        print("✅ 生成成功！")
        print("=" * 60)
        print(f"文件路径: {output_path}")
        print(f"内容长度: {len(content)}字")
        print("=" * 60)
        
        # 如果没有指定输出文件，也打印内容
        if not args.output:
            print("\n内容预览：")
            print("-" * 60)
            print(content[:500] + "..." if len(content) > 500 else content)
            print("-" * 60)
        
        logger.info("任务完成")
        return 0
        
    except ValidationError as e:
        logger.error(f"参数验证失败: {e}")
        print(f"\n❌ 参数错误: {e}\n", file=sys.stderr)
        return 1
        
    except SkillLoadError as e:
        logger.error(f"Skill加载失败: {e}")
        print(f"\n❌ Skill加载失败: {e}\n", file=sys.stderr)
        return 1
        
    except APIError as e:
        logger.error(f"API调用失败: {e}")
        print(f"\n❌ API调用失败: {e}\n", file=sys.stderr)
        return 1
        
    except KeyboardInterrupt:
        logger.warning("用户中断")
        print("\n\n⚠️  用户中断操作\n", file=sys.stderr)
        return 130
        
    except Exception as e:
        logger.exception(f"未预期的错误: {e}")
        print(f"\n❌ 发生错误: {e}\n", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
