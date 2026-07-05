#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 10:32
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : language_model_dataset.py
# @Software: PyCharm

import random

import matplotlib.pyplot as plt
import torch
import collections
import re
from d2l import torch as d2l

#一元
#词元列表
tokens=d2l.tokenize(d2l.read_time_machine())
#语料库
corpus=[token for line in tokens for token in line]
vocab=d2l.Vocab(corpus)
print("一元：")
print(vocab.token_freqs[:10])
#画一元词频图
freqs = [freq for token, freq in vocab.token_freqs]
d2l.plot(freqs, xlabel='token: x', ylabel='frequency: n(x)',
         xscale='log', yscale='log')
# plt.show()

#二元
print("二元：")
bigram_tokens = [pair for pair in zip(corpus[:-1], corpus[1:])]
bigram_vocab = d2l.Vocab(bigram_tokens)
print(bigram_vocab.token_freqs[:10])

#三元
trigram_tokens = [triple for triple in zip(
    corpus[:-2], corpus[1:-1], corpus[2:])]
trigram_vocab = d2l.Vocab(trigram_tokens)
print("三元：")
print(trigram_vocab.token_freqs[:10])

#绘制三种元词频图
bigram_freqs = [freq for token, freq in bigram_vocab.token_freqs]
trigram_freqs = [freq for token, freq in trigram_vocab.token_freqs]
d2l.plot([freqs, bigram_freqs, trigram_freqs], xlabel='token: x',
         ylabel='frequency: n(x)', xscale='log', yscale='log',
         legend=['unigram', 'bigram', 'trigram'])
plt.show()

