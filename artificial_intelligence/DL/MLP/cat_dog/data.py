from torch.utils.data import Dataset
import torch
import numpy as np
import os
import cv2


class AnimalData(Dataset):
    def __init__(self,path,is_trian=True):
        self.dataset = []
        name_list = os.listdir(path)
        for name in name_list:
            tag = name[0]
            img_path = os.path.join(path,name)
            self.dataset.append((img_path,tag))
        self.test_dataset = self.dataset[0:1200]+self.dataset[10800::]
        self.train_dataset = self.dataset[1200:10800]
        if is_trian:
            self.dataset = self.train_dataset
        else:
            self.dataset =  self.test_dataset
        # print(len(self.dataset))
    def __len__(self):
        return len(self.dataset)
    def __getitem__(self, item):
        img = cv2.imread(self.dataset[item][0],cv2.IMREAD_GRAYSCALE)
        # print(img.shape)
        # cv2.imshow("img",img)
        # cv2.waitKey(0)
        img_data = img.reshape(-1)/255
        img_data = torch.tensor(img_data,dtype=torch.float32)
        one_hot = int(self.dataset[item][1])
        # one_hot = torch.zeros(2)
        # one_hot[int(self.dataset[item][1])] = 1
        # print(img_data.shape)
        return img_data,one_hot

if __name__ == '__main__':
    animal = AnimalData(r"cat_dog\img")
    animal[1000]