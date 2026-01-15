import logging
from logging_conf.logging_config import logs
from common.excel_drivel import daada


def main():
    """主应用程序逻辑"""
    logs.info("主程序开始运行...")

    # 调用其他模块的功能
    print("------------------")
    daada()

    logs.info("主程序运行结束。")


if __name__ == "__main__":
    main()