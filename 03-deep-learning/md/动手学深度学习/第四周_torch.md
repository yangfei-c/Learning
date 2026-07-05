# 动手学深度学习10.7~10.13

## torchvision数据集使用

从torchvision下载数据集CIFAR10，按ctrl+p查看参数

```python
import torchvision
train_set=torchvision.datasets.CIFAR10("./dataset",train=True,download=True)
test_set=torchvision.datasets.CIFAR10("./dataset",train=False,download=True)
print(test_set[0])
输出如下
    Files already downloaded and verified
    Files already downloaded and verified
    (<PIL.Image.Image image mode=RGB size=32x32 at 0x1A7CA660BE0>, 3)
```

