from torch.utils.data import DataLoader
import torch
from torch import optim
from net import Net1
from data import MINIST_Data
from tqdm import tqdm
import time
from torch.utils.tensorboard import SummaryWriter

DEVICE = "cuda:0"
class Train():
    def __init__(self):
        self.summarywriter = SummaryWriter("./logs")
        self.train_data = MINIST_Data(r"D:\dataset\MNIST_IMG")
        self.train_dataloader = DataLoader(self.train_data,batch_size=100,shuffle=True)

        self.test_data = MINIST_Data(r"D:\dataset\MNIST_IMG",False)
        self.test_dataloader = DataLoader(self.test_data,batch_size=100,shuffle=True)

        self.net = Net1()
        self.net.to(DEVICE)

        self.opt = optim.Adam(self.net.parameters())
    def __call__(self, *args, **kwargs):
        for epoch in range(10000):
            trainloss_sum = 0
            for i,(train_img,train_label) in enumerate(tqdm(self.train_dataloader)):
                train_img, train_label = train_img.to(DEVICE),train_label.to(DEVICE)
                y = self.net(train_img)
                loss = torch.mean((y-train_label)**2)

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                trainloss_sum += loss.detach().item()
            avg_trainloss = trainloss_sum/len(self.train_dataloader)

            test_losssum = 0
            score = 0
            for i,(test_img,test_lable) in enumerate(tqdm(self.test_dataloader)):
                test_img, test_lable = test_img.to(DEVICE),test_lable.to(DEVICE)
                y = self.net(test_img)
                loss = torch.mean((y-test_lable)**2)
                test_losssum += loss.item()

                y_pred = torch.argmax(y,dim=-1)
                y_lable = torch.argmax(test_lable,dim=-1)
                score += torch.sum(torch.eq(y_pred,y_lable).float())
            accuracy = score/len(self.test_data)
            avg_testloss = test_losssum/len(self.test_dataloader)
            print(f"{epoch},train_loss:{avg_trainloss},test_loss:{avg_testloss},accuracy:{accuracy}")
            self.summarywriter.add_scalars("loss",{"train_loss":avg_trainloss,"test_loss":avg_testloss},epoch)
            self.summarywriter.add_scalar("score",accuracy,epoch)
            torch.save(self.net.state_dict(),f"./checkpoint/{epoch}.t")
            time.sleep(0.1)


if __name__ == '__main__':
    train = Train()
    train()
