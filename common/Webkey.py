'''
    关键字驱动类：本身是一个类，属于逻辑代码类。
        Selenium的二次封装，将Selenium中常用的操作行为，封装为自定义的函数，来实现自动化测试需求满足。
        在实际测试中，我们需要用的方法其实只占据Selenium很小的一部分，所以我们可以直接将常用操作行为提取
        至自定义的类之中，当需要执行自动化时，直接调用关键字类，就不需要再进行Selenium库的调用了。
        因为实际测试过程可能会出现出乎意料的事情，所以封装关键字类不需要一步到位。后期需要什么再额外添加即可。
        常用操作行为：
            get
            find element
            send keys
            click
            ....
        关键字驱动类属于底层逻辑类，本身没有任何用处，只有在调用的时候才会产生价值。所以属于逻辑代码的范畴
        关键字驱动类，在实际应用的过程中不会单独使用，一定会结合数据驱动，和对应的其他模块来实现调用
        关键字驱动类的模式，可以提供非常好的维护性，让我们可以更加清晰地去知道修改问题代码。
        关键字驱动类的核心底层是由多个不同的模块一同组成的，在实际应用的过程会更加的简洁和方便。
        关键字驱动类的内容是可以随时添加的，不用担心代码是否有不完整的情况出现。
'''
import pathlib
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from Chorme_option.Options import chrome_options
from logging_conf.logging_config import logs


def open_browser(type_):
        # 浏览器调用
        file_service_path = pathlib.Path(__file__).parents[1].resolve() / "chromedriver.exe"
        service = Service(str(file_service_path))
        try:
            if type_ == 'chrome':
                driver = webdriver.Chrome(service=service, options=chrome_options())
            else:
                driver = getattr(webdriver, type_.capitalize())()
            return driver
        except:
            return webdriver.Chrome(service=service)


#关键字驱动
class Webkey():
    def __init__(self,type_):
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(3)

    #访问网页
    def open(self,url):
        self.driver.get(url)

    #定位元素
    def locator(self,by,value):
        return self.driver.find_element(by,value)

    #输入内容
    def input(self,by,value,txt):
        el = self.locator(by,value)
        el.clear()
        el.send_keys(txt)

    #点击元素
    def click(self,by,value):
        self.locator(by,value).click()

    #强制等待
    def wait(self,time_):
        time.sleep(int(time_))

    #关闭网页
    def quit(self):
        self.driver.close()

    #下列框的操作
    def select(self,by,value,txt):
        se = Select(self.locator(by,value))
        se.select_by_visible_text(txt)

    #文本断言
    def assert_text(self,expected,by,value):
        """

        :param expected: 预期值
        :param by: 定位方式
        :param value: 定位值
        :return:
        """
        try:
            reality = self.locator(by,value).text
            assert expected == reality, f"断言失败，预期值为{expected}，实际值为{reality}"
            return True
        except Exception as e:
            logs.error(e)
            return False

webkey = Webkey('chrome')
webkey.open('http://127.0.0.1:8000')
