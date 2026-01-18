from symtable import Class
"""
    浏览器Options 设置
"""
from selenium import webdriver


def chrome_options():
    # 如果想要设置浏览器，则需要导入Options类后创建Options对象
    options = webdriver.ChromeOptions()

    # 页面在载策略
    options.page_load_strategy = 'normal'

    # 无头模式：浏览器不以窗口形式打开,而是在后台运行，可以减少浏览器的资源占用
    # options.add_argument('--headless')
    # #OPTION中最常用的两种设置项修改方法
    # options.add_argument()
    # options.add_experimental_option()
    # # 关闭沙盒模式
    # options.add_argument('--no-sandbox')
    # 关掉控制台多余的日志信息,并关掉浏览器自动化控制警告
    options.add_experimental_option("excludeSwitches", ["enable-logging_conf","enable-automation"])
    # 窗口最大化
    # options.add_argument('--start-maximized')
    # 指定窗口位置
    options.add_argument('--window-position=700,200')
    # 指定窗口大小
    options.add_argument('--window-size=1800,1300')

    # 账号密码管理：浏览器帐号密码管理窗口提示关闭
    prefs = {"credentials-enable-service": False,
             "profile.password_manager_enabled": False
             }
    options.add_experimental_option("prefs", prefs)
    #
    # """
    #     selenium 启动的浏览器默认是非登录状态状态的。计算机通过浏览器来访问系统时，会默认加载部分可被缓存的数据到缓存文件当中
    #     Selenium 启动的浏览器默认是非登录状态状态的，是不会加载本地缓存文件的，所以可以理解为一个干干净净的全新的浏览器
    #         1.第一次访问某个域名执行登录时，一定会要求有验证码
    #         2.无法将需要读取的缓存数据及时加载，导致页面加载速度相对会更慢一些
    #     自动化测试不处理验证码，如果实际工作中有验证码的出现，记得联系开发取消验证码或者提供万能验证密码
    #     Selenium 可以考虑通过加载本地缓存文件的方式来提高页面加载速度
    # """
    # # 加载本地缓存文件 浏览器查询本地缓存路径：chrome://version/ 加载本地缓存文件，需要关闭全部浏览器后才能执行自动化代码
    # options.add_argument(r"--user-data-dir=C:\Users\Xie-Xixin\AppData\Local\Google\Chrome\User Data")

    # 保持浏览器打开,因为浏览器打开后会自动关闭,所以需要设置保持浏览器打开
    options.add_experimental_option("detach", True)
    # 进一步去除控制台多余日志信息,如果去除了，会导致一些错误信息无法打印出来
    options.add_argument("--log-level=3")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-certificate-error")


    return options
