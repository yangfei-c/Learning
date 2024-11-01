

# 基本语法方面

## 数组切片操作

```python
x为10行2列的一个数组

索引从0开始，倒着索引从-1开始

print(x[:,1])
打印数组第二列所有元素

print(x[-1,1])
倒数第一行，第二列的该元素

print(X[0:9])省略了，输出第1行到第9行所有元素相当于X[0:9,:]或者X[0:9,]
print(X[0:9,1])则是输出第1行到第9行的所有第二列元素

x[:]则生成x的一个副本与原数组内容完全一样
```

## 生成器

生成器就是一种特殊的函数，使用关键字yield，返回一个生成器对象即使用next()函数来一个一个按自己需要获取，也可以使用for循环

```python
# 生成器函数定义
def my_generator():
    count = 1
    while count <= 5:
        yield count
        count += 1

# 使用 next() 函数获取生成器的值
gen = my_generator()
for _ in range(5):  # 我们知道生成器会产生 5 个值，所以使用 range(5) 来限制 next() 的调用次数
    print(next(gen))

# 使用 for 循环迭代生成器
for value in my_generator():
    print(value)
```

## 上下文管理器

`with` 在 Python 中是一种特殊的语法结构，用来确保代码块执行完毕后做一些清理工作，比如关闭文件或释放资源。它通常和一些支持上下文管理的类或对象一起使用。

```python
#在自动求导的上下文中，特别是在使用深度学习框架如MXNet时，with autograd.record(): #语句用于指示框架开始记录在该代码块中执行的所有操作
import mxnet as mx
from mxnet import autograd, nd

# 定义两个变量
x = nd.array([1, 2, 3])
y = nd.array([4, 5, 6])

# 开始记录计算图
with autograd.record():
    z = x + y  # 假设这是模型的一部分
    loss = nd.mean(z**2)  # 定义损失函数

# 反向传播，计算梯度
loss.backward()

# 打印梯度
print(x.grad, y.grad)  # x 和 y 的梯度将被计算和打印
在这个例子中，with autograd.record(): 确保了 z 和 loss 的计算被记录，使得 loss.backward() 能够正确地计算出梯度。如果没有使用 with 语句，那么梯度计算可能无法正确进行，因为相关的操作没有被记录
```



# 遇到的函数

```
1.  random.shuffle 是 Python 标准库 random`模块中的一个函数，用于将序列（如列表）中的元素随机打乱位置。
2.  nd.take 函数在 MXNet 中用于根据索引数组从 ndarray 中选取元素，这可以应用于不同维度的数组。
3.  `nd.dot` 函数计算矩阵相乘
```

# 列表推导式

它允许你用一行代码生成列表，通常比使用传统的 for 循环更简洁和高效

生成0~9偶数列表

```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # 输出: [0, 2, 4, 6, 8]

```

读取多个图像

```python
image_files = ["../img/ChenYao.jpg", "../img/LinYunEr.jpg", "../img/ZhaoJinMai2.webp", "../img/ChenYao3.webp"]
# 读取和转换图像
images = [cv2.cvtColor(cv2.imread(img_file), cv2.COLOR_BGR2RGB) for img_file in image_files]
```

列表推导式适用小列表，对于大型数据集使用生成器表达式更有效可以逐个生成元素

# zip，enumerate

```python
for i, (title, image) in enumerate(zip(titles, images),1)
打包和为可迭代对象生成一个带有索引的迭代器
```

# 高级索引

```python
y = torch.tensor([0,1,1])
y_hat = torch.tensor([[0.1, 0.3, 0.6], 
                      [0.3, 0.2, 0.5],
                      [0.4, 0.2, 0.5]])
print(y_hat[[0,2],0])
结果是：
	0.1
    0.4
print(y_hat[range(len(y_hat)),y])
结果是：
	0.1
    0.2
    0.2
