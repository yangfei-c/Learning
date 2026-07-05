#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/21 17:14 
@file: email_message.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import smtplib
smtObj=smtplib.SMTP('smtp.gmail.com',587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login('ccc420513@gmail.com','c15936982275')