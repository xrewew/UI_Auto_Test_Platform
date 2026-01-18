"""
    BasePage:
        基础页面类：
            所有页面类的父类，包含所有页面类共有的方法和属性。用于实现在页面对象层的底层逻辑，主要用于封装各类操作行为
"""
import pathlib
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from Chorme_option.Options import chrome_options
from logging_conf.logging_config import logs

#关键字驱动
class BasePage:
    def __init__(self,driver):
        self.driver = driver
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


