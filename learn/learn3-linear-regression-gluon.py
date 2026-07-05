from mxnet import ndarray as nd
from mxnet import autograd
from mxnet import gluon

#创建数据
num_inputs=2
num_examples=1000
true_w=[2,-3.4]
true_b=4.2

X=nd.random_normal(shape=(num_examples,num_inputs))
y=true_w[0]*X[:,0]+true_w[1]*X[:,1]+true_b
y+=.01*nd.random_normal(shape=y.shape)

#读取数据
batch_size=10
dataset=gluon.data.ArrayDataset(X,y)
data_iter=gluon.data.DataLoader(dataset,batch_size,shuffle=True)

for data,label in data_iter:
    print(data,label)
    break

#模型定义
net=gluon.nn.Sequential()
net.add(gluon.nn.Dense(1))

#初始化模型参数
net.initialize()

#损失函数
square_loss=gluon.loss.L2Loss()

#优化
trainer=gluon.Trainer(
    net.collect_params(),'sgd',{'learning_rate':0.1})

epochs=5
batch_size=10
for e in range(epochs):
    total_loss=0
    for data,label in data_iter:
        with autograd.record():
            output=net(data)
            loss=square_loss(output,label)
        loss.backward()
        trainer.step(batch_size)
        total_loss=total_loss+nd.sum(loss).asscalar()
    print("Epoch %d,average loss:%f" % (e,total_loss/num_examples))

dense=net[0]
true_w,dense.weight.data()
true_b,dense.bias.data()
print(true_w)
print(dense.weight.data())