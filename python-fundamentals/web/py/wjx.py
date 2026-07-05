#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/12 15:05 
@file: wjx.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
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
time_wait=0.1
# 启动 Chrome 浏览器
browser = webdriver.Chrome()
# 打开指定的网页
browser.get('https://www.wjx.cn/vm/YuyJRi9.aspx ')

try:
    # 尝试直接查找问卷字段 q1 是否可见
    input_elem1 = browser.find_element(By.ID, 'q1')
    print("问卷已开放，直接填写。")

except:
    # 如果找不到字段 q1，则进入等待“立即开始”按钮的循环
    print("问卷暂未开放，开始等待开放...")
    while True:
        try:
            start_button = browser.find_element(By.XPATH, '/html/body/div[2]/form/div[10]/div[2]/div[2]/div/div/a')
            start_button.click()
            print("已点击'立即开始'按钮。")
            break  # 找到并点击后退出循环
        except:
            print(f"等待问卷开放，{time_wait}秒后重试...")
            time.sleep(time_wait)

input_elem1 = browser.find_element(By.ID, 'q1')
input_elem1.send_keys('陈飞阳')
input_elem2 = browser.find_element(By.ID,"q2")
input_elem2.send_keys('202430310006')
input_elem3 = browser.find_element(By.ID, 'q3')
input_elem3.send_keys('信息与通信工程1班')
input_elem4 = browser.find_element(By.ID,"q4")
input_elem4.send_keys('15936982275')
submit= browser.find_element(By.ID,"SubmitBtnGroup")
submit.click()
time.sleep(10)