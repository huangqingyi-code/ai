import torch
from torch.utils.data import DataLoader
from data import DogCat_Data
from net import Net1
from torch import optim
import time
from tqdm import tqdm

DEVICE = "cuda:0"


class Train():
    def __init__(self):
        self.train_dataset = DogCat_Data(r"D:\dataset\cat_dog\img")
        self.train_dataload = DataLoader(self.train_dataset, batch_size=100, shuffle=False)

        self.test_dataset = DogCat_Data(r"D:\dataset\cat_dog\img", False)
        self.test_dataload = DataLoader(self.test_dataset, batch_size=100, shuffle=True)

        self.net = Net1()
        # print(self.net.params)
        self.net.to(DEVICE)

        self.opt = optim.Adam(self.net.parameters(),lr=0.001)

    def __call__(self):
        for epoch in range(10000):
            loss_train = 0
            for i, (train_img, train_tag) in enumerate(tqdm(self.train_dataload)):
                train_img, train_tag = train_img.to(DEVICE), train_tag.to(DEVICE)
                y = self.net(train_img)
                loss = torch.mean((y - train_tag) ** 2)
                # print(y.shape,train_tag.shape)
                print("loss:",loss.item())

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
                # print("y:",y)
                # print(test_tag.shape,y.shape)
                loss = torch.mean((y - test_tag) ** 2).cpu().item()
                test_loss += loss
                pre_tag = torch.argmax(y, dim=1)
                label_tag = torch.argmax(test_tag, dim=1)
                score = torch.sum(torch.eq(pre_tag, label_tag).float())
                test_score += score

            avg_testloss = test_loss / len(self.test_dataload)
            avg_score = test_score / len(self.test_dataset)
            print(f"{epoch},avg_trainloss:{avg_trainloss},avg_testloss:{avg_testloss},avg_score:{avg_score}")
            # print(epoch,"avg_trainlos:",avg_trainloss,"avg_testloss:",avg_testloss,"avg_score:",avg_score)
            torch.save(self.net.state_dict(), f"./checkpoints/{epoch}.t")

            time.sleep(0.1)


if __name__ == '__main__':
    train = Train()
    train()
