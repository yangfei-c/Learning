#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/12 15:33 
@file: wjx_by_select_time.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

# 设置问卷填写的目标时间 (24 小时格式，例如晚上 8 点)
target_time = "16:48:01"

# 启动 Chrome 浏览器
browser = webdriver.Chrome()

# 等待到指定时间
print(f"等待到指定时间 {target_time} 开始填写表单...")
while True:
    # 获取当前时间
    current_time = datetime.now().strftime("%H:%M:%S")
    # 如果当前时间达到了目标时间
    if current_time == target_time:
        print("时间已到，开始填写表单...")
        break
    # 每隔 10 秒检查一次时间
    time.sleep(1)

# 打开指定的网页
browser.get('https://www.wjx.cn/vm/YuyJRi9.aspx')

try:
    # 查找并填写问卷字段
    input_elem1 = browser.find_element(By.ID, 'q1')
    input_elem1.send_keys('陈飞阳')

    input_elem2 = browser.find_element(By.ID, "q2")
    input_elem2.send_keys('202430310006')

    input_elem3 = browser.find_element(By.ID, 'q3')
    input_elem3.send_keys('信息与通信工程1班')

    input_elem4 = browser.find_element(By.ID, "q4")
    input_elem4.send_keys('15936982275')

    # 提交问卷
    submit = browser.find_element(By.ID, "SubmitBtnGroup")
    submit.click()

    print("表单已填写并提交")
    time.sleep(10)

finally:
    # 关闭浏览器
    browser.quit()