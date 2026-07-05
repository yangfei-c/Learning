#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/11/8 14:58
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : web.py
# @Software: PyCharm
'''
下载所有的XKCD漫画
'''
import requests

res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print(f'There was a problem:{exc}')