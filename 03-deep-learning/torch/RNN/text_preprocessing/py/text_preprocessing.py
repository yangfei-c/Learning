#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/17 20:34
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : text_preprocessing.py
# @Software: PyCharm

import collections
import re
from d2l import torch as d2l

#读取数据集
d2l.DATA_HUB['time_machine']=(d2l.DATA_URL + 'timemachine.txt',
                              '090b5e7e70c295757f55df93cb0a180b9691891a')

def read_time_machine():
    file_path = d2l.download('time_machine')  # 下载文件并获取路径
    print("下载的文件路径:", file_path)  # 打印下载路径
    with open(file_path,'r') as f:
        lines=f.readlines()
    return [re.sub('[^A-Za-z]+',' ',line).strip().lower() for line in lines]

lines=read_time_machine()#这里读取文本数据
# print("文本总行数：{}".format(len(lines)))
# print(lines[0])
# print(lines[100])

#词元化
def tokenize(lines,token='word'):
    if token=='word':
        return [line.split() for line in lines]
    elif token=='char':
        return [list(line) for line in lines]
    else:
        print('错误：未知词元类型：'+token)

tokens=tokenize(lines)#这里文本数据词元化
# for i in range(11):
#     print(tokens[i])

#词表
class Vocab:
    """文本词表"""
    def __init__(self, tokens=None, min_freq=0, reserved_tokens=None):
        if tokens is None:
            tokens = []
        if reserved_tokens is None:
            reserved_tokens = []
        # 按出现频率排序
        counter = count_corpus(tokens)
        self._token_freqs = sorted(counter.items(), key= (lambda x: x[1]),
                                   reverse=True)#counter.items()二元组
                                #lambda 是一个用于创建匿名函数的关键字，格式为：lambda 参数: 表达式
        #初始化创建
        self.idx_to_token = ['<unk>'] + reserved_tokens
        self.token_to_idx = {token: idx
                             for idx, token in enumerate(self.idx_to_token)}

        #从_token_freqs取数据加入idx_to_token和_token_to_idx中
        for token, freq in self._token_freqs:
            if freq < min_freq:
                break
            if token not in self.token_to_idx:
                self.idx_to_token.append(token)
                self.token_to_idx[token] = len(self.idx_to_token) - 1

    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk)#键不存在时返回的默认值
        return [self.__getitem__(token) for token in tokens]

    def to_tokens(self, indices):
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]

    @property
    def unk(self):  # 未知词元的索引为0
        return 0

    @property
    def token_freqs(self):
        return self._token_freqs

def count_corpus(tokens):
    """统计词元的频率"""
    # 这里的tokens是1D列表或2D列表
    if len(tokens) == 0 or isinstance(tokens[0], list):
        # 将词元列表展平成一个列表
        tokens = [token for line in tokens for token in line]
        #双层循环，外层for line in tokens
                    #内层for token in line
    return collections.Counter(tokens)

vocab=Vocab(tokens)#词元化的列表传入进行词表构建
# print(list(vocab.token_to_idx.items())[:10])
# print(vocab.to_tokens([2,4,19]))
# print(vocab['the'])
# for i in [0, 10]:
#     print('文本:', tokens[i])
#     print('索引:', vocab[tokens[i]])
def load_corpus_time_machine(max_tokens=-1):
    lines=read_time_machine()
    tokens=tokenize(lines,'char')
    vocab=Vocab(tokens)
    corpus=[vocab[token] for line in tokens for token in tokens]
    if max_tokens>0:
        corpus=corpus[:max_tokens]
    return corpus,vocab

corpus,vocab=load_corpus_time_machine()
print(len(corpus))
print(len(vocab))

