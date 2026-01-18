import pathlib
import unittest
import pytest

from ddt import file_data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Chorme_option.Options import chrome_options
from logging_conf.logging_config import logs
from page_object.edit_addrss import EditAddrssPage
from page_object.login_page import LoginPage


class TestMall(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # setUpClass方法是在所有测试方法运行前运行一次，用于初始化测试环境
        chromedriver = pathlib.Path(__file__).parents[1].resolve() / 'chromedriver.exe' # 定位chromedriver.exe文件
        service = Service(str(chromedriver)) # 创建Service对象，用于指定chromedriver.exe文件的路径
        driver = webdriver.Chrome(service=service, options=chrome_options()) # 创建Chrome浏览器实例
        cls.login = LoginPage(driver) # 创建LoginPage对象，用于登录操作
        cls.edit_address = EditAddrssPage(driver) # 创建EditAddrssPage对象，用于编辑地址操作

    @file_data('edit_data.yaml')
    def test_01_login(self,**kwargs): # 测试登录功能
        if 'login' in kwargs:
            self.login.user_login(**kwargs['login']) # 调用LoginPage对象的login方法，进行登录操作
        else:
            logs.info("No login data found in kwargs")
    @file_data('edit_data.yaml')
    def test_02_edit_address(self,**kwargs): # 测试编辑地址功能
        if 'edit_address' in kwargs:
            self.edit_address.user_edit_address(**kwargs['edit_address']) # 调用EditAddrssPage对象的edit_address方法，进行编辑地址操作
        else:
            logs.info("No edit address data found in kwargs")

if __name__ == '__main__':
    unittest.main()