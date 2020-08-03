import torch,numpy
from torchvision import transforms
from PIL import Image,ImageDraw
from torch.utils.data import DataLoader
from net import Net
from data import Yellow_Data

if __name__ == '__main__':
    net = Net()
    net.load_state_dict(torch.load("checkpoint_rec/3.t"))
    data = Yellow_Data("D:\dataset\yellow_minion\img_rectangle", False)
    data_loader = DataLoader(data,batch_size=1,shuffle=True)
    for i,(img,label) in enumerate(data_loader):
        y = net(img)
        y = y.detach().numpy()*300
        label = label.detach().numpy()*300
        print(y,label)

        decode = transforms.ToPILImage()
        img = torch.squeeze(img)
        img = decode(img)
        print(img.mode)
        # img = Image.fromarray(img,mode="RGB")
        draw = ImageDraw.Draw(img)
        draw.rectangle(y,outline=(255,0,0),width=2)
        draw.rectangle(label,outline=(0,255,0),width=2)
        img.show()




