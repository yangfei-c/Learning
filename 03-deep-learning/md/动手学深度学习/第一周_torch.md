# 动手学深度学习9.12~9.15

## 机器学习关键组件

可以用来学习的数据data

如何转换数据类型的模型model

一个目标函数（objective function），用来量化模型的有效性

调整模型参数以优化目标函数的算法algorithm

## 监督学习

擅长在给定输入特征的情况下预测标签。

之所以能预测，是因为在训练参数时为模型提供了一个数据集，其中每个样本都有真实的标签。

### 回归

一般有关“有多少”的问题很有可能是回归问题，回归问题目标是生成一个模型使它的预测值非常接近实际标签值。“预测值与实际标签值的差距”损失函数为平方误差。

### 分类

分类很好地解决“哪一个”的问题，分类问题希望预测样本属于哪个类别，训练一个分类器输出预测的类别。与回归不同，分类问题常见的损失函数被称为交叉熵，很好的例子，预测蘑菇是否有毒，如果20%无毒，那么我们也不会去吃它。

```
其它监督学习还有标注问题，搜索问题，推荐系统问题，序列学习问题。
```

## 线性回归

### 线性回归的基本元素

首先要收集真实的数据集(训练数据集，training dataset)，每行数据称为数据样本，预测的目标成为标签（label）或目标（target），预测所依据的自变量称为特征（feature）。

### 线性模型

线性假设即目标可以表示为特征的加权和，如下式

price=w×area+w1×age+b

```
放射变换（affine transformation）特点是通过加权和对特征进行线性变换并通过偏置项进行平移，所以严格来说该式是输入特征的一个仿射变换
```

从式可知，给定数据集，想预测目标，就需要找到该模型的权重w和偏置b。

```
输出的预测值由输入特征通过线性模型的仿射变换进行确定，仿射变换由所选权重和偏置确定。
```

实际在机器学习领域中，通常采用高维数据集，就需要采用线性代数的表示方法。

寻找最佳模型参数之前需要两个工具，模型质量的度量方式和更新模型以提高模型预测质量的方法。

回归常用的损失函数是平方误差函数，往往加一个常熟1/2并无影响，对损失函数求导之后参数系数变为1。

### 随机梯度下降

算法步骤

初始化模型参数
从数据集中随机抽取小批量样本且在负梯度方向上更新参数，并不断迭代。

```
为什么小批量？ 
在每次更新参数之前必须遍历整个数据集，因此每次需要计算更新的时候随机抽取一小批样本。
同时处理整个小批量的样本：
对计算进行向量化，从而利用线性代数库而不是使用for循环。
```

## 从线性回归到神经网络

线性回归模型是一个简单的神经网络如下神经网络图所示

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92%E6%98%AF%E4%B8%80%E4%B8%AA%E5%8D%95%E5%B1%82%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C.jpg" style="zoom:30%;" />

## 从0开始实行线性回归

不使用框架，了解更细致的工作原理方便自己自定义模型，自定义层或自定义损失函数。

### 生成数据集

```python
#函数封装
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

```

​       打印特征和标签的第一行数据样本，绘出第二个特征和标签的散点图

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E6%95%A3%E7%82%B9%E5%9B%BE%E5%92%8C%E6%95%B0%E6%8D%AE%E6%A0%B7%E6%9C%AC.png" alt="15" style="zoom: 50%;" />

### 读取数据集



```python
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
batch_size=5
for X,y in data_iter(batch_size,features,labels):
    print(X,'\n',y)
    break
```

```
生成器保证小批量数据读取，会保存函数状态。
GPU并行计算优势使得大小合理的小批量被并行地进行模型计算。
```

### 初始化模型参数

初始化参数之后就是更新参数，直到这些参数足以拟合我们的数据。

### ……………………

定义模型，定义损失函数，定义优化算法

### 训练

```python
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
```

### 总结

```
在从0实现线性回归的过程中并没有使用框架，这样能更好的了解深度网络是如何实现和优化的。
```

