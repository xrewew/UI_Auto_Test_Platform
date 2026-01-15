"""
    日志配置
"""
import datetime
import os
import pathlib
import logging.config
import time
from logging.handlers import RotatingFileHandler

import colorlog
#对logging.ini进行读取并且封装logger
from conf import setting

# 日志目录
LOG_PATH = setting.FILE_PATH['LOG']
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
    print(f"日志目录创建成功: {LOG_PATH}")

#构造完整的日志文件名,格式为"test.YYYYMMDD.log"
LOG_FILE_NAME = os.path.join(LOG_PATH, f"test.{time.strftime('%Y%m%d')}.log")

#获取logger并进行初始化设置
def get_logger():
    # 读取logging.ini配置文件
    logger_ini_flie = pathlib.Path(__file__).parents[0].resolve() / "logging.ini"
    #使用配置文件初始化---------日志记录器------
    #logging基于配置文件实现对日志的配置：基于logging.config.fileConfig实现
    logging.config.fileConfig(logger_ini_flie,encoding="utf-8")
    #生成日志记录器
    logger = logging.getLogger(__name__)

    # 创建一个RotatingFileHandler实例，用于将日志写入-----------------文件并实现自动轮转
    fh = RotatingFileHandler(filename=LOG_FILE_NAME,mode='a',maxBytes=5242880, backupCount=17,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    # 定义日志格式
    formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d -[%(module)s:%(funcName)s] - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

def clean_logger():
    """处理过期日志文件"""
    now_time = datetime.datetime.now()  # 获取当前时间
    offset_date = datetime.timedelta(days=-30)  # 创建一个表示30天前的时间增量
    before_date = (now_time + offset_date).timestamp()  # 计算出30天前的那个时间点的时间戳
    files = os.listdir(LOG_PATH)  # 列出日志目录下的所有文件
    for file in files:  # 遍历所有文件
        if os.path.splitext(file)[1]:  # 判断文件名是否有扩展名，以此过滤掉文件夹
            filepath = os.path.join(LOG_PATH, file)  # 拼接成完整的文件路径
            file_create_time = os.path.getctime(filepath)  # 获取文件的创建时间戳
            if file_create_time < before_date:  # 如果文件的创建时间早于30天前的时间点
                os.remove(filepath)  # 则删除该文件
                print(f"删除过期日志文件: {filepath}")

#定义一个日志纪录类
class MyLogger():

    def __init__(self): #初始化日志记录器
        clean_logger() #在调用这个类时，自动清理过期的日志文件

    def log(self):
        logger = get_logger() #获取日志记录器
        return logger

logger = MyLogger()
logs = logger.log()