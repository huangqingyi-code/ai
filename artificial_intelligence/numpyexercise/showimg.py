import os
# import matplotlib.pyplot as plt
# from PIL import Image
# name_list = os.listdir(r"D:\pycharm\pycharm project\artificial_intelligence\numpyexercise\image")
# plt.ion()
# for i in name_list:
#     img = Image.open(f"image/{i}")
#     plt.clf()
#     plt.imshow(img)
#     plt.pause(1)
#
# plt.ioff()
# plt.show()
import os
import matplotlib.pyplot as plt
from PIL import Image
path = r"D:\pycharm\pycharm project\artificial_intelligence\numpyexercise\image"
name_lst =os.listdir(path)
for i in name_lst:
    abs_path = os.path.join(path,i)
    img = Image.open(abs_path)
    plt.imshow(img)
    plt.show(block=False)
    plt.pause(1)
    # plt.cla()


