from torch.utils.data import DataLoader
from torch import optim
from tqdm import tqdm
import torch,time
from data import Yellow_Data
from net import Net
from iou import multi_iou
from torch.utils.tensorboard import SummaryWriter

DEVICE = "cuda:0"


class Train():
    def __init__(self):
        self.summarywriter = SummaryWriter("./logs")

        self.train_dataset = Yellow_Data("D:\dataset\yellow_minion\img")
        self.train_dataloader = DataLoader(self.train_dataset, batch_size=60, shuffle=True)

        self.test_dataset = Yellow_Data("D:\dataset\yellow_minion\img", False)
        self.test_dataloader = DataLoader(self.test_dataset, batch_size=30)

        self.net = Net()
        self.net.to(DEVICE)

        self.opt = optim.Adam(self.net.parameters())

    def __call__(self):
        for epoch in range(10000):
            trainloss_sum = 0
            train_iousum = 0
            for i, (img, label) in enumerate(tqdm(self.train_dataloader)):
                img, label = img.to(DEVICE), label.to(DEVICE)
                y = self.net(img)
                # print(label.shape,y.shape)
                loss = torch.mean((y - label) ** 2)

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                trainloss_sum += loss.detach().cpu().item()
                iou = multi_iou(y, label).item()
                # print(type(iou))
                train_iousum += iou
                # print(type(train_iousum))
            train_iou = train_iousum / len(self.train_dataloader)
            avg_trainloss = trainloss_sum / len(self.train_dataloader)

            testloss_sum = 0
            testiou_sum = 0
            for i, (img, label) in enumerate(tqdm(self.test_dataloader)):
                img, label = img.to(DEVICE), label.to(DEVICE)
                y = self.net(img)
                loss = torch.mean((y - label) ** 2).cpu().item()

                testiou_sum += multi_iou(y, label).item()

                testloss_sum += loss
            avg_testloss = testloss_sum / len(self.test_dataloader)
            test_iou = testiou_sum / len(self.test_dataloader)
            if test_iou > 0.9:
                torch.save(self.net.state_dict(), f"./checkpoint/{epoch}.t")
            print(epoch, "train_loss:", avg_trainloss, "train_iou:", train_iou, "tess_loss:", avg_testloss, "test_iou:",
                  test_iou)
            time.sleep(0.5)

            self.summarywriter.add_scalars("loss", {"train_loss": avg_trainloss, "test_loss": avg_testloss}, epoch)
            self.summarywriter.add_scalars("iou", {"train_iou": train_iou, "test_iou": test_iou}, epoch)


if __name__ == '__main__':

    train = Train()
    train()