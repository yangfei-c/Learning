import random
import torch
from d2l import torch as d2l

def synthetic_data(w,b,num_examples):
    X=torch.normal(0,1,(num_examples,len(w)))
    #生成一个张量，形状(num_examples,len(w)),服从标准正态分布
    y=torch.matmul(X,w)+b
    return X,y.reshape((-1,1))#-1自动计算多少行

num_examples=1000
true_w=torch.tensor([2,-3.4])
true_b=4.2

features,labels=synthetic_data(true_w,true_b,num_examples)
print("features:",features[0],"\nlabels:",labels[0])
d2l.set_figsize()
d2l.plt.scatter(features[:,1].detach().numpy(),labels.detach().numpy(),1);
d2l.plt.show()