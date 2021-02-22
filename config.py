# coding:utf-8
import logging


class Config(object):
    """配置信息"""
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"
    DEBUG = True
    # 默认日志等级
    LOG_LEVEL = logging.DEBUG

class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产环境配置信息"""
    DEBUG = False
    LOG_LEVEL = logging.ERROR


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}