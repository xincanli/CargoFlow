import logging
import os
import time
from functools import wraps

class Logger:
    def __init__(self, log_name="BD.log"):
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, log_name)
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger


logger = Logger().get_logger()


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        case_name = None

        # 遍历所有参数，找 dict 里有 name 的
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, dict) and "name" in arg:
                case_name = arg["name"]
                break

        if case_name:
            logger.info(f"开始执行用例：{case_name}")
        else:
            logger.info(f"开始执行函数：{func.__name__}")

        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            if case_name:
                logger.info(f"用例 {case_name} 执行成功")
            else:
                logger.info(f"函数 {func.__name__} 执行成功")
            return result
        finally:
            elapsed = time.time() - start_time
            logger.info(f"执行耗时: {elapsed:.3f} 秒")

    return wrapper

