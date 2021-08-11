#import torch
import torchvision.transforms as transforms
from torchvision.transforms.transforms import ColorJitter, RandomCrop, RandomGrayscale, RandomHorizontalFlip, RandomRotation, Resize, ToPILImage, ToTensor
from torchvision.utils import save_image
from data_loader import ImageDataset
from torch.utils.data import DataLoader

trans = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((256,256)),
    #transforms.RandomCrop((224,224)),
    #transforms.ColorJitter(brightness = 0.3),
    #transforms.RandomRotation(degrees = 45) , 
    transforms.RandomVerticalFlip(p=0.5),
    transforms.RandomGrayscale(p=0.1),
    transforms.RandomHorizontalFlip(p = 0.5),
    transforms.ToTensor()
    
])


dataset = DataLoader(ImageDataset(root_dir='D:\\work\\projects\\3D-Crater\\Dataset\\Total' , transform=trans))
count = 0
'''for img in dataset :
    img_num = 0
    while img_num < 10 :
        save_image( img,'resized_img/img' +str(count) + str(img_num) + '.png')
        img_num += 1
    count += 1'''
    
img_num = 0
while img_num < 5 :
    count = 0
    for img in dataset:
        save_image( img,'D:/work/projects/3D-Crater/Dataset/augmented_images/img' +str(count) + str(img_num) + '.png')
        count +=1
    img_num += 1