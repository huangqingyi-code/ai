from torchvision import datasets,transforms
import torch
import numpy
from torch.utils.data import DataLoader,Dataset

train_dataset = datasets.MNIST(root="MINIST_data",train=True,download=True,transform=transforms.ToTensor())
#transforms.ToTensor()
#Converts a PIL Image or numpy.ndarray (H x W x C) in the range
#[0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0]

test_dataset = datasets.MNIST(root="MINIST_data",train=False,download=True,transform=transforms.ToTensor())

# img = train_dataset[10][0]
# uncode = transforms.ToPILImage()
# img = uncode(img)
# img.show()
print(train_dataset[10][0])
# print(train_dataset.data[10])  #没有应用到__getitem__中的img = Image.fromarray(img.numpy(),mode="L")
# print(list(train_dataset))
# print(train_dataset.targets.shape)
# img = train_dataset.data[10]
# uncode = transforms.ToPILImage()   #tensor类型的数据转成PILImage类型
# img = uncode(img)

# print(type(train_dataset))  #<class 'torchvision.datas ets.mnist.MNIST'>

train_dataloader = DataLoader(train_dataset,batch_size=100,shuffle=True)
test_dataloader = DataLoader(test_dataset,batch_size=100,shuffle=True)

# for i,(img,label) in enumerate(train_dataloader):
# #TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists;
# # found <class 'PIL.Image.Image'>,train_dataloder是PIL类型。__getitem__里面设置的
#     print(img)