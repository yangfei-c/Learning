from PIL import Image
from torch.utils.tensorboard import SummaryWriter

from torchvision import transforms

img_path= "/I-am-tudui/Dataset/data\\hymenoptera_data\\train\\ants\\6240329_72c01e663e.jpg"
img=Image.open(img_path)
write=SummaryWriter("../logs")
print(img)
img_tensor=transforms.PILToTensor()
tensor_img=img_tensor(img)
print(tensor_img.type())
write.add_image("tensor_img",tensor_img)
write.close()