#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/9 17:37 
@file: web_submit.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 启动 Chrome 浏览器
browser = webdriver.Chrome()
# 打开指定的网页
browser.get('http:v8.chaoxing.com')
# 找到email元素
input_elem = browser.find_element(By.ID, 'uunnmm')
input_elem.send_keys('15936982275')
time.sleep(5)
passward_button = browser.find_element(By.ID,"pwd")
passward_button.send_keys('c15936982275')
time.sleep(5)
submit_button = browser.find_element(By.ID,"login")
submit_button.click()
time.sleep(500)