from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np
writer=SummaryWriter("../logs")
img_path= "/I-am-tudui/Dataset/data\\hymenoptera_data\\train\\bees\\39747887_42df2855ee.jpg"
img_PIL=Image.open(img_path)
img_array=np.array(img_PIL)
print(type(img_array))
print(img_array.shape)
writer.add_image("iamge",img_array,0,dataformats='HWC')
# writer.add_image()

writer.close()