range()#返回一个可迭代对象，会被视为高级索引
y_hat[range(len(y_hat)),y]#实际上在做选择
```

# dtype,==,argmax(axis=1)

```python
y_hat.type(y.dtype)==y#返回布尔列表，==对数据类型敏感所以保证数据类型一样
```

# numel,argmax(axis=0)

```python
y_hat.argmax(axis=1)#argmax返回每一行最大值的索引，指定了axis=1
y_hat.numel()#获取y中元素的数量
```

# 错误记录

## 文件读取报错

```python
img_path="D:\Python\XiangGuanXueXi\DeepLearning\I-am-tudui\data\hymenoptera_data\train\ants\0013035.jpg"

img=Image.open(img_path)
报错：
	OSError: [Errno 22] Invalid argument: 'D:\\Python\\XiangGuanXueXi\\DeepLearning\\I-am-tudui\\data\\hymenoptera_data\train\x07nts\x013035.jpg'
注意:
    python中\n,\t，\是带斜杠的转义字符,本来\train在os里面是\\train，但有\t就变成了\train
解决：
如下两种方式：
	1：img_path="D:\\Python\\XiangGuanXueXi\\DeepLearning\\I-am-tudui\\data\\hymenoptera_data\\train\\ants\\0013035.jpg"
    2：img=Image.open(r"D:\Python\XiangGuanXueXi\DeepLearning\I-am-tudui\data\hymenoptera_data\train\ants\0013035.jpg")
```

## torch.load加载pytorch模型出现反序列化报错

### 背景

1. 反序列化是指将数据从一种可存储或传输的格式（通常是字节流）还原为原始对象的过程。
2. 序列化是将对象转换为可存储或传输的格式（比如字符串、二进制数据），
3. 而反序列化则是将这些序列化的数据恢复成原来的对象。
4. 在 Python 中，pickle 模块用于序列化和反序列化对象。例如，使用 torch.load 加载一个 PyTorch 模型时，实际上是在反序列化模型的存储状态，即将保存的二进制文件重新转换回 PyTorch 模型对象

```
torch.load() 是用来加载序列化的对象（如模型、张量等）的函数，而底层实际上使用了 Python 的 pickle 模块来处理序列化（保存）和反序列化（加载）操作。
这也是为什么你在使用 torch.load() 时会遇到 pickle 相关的错误。
```

### 报错

```python
下面是报错
    raise pickle.UnpicklingError(_get_wo_message(str(e))) from None
    _pickle.UnpicklingError: Weights only load failed. This file can still be loaded, to do so you have two options 
这错误意思是
    表示在使用 Python 的 pickle 模块加载序列化文件时出现问题。在你的情况下，加载的是 PyTorch 模型的权重文件
    weights_only=True 失败：你在加载模型时使用了 weights_only=True，这种情况下，PyTorch 仅加载模型的权重，不反序列化模型的其他部分。但是，如果权重文件中涉及了某些未允许的全局对象，反序列化仍然会失败。
同时也提供了两种选择来解决报错
```

#### 选择1

```python
(1) Re-running `torch.load` with `weights_only` set to `False` will likely succeed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.
把weights_only设置成False
```

这种方式会加载整个模型结构以及权重，可能会绕过反序列化失败的问题，但它有潜在的安全风险，因为反序列化可能执行任意代码。==仅当文件来自可信来源时，才能使用此选项==：

#### 选择2

```python
(2) Alternatively, to load with `weights_only=True` please check the recommended steps in the following error message.
	WeightsUnpickler error: Unsupported global: GLOBAL torchvision.models.vgg.VGG was not an allowed global by default. Please use `torch.serialization.add_safe_globals([VGG])` to allowlist this global if you trust this class/function.
可以通过添加信任的全局对象到 add_safe_globals()，以便仅加载权重而不会反序列化模型结构。具体方法是将 torchvision.models.vgg.VGG 等未允许的对象添加到安全列表中：
```

#### 采用选择2解决

```python
from torch.nn import Sequential, Conv2d, ReLU,MaxPool2d,AvgPool2d,AdaptiveAvgPool2d,Linear,Dropout
from torchvision.models import VGG
torch.serialization.add_safe_globals([VGG,set,Sequential,Conv2d,ReLU,MaxPool2d,AvgPool2d,Linear,Dropout,AdaptiveAvgPool2d])
```

