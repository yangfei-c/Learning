#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/15 15:17
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : train_after_data_by_transform.py
# @Software: PyCharm
#!/usr/bin/python3.10

#导包
import time
import torch
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

#定义训练设备
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

# 定义残差块
class Conv_Block(nn.Module):
    def __init__(self, inchannel, outchannel, res=True):
        super(Conv_Block, self).__init__()
        self.res = res  # 是否带残差连接
        self.left = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(outchannel),
            nn.ReLU(inplace=True),
            nn.Conv2d(outchannel, outchannel, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(outchannel),
        )

        # 如果输入输出通道数不同，使用shortcut进行1x1卷积调整
        self.shortcut = nn.Sequential()
        if inchannel != outchannel:
            self.shortcut = nn.Sequential(
                nn.Conv2d(inchannel, outchannel, kernel_size=(1, 1), bias=False),
                nn.BatchNorm2d(outchannel)
            )
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        out = self.left(x)
        if self.res:
            out += self.shortcut(x)
        out = self.relu(out)
        return out

# 定义新的 M_model
class M_model(nn.Module):
    def __init__(self):
        super(M_model, self).__init__()

        # 定义4个卷积块
        self.block1 = Conv_Block(inchannel=3, outchannel=64)
        self.block2 = Conv_Block(inchannel=64, outchannel=128)
        self.block3 = Conv_Block(inchannel=128, outchannel=256)
        self.block4 = Conv_Block(inchannel=256, outchannel=512)

        # 全连接层
        self.classifier = nn.Sequential(
            nn.Flatten(),  # Flatten层
            nn.Dropout(0.4),
            nn.Linear(512 * 2 * 2, 256),  # 根据特征图尺寸计算输入到全连接层的大小
            nn.ReLU(),
            nn.Linear(256, 64),  # 第二个全连接层
            nn.ReLU(),
            nn.Linear(64, 10)  # 输出层（10类）
        )

        self.maxpool = nn.MaxPool2d(kernel_size=2)  # 最大池化层，用于每个卷积块后缩减尺寸

    def forward(self, x):
        # 通过每个卷积块和池化层
        out = self.block1(x)
        out = self.maxpool(out)
        out = self.block2(out)
        out = self.maxpool(out)
        out = self.block3(out)
        out = self.maxpool(out)
        out = self.block4(out)
        out = self.maxpool(out)

        # 通过全连接层
        out = self.classifier(out)
        return out

#数据预处理
train_transforms = transforms.Compose([
    transforms.ToTensor(),  # 转化为tensor类型
    # 从[0,1]归一化到[-1,1]
    transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225]),
    transforms.RandomHorizontalFlip(),  # 随机水平镜像
    transforms.RandomErasing(scale=(0.04, 0.2), ratio=(0.5, 2)),  # 随机遮挡
    transforms.RandomCrop(32, padding=4),  # 随机裁剪
])
test_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

#准备数据集
train_data=torchvision.datasets.CIFAR10(root="../dataset",train=True,
                transform=train_transforms,download=True)
test_data=torchvision.datasets.CIFAR10(root="../dataset",
                train=False,transform=test_transforms,download=True)

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
if torch.cuda.is_available():
    m_model=m_model.cuda()

#损失函数
loss_function=nn.CrossEntropyLoss()
if torch.cuda.is_available():
    loss_function=loss_function.cuda()

# 设置训练网络参数
train_nums=0#记录训练次数
test_nums=0#记录测试次数
epoch=100#训练轮数

#优化器
learning_rate_min=5e-2
learning_rate_max=1e-3#科学计数法
#添加tensorboard
writer=SummaryWriter("../logs_train")
start_time=time.time()
for i in range(epoch):
    #动态学习率
    learning_rate = learning_rate_max - (learning_rate_max - learning_rate_min) * (i + 1) / epoch
    optimizer = torch.optim.SGD(m_model.parameters(), lr=learning_rate)
    print("learning_rate:{}".format(learning_rate))

    print("----------第{}轮训练开始---------".format(i+1))
    # 训练步骤开始
    for date in train_data_loader:
        imgs,targets=date
        if torch.cuda.is_available():
            imgs=imgs.cuda()
            targets=targets.cuda()
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
            end_time=time.time()
            print(end_time-start_time)
            print("训练次数：{},损失：{}".format(train_nums,loss))
            writer.add_scalar("train_loss",loss.item(),train_nums)
    #测试步骤
    total_test_loss=0
    total_accuracy=0
    with torch.no_grad():
        for data in test_data_loader:
            imgs,targets=data
            if torch.cuda.is_available():
                imgs=imgs.cuda()
                targets=targets.cuda()
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
