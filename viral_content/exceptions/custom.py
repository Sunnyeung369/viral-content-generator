"""
自定义异常类

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""


class ViralContentError(Exception):
    """基础异常类"""
    pass


class SkillLoadError(ViralContentError):
    """Skill文件加载错误"""
    pass


class APIError(ViralContentError):
    """API调用错误"""
    pass


class ValidationError(ViralContentError):
    """参数验证错误"""
    pass


class ConfigError(ViralContentError):
    """配置错误"""
    pass


class AccountLoadError(ViralContentError):
    """账号配置加载错误"""
    pass


class OfferLoadError(ViralContentError):
    """产品配置加载错误"""
    pass


class StyleLoadError(ViralContentError):
    """风格配置加载错误"""
    pass


# 兼容旧版命名
ConfigurationError = ConfigError
GenerationError = APIError

FileOperationError = ViralContentError

