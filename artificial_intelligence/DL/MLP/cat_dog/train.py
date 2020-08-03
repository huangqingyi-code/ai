import torch
from torch.utils.data import DataLoader
from data import AnimalData
from net import Net
from torch import optim
from tqdm import tqdm
import time
import numpy as np

DEVICE = "cuda:0"


class Train():
    def __init__(self):
        self.train_dataset = AnimalData(r"D:\dataset\cat_dog\img")
        self.train_dataload = DataLoader(self.train_dataset, batch_size=100, shuffle=True)

        self.test_dataset = AnimalData(r"D:\dataset\cat_dog\img", False)
        self.test_dataload = DataLoader(self.test_dataset, batch_size=100, shuffle=True)

        self.net = Net()
        self.net.to(DEVICE)

        self.opt = optim.Adam(self.net.parameters())

    def __call__(self):
        for epoch in range(10000):
            loss_train = 0
            for i, (train_img, train_tag) in enumerate(tqdm(self.train_dataload)):
                train_img, train_tag = train_img.to(DEVICE), train_tag.to(DEVICE)
                y = self.net(train_img)
                # print(y)
                loss = torch.mean((y - train_tag[:, None]) ** 2)

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                loss_train += loss.detach().cpu().item()
            avg_trainloss = loss_train / len(self.train_dataload)

            test_loss = 0
            test_score = 0
            for i, (test_img, test_tag) in enumerate(tqdm(self.test_dataload)):
                test_img, test_tag = test_img.to(DEVICE), test_tag.to(DEVICE)
                y = self.net(test_img)
                # print(test_tag,y)
                loss = torch.mean((y - test_tag[:, None]) ** 2).cpu().item()
                test_loss += loss
                # pre_tag = torch.argmax(y,dim=1)
                # label_tag = torch.argmax(test_tag,dim=1)
                # score = torch.sum(torch.eq(pre_tag,label_tag).float())

                # y = y.cpu().detach().numpy()    #要转成numpy要先转到cpu运算
                # y = np.where(y>=0.5,1,0)
                # y = torch.from_numpy(y)
                y[y >= 0.5] = 1
                y[y < 0.5] = 0

                # print(y,test_tag[:,None])
                score = torch.sum(torch.eq(y, test_tag[:, None]).float())
                test_score += score
                # print(test_score)
            avg_testloss = test_loss / len(self.test_dataload)
            avg_score = test_score / len(self.test_dataset)
            print(f"{epoch},avg_trainloss:{avg_trainloss},avg_testloss:{avg_testloss},avg_score:{avg_score}")
            # print(epoch,"avg_trainlos:",avg_trainloss,"avg_testloss:",avg_testloss,"avg_score:",avg_score)

            time.sleep(0.1)


if __name__ == '__main__':
    train = Train()
    train()
