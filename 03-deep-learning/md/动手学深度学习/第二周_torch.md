

# 动手学深度学习9.16~9.22

## softmax网络架构

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/softmax%E7%BD%91%E7%BB%9C%E6%9E%B6%E6%9E%84.png" style="zoom: 20%;" />

```
与线性回归一样，softmax也是一个单层神经网络，每个输出o1，o2，o3取决于所有输入x1，x2，x3，x4，因此softmax回归的输出层也是全连接层。
```

## 交叉熵损失

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E4%BA%A4%E5%8F%89%E7%86%B5%E6%8D%9F%E5%A4%B1.jpg" style="zoom: 33%;" />

## softmax运算

我们并不能将未规范化的预测o直接作为感兴趣的输出，

1.输出数值总和没有限制为1

2.输出可能为负值

```
解决办法
对每个未规范的预测求幂确保输出为非负值
再让每个求幂后的结果除以结果的总和确保输出概率综合为1
```

## 多层感知机

单层感知机只能处理线性可分问题，所有就需要到了多层感知机来处理更多复杂的非线性的问题

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E5%8D%95%E9%9A%90%E8%97%8F%E5%B1%82%E5%A4%9A%E5%B1%82%E6%84%9F%E7%9F%A5%E6%9C%BA.png" style="zoom: 25%;" />

```
把前L-1层看作表示，最后一层看作线性预测器
前L-1层负责从输入数据中提取特征或进行特征变换即构建数据的表示
第L层即最后一层，根据提取的特征进行线性预测
隐藏层通过激活函数对输入进行非线性变换，这是层感知机（MLP）等神经网络能够处理复杂的、非线性问题的关键。激活函数的引入使得网络的表示能力大大增强。如果没有激活函数，网络的每一层只能执行线性变换，
```

## 常用激活函数

### ReLU函数

修正线性单元（rectified linear unit,ReLU），实现简单，在各种预测任务中表现良好
$$
ReLU(x)=max(x,0)
$$
如下图所示为ReLU函数及其导数的曲线图

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/ReLU%E5%8F%8A%E5%85%B6%E5%AF%BC%E6%95%B0.png" style="zoom: 50%;" />

### sigmoid函数

又被称为挤压函数，它将范围（-inf,inf）上的任意输入压缩到区间（0，1）上的某个值
$$
sigmoid(x)=\frac{1}{1+e^{-x}}
$$
在隐藏层使用较少被更简单更容易训练的ReLU取代

如下图所示为sigmoid函数及其导数的曲线图

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/sigmoid%E5%8F%8A%E5%85%B6%E5%AF%BC%E6%95%B0.png" style="zoom:33%;" />

### tanh函数

与sigmoid函数类似也能将输入压缩转换到区间（-1，1）上

如下是tanh函数公式
$$
tanh(x)=\frac{1-e^{-2x}} {1+e^{-2x}}
$$
tanh函数关于坐标系原点中心对称

tanh函数及其导数曲线图如下图所示

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/tanh%E5%8F%8A%E5%85%B6%E5%AF%BC%E6%95%B0.png" style="zoom: 33%;" />

## 模型选择

### 定义

在机器学习中，通常评估几个候选模型后选择最终的模型。

### 验证集-确定最佳模型

将数据分成3份，训练数据集，测试数据集和验证数据集也称为验证集

### 数据稀缺时-K折交叉验证

当数据稀缺时可能无法提供足够数据来构成一个合适的验证集，采用K折交叉验证可以很好的解决

即将原始数据分为K个不重叠的子集，然后执行K次模型训练和验证（每次在K-1个子集上进行训练并在剩余那个没有用于训练的子集上进行验证）最后对K次实验结果取平均值来估计训练误差和验证误差。

## 泛化和训练误差

泛化误差和训练误差代表模型在不同数据集上的表现

### 训练误差

训练误差是指模型在训练数据上的错误率或损失。当模型在训练集上进行学习时，它会调整参数以最小化这个误差。

训练误差越低，说明模型在训练集上的表现越好。然而，低训练误差并不一定代表模型有良好的泛化能力，因为它可能仅仅是在记忆训练数据，而非理解其模式。

### 泛化误差

泛化误差是模型在未见过的测试数据或验证数据上的错误率或损失。

它反映了模型能否将从训练数据中学到的知识有效应用到新数据上，即模型的实际预测能力。*<u>通常，泛化误差是评估模型好坏的更重要标准，因为我们关心的是模型在新数据上的表现。</u>*

## 欠拟合

### 定义

欠拟合是指模型过于简单，无法捕捉数据的内在模式，导致在训练数据和测试数据上都表现不佳。

### 原因

模型太简单（例如使用了线性模型去拟合非线性数据）。

特征不足或重要特征未被充分利用。

训练时间不足，模型尚未充分学习数据模式。

### 解决方法

使用更复杂的模型（例如从线性模型切换到更复杂的非线性模型）。

