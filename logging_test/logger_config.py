import logging


class LoggerConfig:
    @staticmethod
    def logger_config_info():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='my_logging.log',
                                      encoding='utf-8')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(levelname)s (%(asctime)s): %(message)s')
        handler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(handler)
        return logger
