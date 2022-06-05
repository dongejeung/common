# Root Logger sample
# Create Date 2022-06-06
import sys, json, time, math
import logging as log
import pendulum as pdl
import os


# 가장 기본적인 형태의 로거 샘플!
class RootLogger():
    def __init__(self, logger_name):
        self.logger_name = logger_name

    def get_log(self):
        logger = log.getLogger(self.logger_name)
        logger.setLevel(log.INFO)

        # when logger already exists
        if len(logger.handlers) > 0:
            return logger

        now = pdl.now(tz='Asia/Seoul')
        now_str = now.strftime('%Y%m%d%H')

        log_path = f''
        log_file_name = f''

        os.makedirs(log_path, exist_ok=True)

        stream_handler = log.StreamHandler()
        formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        file_handler = log.FileHandler(f'{log_path}/{log_file_name}')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

