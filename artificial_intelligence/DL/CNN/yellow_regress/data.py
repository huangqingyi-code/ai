from torch.utils.data import Dataset
import torch, random, os, cv2
from torchvision import datasets, transforms
from PIL import Image


class Yellow_Data(Dataset):
    def __init__(self, path, is_train=True):
        self.dataset = []
        name_list = os.listdir(path)
        for name in name_list:
            # num = name.split(".")[0]
            img_path = os.path.join(path, name)
            lable = name.split(".")[1:5]
            lable = [int(x) / 300 for x in lable]
            # print(table)
            self.dataset.append((img_path, lable))
        random.seed(0)
        random.shuffle(self.dataset)
        num = len(self.dataset)
        self.train_dataset = self.dataset[:int(num * 0.8)]
        self.test_dataset = self.dataset[int(num * 0.8):]
        if is_train:
            self.dataset = self.train_dataset
        else:
            self.dataset = self.test_dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, item):
        img = self.dataset[item]
        img_data = Image.open(img[0])
        decode = transforms.ToTensor()
        img_data = decode(img_data)
        lable = torch.tensor(img[1], dtype=torch.float32)
        return img_data, lable


if __name__ == '__main__':
    data = Yellow_Data("D:\dataset\yellow_minion\img_rectangle", False)
    # print(data[100][0])
    # print(len(data))
    img = data[100][0]
    encode = transforms.ToPILImage()
    img = encode(img)
    img.show()