import random
import torch
from d2l import torch as d2l

def synthetic_data(w,b,num_examples):
    X=torch.normal(0,1,(num_examples,len(w)))
    #生成一个张量，形状(num_examples,len(w)),服从标准正态分布
    y=torch.matmul(X,w)+b
    return X,y.reshape((-1,1))#-1自动计算多少行

true_w=torch.tensor([2,-3.4])
true_b=4.2

features,labels=synthetic_data(true_w,true_b,1000)
# print("features:",features[0],"\nlabels:",labels[0])
# d2l.set_figsize()
# d2l.plt.scatter(features[:,1].detach().numpy(),labels.detach().numpy(),1);
# d2l.plt.show()

#读取数据集，定义为生成器以便取小批量数据
def data_iter(batch_size,features,labels):
    num_examples=len(features)#len返回张量第一个维度的大小
    #生成索引列表
    indices=list(range(num_examples))
    #打乱
    random.shuffle(indices)
    for i in range(0,num_examples,batch_size):
        #min防止超出数据集实际边界
        #索引列表张量形式
        batch_indices=torch.tensor(indices[i:min(i+batch_size,num_examples)])
        yield features[batch_indices],labels[batch_indices]
batch_size=10
# for X,y in data_iter(batch_size,features,labels):
#     print(X,'\n',y)
#     break

#初始化参数
w=torch.normal(0,0.01,size=(2,1),requires_grad=True)
#权重从均值为零，标准差为0.01的正态分布中抽样随机数来初始化
b=torch.zeros(1,requires_grad=True)

#定义模型
def linreg(X,w,b):
    return torch.matmul(X,w)+b

#定义损失函数
def squared_loss(y_hat,y):
    return (y_hat-y.reshape(y_hat.shape))**2/2

#定义优化算法
def sgd(params,lr,batch_size):
    with torch.no_grad():
        for param in params:
            param-=lr*param.grad/batch_size
            param.grad.zero_()#梯度清0

#训练
lr=0.03
num_epochs=3
net=linreg
loss=squared_loss

for epoch in range(num_epochs):
    for X,y in data_iter(batch_size,features,labels):
        l=loss(net(X,w,b),y)
        l.sum().backward()
        sgd([w,b],lr,batch_size)
    with torch.no_grad():
        train_l=loss(net(features,w,b),labels)
        print(f'epoch{epoch+1},loss {float(train_l.mean()):f}')