from data import *
from net import *
import torch
from torch.utils.data import DataLoader
from torch import optim
from torch.utils.tensorboard import SummaryWriter
import time
from tqdm import tqdm

DEVICE = "cuda:0"  #一台机子上可能有多个显卡
class Train():
    #获取数据
    def __init__(self,path):
        self.summartwriter = SummaryWriter("logs")
        #训练集
        self.data_train = MINI(path)
        self.data_trainloader = DataLoader(self.data_train,batch_size=100,shuffle=True)
        #shuffle打乱不放回抽样，batch_size每次训练100张图片,self.data_trainloader是一个迭代器

        #测试集
        self.data_test = MINI(path,False)
        self.data_testloader = DataLoader(self.data_test,batch_size=100)  #不用打乱

        #创建模型
        self.net = Net3()
        #加载参数
        # self.net.load_state_dict(torch.load("checkpoint/5.t"))

        #模型加载完参数后放在cuda上计算
        self.net.to(DEVICE)

        self.opt = optim.Adam(self.net.parameters())

    #训练代码
    def __call__(self):
        for epoch in range(100000):  #批次尽量大，事先不知道训练多少轮可以训练好，在训练过程中可以加判断条件loss，accuracy满足时停止训练
            loss_sum = 0
            for i,(img,target) in enumerate(tqdm(self.data_trainloader)):
                img,target = img.to(DEVICE),target.to(DEVICE)  #数据加载到cuda
                y = self.net(img)
                loss = torch.mean((y-target)**2)  #tensor平方，里面每个数据都会平方
                #tensor(0.1130, grad_fn=<MeanBackward0>)  里面含有变量要detach

                self.opt.zero_grad()
                loss.backward()    #求导的时候需要flaot(),否则会报错
                self.opt.step()
                loss_sum += loss.detach().cpu().item()   #item()只能将单个元素的tensor转成scalar，多个要用numpy()
            average_loss = loss_sum/len(self.data_trainloader)
            # print(epoch,average_loss)

            test_losssum = 0
            score = 0
            for i,(test_img,test_target) in enumerate(tqdm(self.data_testloader)):
                test_img,test_target = test_img.to(DEVICE),test_target.to(DEVICE)
                test_y = self.net(test_img)
                test_loss = torch.mean((test_y-test_target)**2).cpu().item()
                test_losssum += test_loss
                pre_tag = torch.argmax(test_y,dim=1)
                label_tag = torch.argmax(test_target,dim=1)
                score += torch.sum(torch.eq(pre_tag,label_tag).float())
            # print(len(self.data_test))
            # print(len(self.data_testloader))
            average_score = score/len(self.data_test)
            avg_testloss = test_losssum/len(self.data_testloader)
            end = time.time()
            print(epoch,"time:",end-start,"train_loss:", average_loss, "test_loss:", avg_testloss, "score:", average_score.item())
            self.summartwriter.add_scalars("loss",{"train_loss":average_loss,"test_loss":avg_testloss},epoch)
            self.summartwriter.add_scalar("score",average_score,epoch)
            #启用tensorboard：tensorboard --logdir=logs,训练完一次后清楚logs，否则图形会跟乱

            #保存参数
            torch.save(self.net.state_dict(),f"./checkpoint/{epoch}.t")
            #把每一轮的参数都保存下来，训练太多轮次过拟合时可以选择中间参数


if __name__ == '__main__':
    start = time.time()
    train = Train("D:\dataset\MNIST_IMG")
    train()