增加更多的特征或使用更有效的特征工程。

提高模型的训练时间或增加训练轮次。

## 过拟合

### 定义

过拟合是指模型过于复杂，过度关注训练数据中的细节和噪声，导致在训练数据上表现良好，但在测试数据上表现很差。

### 原因

模型过于复杂（例如使用过多的层或节点的神经网络）。

训练数据中的噪声或异常值被模型过度学习。

训练时间过长，模型过度拟合训练数据。

### 解决过拟合

#### 正则化-权重衰减

权重衰减是正则化的一种形式，主要通过限制模型参数的大小来防止过拟合。它通常通过向损失函数中添加一个基于权重的正则化项 （L2范数）来实现。
$$
L（w）=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y})^2+\lambda||w||_2^2
$$


#### 暂退法

这是一种神经网络训练技术，其基本思想是在训练过程中随机“丢弃”一部分神经元，即将它们的输出置为零，从而避免模型对某些特定神经元过度依赖。

## 前向传播

 是指数据通过神经网络的每一层进行计算，从输入层到输出层的过程。这个过程包括：

1. **输入层**：接收原始数据。
2. **隐藏层**：每一层的神经元接收前一层的输出，并应用激活函数进行计算。
3. **输出层**：最后一层生成预测结果。

在前向传播中，每个神经元计算其加权和并加上偏置，然后通过激活函数进行非线性变换。

## 反向传播

是训练神经网络的关键步骤，用于计算每个权重的梯度，并更新权重以最小化损失函数。包括：

1. **计算损失函数的梯度**：通过输出层的预测值和实际值计算损失。
2. **计算每层的梯度**：利用链式法则从输出层逐层向回计算梯度。
3. **更新权重**：通过梯度下降算法（如SGD）调整权重，以减少损失

## 梯度消失与梯度爆炸

梯度消失是指在训练过程中，网络深层的梯度非常小，导致权重更新缓慢或几乎停滞。这通常发生在深层网络或使用某些激活函数（如 Sigmoid 和 Tanh）时。

梯度爆炸是指在训练过程中，网络中的梯度变得非常大，导致权重更新过大，从而使模型不稳定。

# 第五章

## 层和块

层（Layer）深度学习网络的基本构建单元，通常执行一个简单的变换或操作，如线性变换、卷积、激活函数等。
块（Block）由多个层或子模块组成，封装更复杂的逻辑或结构。通过块，可以使网络设计更加模块化和灵活。

```
net=nn.Sequential(nn.Linear(20,256),nn.ReLU(),nn.Linear(256,19))
nn.Sequential将三个层连接起来作为一个块
分别是线形层，激活层，线性层
```

### 自定义块

通过自定义块来直观了解块是如何工作的

```python
class MLP(nn.Module):#继承nn.Module框架
    def __init__(self):
        super().__init__()
        self.hidden=nn.Linear(20,256)
        self.out=nn.Linear(256,10)

    def forward(self,X):#前向传播计算方法
        return self.out(F.relu(self.hidden(X)))
```

### 顺序块

```python
class MySequential(nn.Module):
    def __init__(self,*args):
        super().__init__()
        for idx,module in enumerate(args):
        #enumerate打包块和索引为元组for来遍历
            self._modules[str(idx)]=module
    def forward(self,X):#前向传播计算
        for block in self._modules.values():
            X=block(X)
        return X
```

### 混合块

混合块的使用使得神经网络的设计更具灵活性、可扩展性和可维护性。它们适用于多种深度学习应用，特别是在需要处理复杂任务和大规模数据时。

```python
class FixedHiddenMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.rand_weight=torch.rand((20,20),requires_grad=False)
        self.linear=nn.Linear(20,20)
    def forward(self,X):
        X=self.linear(X)
        X=F.relu(torch.mm(X,self.rand_weight)+1)
        X=self.linear(X)
        while X.abs().sum()>1:
            X /=2
        return X.sum()

class NestMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net=nn.Sequential(nn.Linear(20,64),nn.ReLU(),nn.Linear(64,32),nn.ReLU())
        self.linear = nn.Linear(32, 16)
    def forward(self,X):
        return self.linear(self.net(X))
```

### 自定义层

自定义层是构建深度学习模型的基础组件。它通常实现一个特定的操作，比如卷积、激活函数或归一化。

```python
class centered_layer(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self,X):
        return X-X.mean()
```



## 参数管理

### 参数访问

```python
print(net[0].state_dict())#打印第一层参数
```

### 目标参数

```python
print(net[2].bias)
print(net[2].bias.data)
#直接访问到bias
```

### 一次性访问所有参数

```python
print(*[(name,param.shape) for name,param in net[0].named_parameters()])
print(*[(name,param.shape) for name,param in net.named_parameters()])
```

### 从嵌套中获取参数

进入block2

​	block1-->block1-->block1-->block1

​		block1中的结构

​			linear-->ReLU-->linear-->ReLU

进入linear(4,1)

