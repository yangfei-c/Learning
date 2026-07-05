#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/24 22:38 
@file: locate_on_screen.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import pyautogui

locate=pyautogui.locateOnScreen('img.png')
x,y=pyautogui.center(locate)
pyautogui.doubleClick(x,y)

