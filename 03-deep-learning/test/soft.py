import matplotlib.pyplot as plt
import torch
from IPython import display
from d2l import torch as d2l

#设置数据迭代器批量
batch_size=256
#train_iter,test_iter=d2l.load_data_fashion_mnist(batch_size)
#初始化参数
num_inputs=784
num_outputs=10
W=torch.normal(0,0.01,size=(num_inputs,num_outputs),requires_grad=True)
b=torch.zeros(num_outputs,requires_grad=True)

def softmax(X):
    X_exp=torch.exp(X)
    denominator=X_exp.sum(1,keepdim=True)
    return X_exp/denominator

def net(X):
    return softmax(torch.matmul(X.reshape((-1,W.shape[0])),W)+b)

def loss(y_hat,y):
    return -torch.log(y_hat[range(len(y_hat)),y])


def evaluate_accuracy(net, data_iter):
    metric = Accumulator(2)  # 创建一个 Accumulator 用于累计准确率和样本数
    with torch.no_grad():  # 禁用梯度计算以节省内存和计算资源
        for X, y in data_iter:
            # 获取模型预测
            y_hat = net(X)
            # 判断是否为多分类任务并计算准确率
            if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
                y_hat = y_hat.argmax(axis=1)  # 获取概率最大索引值
            cmp = y_hat.type(y.dtype) == y  # 通过预测与真实比对，返回一个布尔列表
            metric.add(float(cmp.type(y.dtype).sum()), y.numel())  # 累加准确的样本数和总样本数
    return metric[0] / metric[1]  # 返回准确率

class Accumulator:
    def __init__(self,n):
        self.data=[0.0]*n
    def add(self,*args):
        #列表推导式
        self.data=[a+float(b) for a,b in zip(self.data,args)]
    def reset(self):
        self.data=[0.0]*len(self.data)
    def __getitem__(self, idx):
        return self.data[idx]

X = torch.tensor([[1.0, 2.0, 3.0],
                  [1.0, 2.0, -1.0]])

