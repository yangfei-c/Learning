#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/12 16:44
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : train.py
# @Software: PyCharm
import torch.optim
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from model import *

#准备数据集
train_data=torchvision.datasets.CIFAR10(root="../dataset",train=True,
                transform=torchvision.transforms.ToTensor(),download=True)
test_data=torchvision.datasets.CIFAR10(root="../dataset",
                train=False,transform=torchvision.transforms.ToTensor(),download=True)

#打印数据集长度
train_data_size=len(train_data)
test_data_size=len(test_data)
print("训练集长度为：{}".format(train_data_size))
print("测试集长度为：{}".format(test_data_size))

#Dataloader加载数据集
train_data_loader=DataLoader(train_data,batch_size=64)
test_data_loader=DataLoader(test_data,batch_size=64)

#创建网络模型
m_model=M_model()

#损失函数
loss_function=nn.CrossEntropyLoss()

#优化器
learning_rate=1e-2#科学计数法
optimizer=torch.optim.SGD(m_model.parameters(),lr=learning_rate)

# 设置训练网络参数
train_nums=0#记录训练次数
test_nums=0#记录测试次数
epoch=10#训练轮数

#添加tensorboard
writer=SummaryWriter("../logs_train")
for i in range(epoch):
    print("----------第{}轮训练开始---------".format(i+1))

    # 训练步骤开始
    for date in train_data_loader:
        imgs,targets=date
        outputs=m_model(imgs)

        #损失
        loss=loss_function(outputs,targets)

        #优化器进行模型优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        #训练第几次时的损失值
        train_nums+=1
        if train_nums%100==0:
            print("训练次数：{},损失：{}".format(train_nums,loss))
            writer.add_scalar("train_loss",loss.item(),train_nums)
    #测试步骤
    total_test_loss=0
    total_accuracy=0
    with torch.no_grad():
        for data in test_data_loader:
            imgs,targets=data
            outputs=m_model(imgs)
            loss=loss_function(outputs,targets)
            accuracy=(outputs.argmax(1)==targets).sum()
            total_accuracy=total_accuracy+accuracy
            total_test_loss=total_test_loss+loss.item()
    print("整体测试集上的loss：{}".format(total_test_loss))
    print("整体测试集上正确率：{}".format(total_accuracy/test_data_size))
    writer.add_scalar("test_accuracy",total_accuracy/test_data_size,i)
    writer.add_scalar("test_loss",total_test_loss,i)

    #模型保存
    torch.save(m_model,"../model/model_{}".format(i+1))
    print("第{}轮模型已保存".format(i+1))

writer.close()
