"""
    浏览器driver
    1. 调用浏览器
    2. 添加option设置才能启动浏览器
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from logging_conf.logging_config import logs

from Chorme_option.Options import chrome_options

# 浏览器调用
service = Service('../chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options()) #添加option设置才能启动浏览器并生效上面的设置

#隐性等待
driver.implicitly_wait(3)

driver.get("https://www.baidu.com/")
logs.info("打开了百度")
driver.find_element(By.ID, "chat-textarea").send_keys("搞比例")
logs.info("在搜索框中输入了搞比例")
time.sleep(3)
driver.close()
