from torchvision import datasets,transforms
from torch.utils.data import Dataset
import os,cv2,torch
import numpy as np

class MINIST_Data(Dataset):
    def __init__(self,path,is_train=True):
        super().__init__()
        self.dataset = []
        # path = r"D:\dataset\MNIST_IMG"
        dir_name = "TRAIN" if is_train else "TEST"
        dir_sub = os.path.join(path,dir_name)
        for tag in os.listdir(dir_sub):
            dir_img = os.path.join(dir_sub,tag)
            for img in os.listdir(dir_img):
                img_path = os.path.join(dir_img,img)
                self.dataset.append((img_path,tag))
    def __len__(self):
        return len(self.dataset)
    def __getitem__(self, item):
        data = self.dataset[item]
        img_data = cv2.imread(data[0],0)

        # img_data = img_data.reshape(28,28,1)
        # img_data = img_data.transpose(2,0,1)/255
        # img_data = img_data.astype(dtype=np.float32)
        # img_data = torch.from_numpy(img_data)
        # print(img_data.dtype)

        decode = transforms.ToTensor()
        img_data = decode(img_data)

        one_hot = torch.zeros(10)
        one_hot[int(data[1])] = 1
        return img_data,one_hot

if __name__ == '__main__':
    data = MINIST_Data(r"D:\dataset\MNIST_IMG")
    print(data[40000][0].shape)
    print(len(data))

