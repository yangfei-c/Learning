#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/11 23:07 
@file: time_datatime_multithreading.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import time,threading
print("start program")
def take_a_nap():
    time.sleep(2)
    print("wake up")

thread=threading.Thread(target=take_a_nap)
thread.start()
print("end program")