#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 15:04
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : read_by_random.py
# @Software: PyCharm

import torch
import random


def seq_data_iter_random(corpus, batch_size, num_steps):  #@save
    # 0~4随机选一个作为起始位置，进行切片操作
    corpus = corpus[random.randint(0, num_steps - 1) : ]
    #可以生成多少个子序列，减去1，是因为我们需要考虑标签
    num_subseqs = (len(corpus) - 1) // num_steps
    # 长度为num_steps的子序列的起始索引
    initial_indices = list(range(0, num_subseqs * num_steps, num_steps))
    random.shuffle(initial_indices)#打乱起始索引

    def data(pos):
        # 返回从pos位置开始的长度为num_steps的序列
        return corpus[pos: pos + num_steps]

    num_batches = num_subseqs // batch_size#可以生成num_batches个标签队
    for i in range(0, batch_size * num_batches, batch_size):
        # 在这里，initial_indices包含子序列的随机起始索引
        initial_indices_per_batch = initial_indices[i: i + batch_size]#取起始索引
        X = [data(j) for j in initial_indices_per_batch]
        Y = [data(j + 1) for j in initial_indices_per_batch]
        yield torch.tensor(X), torch.tensor(Y)

my_seq = list(range(35))
for X, Y in seq_data_iter_random(my_seq, batch_size=2, num_steps=5):
    print('X: ', X, '\nY:', Y)