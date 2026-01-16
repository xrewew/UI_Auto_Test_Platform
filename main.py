import logging

from common.excel_drivel import excel_run, sum_pass_fail
from logging_conf.logging_config import logs
"""
    程序的主入口，所有一切的程序调用都从这里开始运行的。
"""

def main():
    """主应用程序逻辑"""
    logs.info("主程序开始运行...")

    # 调用其他模块的功能
    excel_run()

    logs.info("主程序运行结束。")


if __name__ == "__main__":
    main()
    sum_pass_fail()
