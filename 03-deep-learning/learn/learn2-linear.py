import mxnet.ndarray as nd
import mxnet.autograd as ag
import random
from mxnet import autograd

#生成数据
num_inputs=2
num_examples=1000
true_w=[2,-3.4]
true_b=4.2
X=nd.random_normal(shape=(num_examples,num_inputs))
y=true_w[0]*X[:,0]+true_w[1]*X[:,1]+true_b
y+=.01*nd.random_normal(shape=y.shape)

batch_size = 10
def data_iter():#生成器，关键字yield，被使用的时候可以一个一个取值
    #产生num_examples个索引
    idx=list(range(num_examples))
    #随机打乱索引列表idx
    random.shuffle(idx)
    for i in range(0,num_examples,batch_size):#一次取10个
        j=nd.array(idx[i:min(i+batch_size,num_examples)])#创建索引数组，min同时保证不超过样本
        yield nd.take(X,j),nd.take(y,j)

# for data,label in data_iter():
#     print(data,label)
#     break

#随机初始化参数
w=nd.random.normal(shape=(num_inputs,1))
b=nd.zeros((1))
params=[w,b]

for param in params:
    param.attach_grad()

#定义模型
def net(X):
    return nd.dot(X,w)+b
#损失函数
def square_loss(yhat,y):
    return (yhat-y.reshape(yhat.shape))**2

def SGD(params,lr):
    for param in params:
        param[:]=param-lr*param.grad

#训练
epochs=5
learning_rate=.01
for e in range(epochs):
    total_loss=0
    for data,label in data_iter():
        with autograd.record():
            output=net(data)
            loss=square_loss(output,label)
        loss.backward()
        SGD(params,learning_rate)
        total_loss=total_loss+nd.sum(loss).asscalar()
    print("Epoch %d,average loss:%f" % (e,total_loss/num_examples))
    print(true_w,w,true_b,b)

'''
总结
逻辑就是
给数据，定义模型，训练
'''
