#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/24 21:34 
@file: where_mouse.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import pyautogui
import time

print('Press Ctrl-C to quit')
print('Mouse coordinates will be displayed below:\n')

try:
    while True:
        x, y = pyautogui.position()
        position_str = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        print('\r' + position_str, end='', flush=True)  # 动态刷新，覆盖整行
        time.sleep(1)  # 控制刷新频率
except KeyboardInterrupt:
    print('\nProgram terminated by user. Goodbye!')
