import torch

print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.version.cuda)
print(torch.__version__)

#nvidia-smi.exe -l 3  查看显卡使用率