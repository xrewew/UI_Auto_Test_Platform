import logging
import os
import threading

from common.excel_drivel import excel_run, sum_pass_fail
from logging_conf.logging_config import logs
from common.excel_drivel import find_testcase
"""
    程序的主入口，所有一切的程序调用都从这里开始运行的。
"""
"""
        测试用例执行过程中提升效率的方案：
        方案1：
            如果用例数量巨大，可以采取分布式测试框架部署的模式，以主从节点模式实现分布式任务调度。
            通过子节点的负载均衡实现大批用例的并发运行处理。从而实现更有效率的自动化测试执行。
            整体实现通过Selenium Grid来实现配置。主从节点的环境需要保持一致。
        方案2：
            通过多线程的模式来实现用例的并发。只限于单节点的工作机执行。   
            线程与进程：
            程序的运行是基于进程来实现的。线程是进程的子级单位。一个进程可以拥有多个线程。
            在用例执行过程中，把不同的测试用例区分为不同的线程，让不同线程执行不同用例。从而实现多用例并发
            同步与异步：
                默认状态下，程序是基于同步状态来执行的，也就是一个个命令排队执行。效率相对低下
                异步则恰恰相反。
                单个设备的资源是有上限的，所以在进行线程创建的时候，一定要合理使用资源。如果数目太大，可以考虑Selenium Grid
"""

def main():
    """主应用程序逻辑"""
    logs.info("主程序开始运行...")
    cases = find_testcase()
    th = []
    for case in cases:
        print(case)
        thead = threading.Thread(target=excel_run, args=[case]) #创建线程，target指定线程要执行的函数，args指定函数的参数
        th.append(thead) #将线程添加到线程组列表中
    # for t in th:
    #     t.start() #启动线程

    logs.info("主程序运行结束。")


if __name__ == "__main__":
    main()
    # sum_pass_fail()



