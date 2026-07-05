from torch.utils.data import Dataset
from PIL import Image
import os
class my_data(Dataset):
    def __init__(self,root_dir,label_dir):
        self.root_dir=root_dir
        self.label_dir=label_dir
        self.path=os.path.join(self.root_dir,self.label_dir)
        self.img_path=os.listdir(self.path)

    def __getitem__(self, idx):
        img_name=self.img_path[idx]
        img_path=os.path.join(self.root_dir,self.label_dir,img_name)
        img=Image.open(img_path)
        label=self.label_dir
        return img,label
    def __len__(self):
        return len(self.img_path)

root_dir= "/I-am-tudui/Dataset/data/hymenoptera_data/train"
ants_dir="ants"
bees_dir="bees"
ants_dataset=my_data(root_dir,ants_dir)
bees_dataset=my_data(root_dir,bees_dir)
bee_img,bee_label=bees_dataset[2]