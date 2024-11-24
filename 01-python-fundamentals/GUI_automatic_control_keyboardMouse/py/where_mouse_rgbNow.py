#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/24 22:25 
@file: where_mouse_rgbNow.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import pyautogui
import time

print('Press Ctrl-C to quit')
print('Mouse coordinates will be displayed below:')
try:
    while True:
        # 获取鼠标位置
        x, y = pyautogui.position()
        # 构建坐标和颜色信息
        position_str = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        # 获取当前像素颜色
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        position_str += f' RGB:({str(pixelColor[0]).rjust(3)},{str(pixelColor[1]).rjust(3)},{str(pixelColor[2]).rjust(3)})'
        # 动态刷新输出
        print('\r' + position_str, end='', flush=True)
        time.sleep(0.1)  # 控制刷新频率
except KeyboardInterrupt:
    print("\nProgram terminated.")


