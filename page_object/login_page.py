"""
    LoginPage:
        登录页面类：
            包含登录页面的元素定位和操作方法。用于实现在登录页面的操作逻辑，如输入用户名、密码、点击登录按钮等
            所有的页面对象都可以遵循登录页面业务这个模式，即定义一个页面对象类，继承自BasePage类，然后在类中定义具体的元素定位和操作方法。
"""
import pathlib

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Chorme_option.Options import chrome_options
from base_page.Webkey import BasePage


class LoginPage(BasePage): #直接继承BasePage类
    #1.定义页面的URL:方便对于不同页面的对象的管理，不需要再浪费时间去记url
    url = 'http://127.0.0.1:8000/user/login/'
    #2.定义页面的核心元素:页面中的核心元素也就是需要操作的元素，除此之外其他元素与我们没有任何元素
    username = ('name','username') #元组数据结构，第一个元素是定位方式，第二个元素是定位值
    password = ('name','pwd')
    login_button = ('xpath','/html/body/div[2]/div/div[3]/div[2]/form/input[4]')

    #3.页面的核心业务流程
    def user_login(self,user,pwd):
        self.open(self.url)
        self.input(*self.username,txt=user) #*号的作用是将*username元组解包，将元组中的元素分别作为参数传递给input方法
        self.input(*self.password,txt=pwd)
        self.click(*self.login_button)
        self.wait(1)

