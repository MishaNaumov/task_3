from logging_test.logger_config import LoggerConfig
import logging


class Logger:
    def __init__(self):
        self.config = LoggerConfig.logger_config_info()

    @staticmethod
    def info(param):
        logging.info(param)
