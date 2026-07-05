import math

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
from d2l import torch as d2l

#生成数据集
max_degree=20
n_train,n_test=100,100
true_w=np.zeros(max_degree)
true_w[0:4]=np.array([5,1.2,-3.4,5.6])

features=np.random.normal(size=(n_train+n_test,1))
np.random.shuffle(features)
#将features扩展为多项式特征
poly_features=np.power(features,np.arange(max_degree).reshape(1,-1))
for i in range(max_degree):
    poly_features[:,i]/=math.gamma(i+1)#gamma(i+1)为i阶乘
labels=np.dot(poly_features,true_w)
labels+=np.random.normal(scale=0.1,size=labels.shape)

true_w,features,poly_features,labels=[torch.tensor
(x,dtype=torch.float32)for x in[true_w,features,poly_features,labels]]
#print(features[:2],poly_features[:2,:],labels[:2])

#模型评估
def evaluate_loss(net,data_iter,loss):
    metric=d2l.Accumulator(2)
    for X,y in data_iter:
        out=net(X)
        y=y.reshape(out.shape)
        l=loss(out,y)
        metric.add(l.sum(),l.numel())
    return metric[0]/metric[1]

#训练函数
def train(train_features,test_features,train_labels,test_labels,num_epochs=400):
    loss=nn.MSELoss(reduction='none')
    input_shape=train_features.shape[-1]
   #模型为单层线性回归模型
    net=nn.Sequential(nn.Linear(input_shape,1,bias=False))
    batch_size=min(10,train_labels.shape[0])
    #训练数据的迭代器，训练特性和标签打包为小批量进行训练
    train_iter=d2l.load_array((train_features,train_labels.reshape(-1,1)),batch_size)
    test_iter=d2l.load_array((test_features,test_labels.reshape(-1,1)),batch_size,is_train=False)
    #定义优化器
    trainer=torch.optim.SGD(net.parameters(),lr=0.01)
   #xlim横轴范围，yscale纵轴刻度，legend图例
    animator=d2l.Animator(xlabel='epoch',ylabel='loss',yscale='log',
                          xlim=[1,num_epochs],ylim=[1e-3,1e2],legend=['train','test'])
    for epoch in range(num_epochs):
        d2l.train_epoch_ch3(net,train_iter,loss,trainer)
        if epoch==0 or (epoch+1)%20==0:
            animator.add(epoch+1,(evaluate_loss(net,train_iter,loss),evaluate_loss(net,test_iter,loss)))
    print('weight',net[0].weight.data.numpy())
#拟合正常
# train(poly_features[:n_train,:4],poly_features[n_train:,:4],labels[:n_train],labels[n_train:])
# plt.show()

#欠拟合
# train(poly_features[:n_train,:2],poly_features[n_train:,:2],labels[:n_train],labels[n_train:])
# plt.show()

#过拟合
train(poly_features[:n_train,:],poly_features[n_train:,:],labels[:n_train],labels[n_train:],num_epochs=1500)
plt.show()