```python
def block1():
    return nn.Sequential(nn.Linear(4,8),nn.ReLU(),nn.Linear(8,4),nn.ReLU())
def block2():
    net=nn.Sequential()
    for i in range(4):
        net.add_module(f'block{i}',block1())
    return net
rgnet=nn.Sequential(block2(),nn.Linear(4,1))
print(rgnet(X))
print(rgnet)
print(rgnet[0][1][0].bias.data)
#rgnet[0][1][0]
#访问第一个层即block1，rgnet[0][1]访问第一个层里面第二层即第二个block1(因为#block2包含4个block1)，rgnet[0][1][0]访问第一层block2中第二层block2中第一层即linear
```

### 参数初始化

```python
def init_xavier(m):
    if type(m)==nn.Linear:
        nn.init.xavier_uniform_(m.weight)
def init_42(m):
    if type(m)==nn.Linear:
        nn.init.constant_(m.weight,42)
net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 1))
net[0].apply(init_xavier)
net[2].apply(init_42)
print(net[0].weight.data[0])
print(net[2].weight.data)


```

Xavier初始化防止梯度消失和爆炸
$$
W的初始化服从均匀分布(-\sqrt{\frac{6}{n_{in}+n_{out}}} , \sqrt{\frac{6}{n_{in}+n_{out}}})
$$

### 参数绑定

```python
shared=nn.Linear(8,8)
net=nn.Sequential(nn.Linear(4,8),nn.ReLU(),shared,nn.ReLU(),shared,nn.ReLU(),nn.Linear(8,1))
X=torch.rand(size=(2,4))
net(X)
print(net[2].weight.data[0]==net[4].weight.data[0])
```

## 读写文件

耗时较长的训练，最佳做法是定期保存中间结果，以防止服务器断电损失数天结果。

```python
import torch
from torch import nn
from torch.nn import functional as F
x=torch.tensor([2,1,23,1])
torch.save(x,'x_file')
x2=torch.load('x_file',weights_only=True)
print(x2)
```

也可以保存模型参数，之后可以不用随机初始化模型参数直接读取文件中存储的参数

```python
#state_dict()字典，包含模型的所有可学习参数
torch.save(net.state_dict(),'mlp.params')
clone=MLP()
clone.load_state_dict(torch.load('mlp.params',weights_only=True))
```

## 计算设备

我们可以指定用于存储和计算的设备，

CPU代表所有物理CPU和内存

GPU只代表一个卡和相应的显存，如果有多个GPU我们使用torch.device(f'cuda:{i}')来表示第i块GPU

# 第六章

## 卷积神经网络

CNN是一类强大的为处理图像数据而设计的神经网络

多层感知机MLP很适合处理表格数据但是涉及到高维感知数据就不适用了

### 互相关运算

```python
for i in range(Y.shape[0]):
    for j in range(Y.shape[1]):
        Y[i,j]=(X[i:i+h,j:j+w]*K).sum()
#X输入局部区域与卷积核相乘并求和
#h,w为卷积核大小
```

### 卷积层

卷积层通过卷积核（filters）在输入数据上滑动，对局部区域进行加权求和操作，并将结果存储为输出特征图（feature map）。

它可以帮助神经网络捕捉到输入数据的空间特征。

```python
class conv2d(nn.Module):
    def __init__(self,kernel_size):
        super().__init__()
        self.weight=nn.Parameter(torch.rand(kernel_size))
        self.bias=nn.Parameter(torch.zeros(1))
        
    def forward(self,x):
        return corr2d(x,self.weight)+self.bias
```

### 图像中目标边缘检测

#### 手动设计卷积核

进行互相关运算时，如果水平元素相同则输出为零，否则输出为非零

```python
X=torch.ones((6,8))
X[:,2:6]=0
K=torch.tensor([[1.0,-1.0]])
print(corr2d(X,K))
```

#### 学习卷积核

遇到复杂数值的卷积核或者连续卷积层时，不可能手动设计卷积核，通过学习由X生成Y的卷积核

```python
X=X.reshape((1,1,6,8))
#调整批量为1通道为1大小为6X8的四维形状满足conv2d输入数据格式要求
Y=Y.reshape((1,1,6,7))
lr=3e-2
for i in range(10):
    Y_hat=conv2d(X)
    l=(Y_hat-Y)**2
    conv2d.zero_grad()
    l.sum().backward()
    conv2d.weight.data[:]-=lr*conv2d.weight.grad
    if(i+1)%2==0:
        print(f'epoch{i+1},loss{l.sum():.3f}')
```

### 填充与步幅

在输入图像的边缘进行填充元素防止丢失边缘像素

采用调整步幅高效计算或缩减采样

计算输出形状
$$
(\frac{h_{in}-k_h+2p}{s}+1,\frac{w_{in}-k_w+2p}{s}+1)
$$

$$
p是填充，s是步幅，h×w为输入形状，k_h×k_w为卷积核形状
$$

### 
