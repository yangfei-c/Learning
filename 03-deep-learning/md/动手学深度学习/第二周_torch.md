# 动手学深度学习9.16~9.22

## softmax网络架构

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/softmax%E7%BD%91%E7%BB%9C%E6%9E%B6%E6%9E%84.png" style="zoom: 20%;" />

```
与线性回归一样，softmax也是一个单层神经网络，每个输出o1，o2，o3取决于所有输入x1，x2，x3，x4，因此softmax回归的输出层也是全连接层。
```

## softmax运算

我们并不能将未规范化的预测o直接作为感兴趣的输出，

1.输出数值总和没有限制为1

2.输出可能为负值

```
解决办法
对每个未规范的预测求幂确保输出为非负值
再让每个求幂后的结果除以结果的总和确保输出概率综合为1
```

