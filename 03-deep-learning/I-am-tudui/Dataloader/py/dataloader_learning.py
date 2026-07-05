import torch
import torchvision.datasets
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_set=torchvision.datasets.CIFAR10("../dataset", train=False, transform=torchvision.transforms.ToTensor(), download=True)
test_loader=DataLoader(dataset=test_set,batch_size=64,shuffle=True,num_workers=0,drop_last=True)
img,target=test_set[0]
print(img.shape)
print(target)
write=SummaryWriter("../logs")
for epoch in range(2):
    step=0
    for data in test_loader:
        imgs,targets=data
        # print(imgs.shape)
        # print(targets)
        write.add_images("epoch{}".format(epoch),imgs,step)
        step=step+1
write.close()


