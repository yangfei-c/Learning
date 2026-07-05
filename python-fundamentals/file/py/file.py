#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/11/7 9:38
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : file.py
# @Software: PyCharm

# TODO:Save clipboard content
# TODO:List keywords and load content

import shelve,pyperclip,sys

mutliclipboard=shelve.open('mcb')
#save clipboard content
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mutliclipboard[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    # list keywords and load content
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mutliclipboard.keys())))
    elif sys.argv[1] in list(mutliclipboard.keys()):
        pyperclip.copy(mutliclipboard[sys.argv[1]])
mutliclipboard.close()
