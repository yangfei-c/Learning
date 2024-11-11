#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/9 17:20 
@file: web_click.py
@project: ReLearn
@email:ccc420513@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 启动 Chrome 浏览器
browser = webdriver.Chrome()
# 检查 browser 对象的类型（通常用于调试）
print(type(browser))
# 打开指定的网页
browser.get('http://inventwithpython.com')
# 使用新的定位方法找到链接元素CRediT authorship contribution statement
link_elem = browser.find_element(By.LINK_TEXT, 'Blog')
# 检查 link_elem 对象的类型（通常用于调试）
print(type(link_elem))
# 点击链接
link_elem.click()
time.sleep(10000)