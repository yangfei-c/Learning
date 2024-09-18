import matplotlib.pyplot as plt
import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l

d2l.use_svg_display()
#读取数据集
trans=transforms.ToTensor()
mnist_train=torchvision.datasets.FashionMNIST(
    root="../data",train=True,transform=trans,download=True)
mnist_test=torchvision.datasets.FashionMNIST(
    root="../data",train=False,transform=trans,download=True)
#训练6000张图像，测试1000张图象
#print("train:"+str(len(mnist_train)),"test:"+str(len(mnist_test)))
#灰度图，通道为1，高宽28x28
#print(mnist_test[0][0].shape)

def get_fashion_mnist_labels(labels):
    text_labels=['t-shirt','trouser','pullover','dress','coat'
                 ,'sandal','shirt','sneaker','bag','ankle boot']
    #将标签转换为对应的服装类别
    return [text_labels[int(i)] for i in labels]

def show_images(imgs,num_rows,num_cols,titles=None,scale=1.5):
    figsize=(num_cols*scale,num_rows*scale)
    _,axes=d2l.plt.subplots(num_rows,num_cols,figsize=figsize)
    axes=axes.flatten()
    for i,(ax,img) in enumerate(zip(axes,imgs)):
        #axes = [ax1, ax2, ax3]，imgs = [img1, img2, img3]
        #zip(axes, imgs)会产生如下结果：[(ax1, img1), (ax2, img2), (ax3, img3)]
        #enumerate(zip(axes, imgs))，第一次迭代：i = 0, ax = ax1, img = img1
        if torch.is_tensor(img):
            ax.imshow(img.numpy())
        else:
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes

X,y=next(iter(data.DataLoader(mnist_train,batch_size=18)))
show_images(X.reshape(18,28,28),2,9,titles=get_fashion_mnist_labels(y))
#plt.show()