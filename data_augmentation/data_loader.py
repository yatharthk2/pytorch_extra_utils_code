import os
import cv2
import torchvision.transforms as transforms
import torch
from torch.utils.data import Dataset
from skimage import io
from PIL import Image
from glob import glob
 

class ImageDataset(Dataset):
    def __init__(self,root_dir, transform=None):
        super(ImageDataset, self).__init__()
        self.root_dir = root_dir
        self.transform = transform
        self.paths = glob(f'{root_dir}/*')
        
    def __len__(self):
        return(len(self.paths))
    def __getitem__(self , index):
        #img_path = os.path.join(self.root_dir)
        img = io.imread(self.paths[index])
        #img = cv2.imread("data\HDR_FINAL.jpg", cv2.IMREAD_COLOR)
        #img = Image.open("data")
        
        
        if self.transform:
            image = self.transform(img)
            
        return (image)
        
        

