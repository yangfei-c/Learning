#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/22 20:49 
@file: image_operation.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
from PIL import Image

test=Image.open('../img/img.png')
crop=test.crop((20,30,80,90))

test_width,test_height=test.size
paste_width,paste_height=crop.size

for left in range(0,test_width,paste_width):
    for top in range(0,test_height,paste_height):
        print(left,top)
        test.paste(crop,(left,top))
        test.save('../img/result.jpg')