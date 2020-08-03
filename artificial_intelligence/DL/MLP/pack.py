from torch import jit
from net import Net3
import torch

if __name__ == '__main__':
    model = Net3()
    model.load_state_dict(torch.load("checkpoint/5.t"))

    #虚拟一个输入（占位）
    input = torch.randn(1,784)
    torch_module = jit.trace(model,input)
    torch_module.save("minist_net.pt")