#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/24 21:14
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : attention_visualization.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import torch
from d2l import torch as d2l

def show_heatmaps(matrices, xlabel, ylabel, titles=None,
                  figsize=(2.5, 2.5),cmap='Reds'):

    num_rows, num_cols = matrices.shape[0], matrices.shape[1]
    fig, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize,
                                 sharex=True, sharey=True, squeeze=False)
    for i, (row_axes, row_matrices) in enumerate(zip(axes, matrices)):
        for j, (ax, matrix) in enumerate(zip(row_axes, row_matrices)):
            pcm = ax.imshow(matrix.detach().numpy(), cmap=cmap)
            if i == num_rows - 1:
                ax.set_xlabel(xlabel)
            if j == 0:
                ax.set_ylabel(ylabel)
            if titles:
                ax.set_title(titles[j])
    fig.colorbar(pcm, ax=axes, shrink=0.6);
attention_weights = torch.randn((10,10)).reshape((1, 1, 10, 10))
#生成矩阵，把矩阵值映射为图像，值越大就越红
print(attention_weights)
show_heatmaps(attention_weights, xlabel='Keys', ylabel='Queries')
plt.show()
