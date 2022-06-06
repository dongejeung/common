# Root Logger sample
# Create Date 2022-06-06
import sys, json, time, math
import logging as log
import pendulum as pdl
import os


# 가장 기본적인 형태의 로거 샘플!
class RootLogger():
    # init method
    def __init__(self, log_name, log_path, log_level):
        self.log_name = log_name
        self.log_path = log_path
        self.log_level = log_level

    # get log method
    def get_log(self):
        logger = log.getLogger(self.log_name)
        #logger.setLevel(log.INFO)
        logger.setLevel(self.log_level)

        # when logger already exists
        if len(logger.handlers) > 0:
            return logger

        now = pdl.now(tz='Asia/Seoul')
        now_str = now.strftime('%Y%m%d%H')

        log_path = self.log_path
        log_file_name = self.log_name

        os.makedirs(log_path, exist_ok=True)

        stream_handler = log.StreamHandler()
        formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        file_handler = log.FileHandler(f'{log_path}/{log_file_name}')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

