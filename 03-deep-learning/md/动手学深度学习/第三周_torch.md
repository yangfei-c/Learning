# 动手学深度学习9.23~9.29

## 1×1卷积层

1×1 卷积核可以在不改变空间维度的情况下，减少或增加通道数。这个特性使得 1×1 卷积非常适合用于降维或升维，从而减少计算复杂度或增加模型的表达能力

```python
def corr2d_muti_in_out_11(X,K):
    c_i,h,w=X.shape
    c_o=K.shape[0]#获得核的通道数
    X=X.reshape((c_i,h*w))#重塑形状
    K=K.reshape((c_o,c_i))
    Y=torch.matmul(K,X)
    return Y.reshape((c_o,h,w))
X=torch.normal(0,1,(3,3,3))
K=torch.normal(0,1,(2,3,1,1))
```

```python
# 输入张量 X，形状为 (3, 2, 2)，表示 3 个通道，每个通道是 2x2 的矩阵
X = torch.tensor([[[0.0, 1.0], 
                   [2.0, 3.0]],
                  
                  [[4.0, 5.0], 
                   [6.0, 7.0]],
                  
                  [[8.0, 9.0], 
                   [10.0, 11.0]]])

# 卷积核张量 K，形状为 (2, 3, 1, 1)，2 个输出通道，3 个输入通道
K = torch.tensor([[[[0.0]], [[1.0]], [[2.0]]],  # 第 1 个卷积核
                  [[[3.0]], [[4.0]], [[5.0]]]]) # 第 2 个卷积核
```

X=X.reshape((c_i,h*w))#重塑形状

 K=K.reshape((c_o,c_i))#重塑卷积核的形状

```python
X = tensor([[ 0.,  1.,  2.,  3.],
            [ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]])
```

## 汇聚层

降低卷积层对位置的敏感性，降低对空间降采样表示的敏感性

### 最大汇聚层

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E6%9C%80%E5%A4%A7%E6%B1%87%E8%81%9A%E5%B1%82.png" style="zoom:33%;" />

最大汇聚层保留局部区域中的最强特征，突出最显著的特征信号，过滤掉弱特征
通过汇聚操作减少特征图的高度和宽度，通常步幅与池化窗口大小相同
由于汇聚操作的降维特性，它可以有效地减少模型的参数量，进而有助于降低过拟合

### 平均汇聚层

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E5%B9%B3%E5%9D%87%E6%B1%87%E8%81%9A%E5%B1%82.png" style="zoom:33%;" />

平均汇聚层对特征进行平滑处理，减少特征图的变化幅度，将局部特征信息平均化。
通过汇聚操作减少特征图的高度和宽度，起到降采样的作用

## 卷积神经网络LeNet

最早发布的卷积神经网络之一，贝尔实验室1989年提出，目的识别图像中的手写文字

如图为LeNet模型的训练和评估

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/c3c92220d68eff51f36de69c98510e350e8bdafe/img/md_need/LeNet%E6%A8%A1%E5%9E%8B.png" style="zoom: 67%;" />

```
loss 0.468, train acc 0.824, test acc 0.800
12518.1 examples/sec on cpu
Total training time: 47.93 seconds
```

# 第七章现代卷积神经网络

本章学习现代神经网络架构，有助于研究开发自己的架构

深度卷积神经网络发展的突破

```
Image Net挑战赛推动计算机视觉和机器学习的发展
GPU补充计算资源
```

AlexNet横空出世首次证明学习到的特征可以超越手动设计的特征一举打破计算机视觉研究现状



