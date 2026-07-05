# 动手学深度学习10.14~10.20

## 模型验证

### 轮数为10轮，学习率为0.005的情况下准确率约47%

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E4%BD%8E%E5%87%86%E7%A1%AE%E7%8E%87%E9%AA%8C%E8%AF%81.png" alt="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E4%BD%8E%E5%87%86%E7%A1%AE%E7%8E%87%E9%AA%8C%E8%AF%81.png" style="zoom: 25%;" />

```
对猫进行预测，得到索引为5，但实际上猫的索引为三所以预测错误
```

![](https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/%E4%BD%8E%E5%87%86%E7%A1%AE%E7%8E%87%E5%AF%B9%E9%A3%9E%E6%9C%BA%E8%BF%9B%E8%A1%8C%E9%A2%84%E6%B5%8B.png)

```
同时该模型下对飞机预测，预测正确
```

### 轮数为30轮，学习率为0.005的情况下准确率约61%

<img src="https://gitee.com/yangfeiChen/DeepLearning/raw/master/img/md_need/30%E8%BD%AE%E9%A2%84%E6%B5%8B%E7%8C%AB.png" style="zoom: 25%;" />

```
还是预测为索引5即狗，但此时可以看到索引3和索引5概率相差不大
```

