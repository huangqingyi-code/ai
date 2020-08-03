import torch,cv2,os
import numpy as np
from torch.utils.data import Dataset

class MINI(Dataset):
    def __init__(self,path,is_train=True):
        self.dataset = []
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{path}/{sub_dir}"):
            img_dir = f"{path}/{sub_dir}/{tag}"
            for img in os.listdir(img_dir):
                img_path = os.path.join(img_dir,img)
                self.dataset.append((img_path,int(tag)))
    def __len__(self):
        return len(self.dataset)
    def __getitem__(self, item):
        data = self.dataset[item]
        img = cv2.imread(data[0],cv2.IMREAD_GRAYSCALE)
        img_data = img.reshape(-1)
        img_data = img_data/255
        one_hot = np.zeros(10)
        one_hot[data[1]] = 1
        # img_data = torch.from_numpy(img_data,dtype=torch.float32)   #数据要转换成torch.float32
        img_data = torch.tensor(img_data,dtype=torch.float32)
        # one_hot = torch.from_numpy(one_hot,dtype=torch.float32)
        one_hot = torch.tensor(one_hot,dtype=torch.float32)
        return img_data,one_hot
if __name__ == "__main__":
    datasets = MINI("D:\dataset\MNIST_IMG")
    # print(len(datasets))
    print(datasets[2000][1])
