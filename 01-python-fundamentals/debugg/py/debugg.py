#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/11/7 11:28
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : debugg.py
# @Software: PyCharm
def spam():
    bacon()
def bacon():
    raise Exception('The is  the error message')
spam()