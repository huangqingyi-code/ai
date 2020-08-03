from torch.utils.data import Dataset
import torch,os,cv2
from torchvision import transforms

class DogCat_Data(Dataset):
    def __init__(self,path,is_train=True):
        self.dataset = []
        name_list = os.listdir(path)
        for name in name_list:
            tag = name[0]
            img_path = os.path.join(path,name)
            self.dataset.append((img_path,tag))
        num = len(self.dataset)
        self.test_dataset = self.dataset[0:int(0.1*num)]+self.dataset[int(0.9*num)::]
        self.train_dataset = self.dataset[int(0.1*num):int(0.9*num)]
        if is_train:
            self.dataset = self.train_dataset
        else:
            self.dataset =  self.test_dataset
    def __len__(self):
        return len(self.dataset)
    def __getitem__(self, item):
        data = self.dataset[item]
        img = cv2.imread(data[0])

        decode = transforms.ToTensor()
        img = decode(img)

        one_hot = torch.zeros(2)
        one_hot[int(data[1])] = 1
        return img,one_hot

if __name__ == '__main__':
    data = DogCat_Data(r"D:\dataset\cat_dog\img")
    print(len(data))
    print(data[800][1].dtype)
