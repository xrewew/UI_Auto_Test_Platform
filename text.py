from selenium.webdriver.common.by import By

from common.Webkey import Webkey

browser = Webkey('chrome')
browser.open('http://baidu.com')
browser.input(By.ID,'chat-textarea','你好')
