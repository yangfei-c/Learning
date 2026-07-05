#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/12 16:24 
@file: wjx_by_wait_time.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
start_time=time.time()
time_wait = 0.1
# 启动 Chrome 浏览器
browser = webdriver.Chrome()

# 打开指定的网页
browser.get('https://www.wjx.cn/vm/YuyJRi9.aspx ')

try:
    # 使用显式等待，等待问卷字段 q1 出现
    input_elem1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'q1')))
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

# 等待问卷开放后，查找并填写问卷字段
input_elem1 = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'q1')))
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
end_time=time.time()
print(f'填写问卷用时{start_time-end_time}秒')
# 可选：等待一些时间，以确保问卷成功提交
time.sleep(10)

# 关闭浏览器
browser.quit()
