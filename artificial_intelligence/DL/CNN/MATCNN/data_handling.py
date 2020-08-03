from PIL import Image, ImageDraw
import os, random
from iou import single_iou
from itertools import islice
import matplotlib.pylab as plt
import numpy as np

img_src = r"D:\dataset\CelebA\Img\img_celeba.7z\img_celeba"
anno_src = "D:\dataset\CelebA\Anno\list_bbox_celeba.txt"

dst_path = r"D:\dataset\CelebA\img_face"
negative_sample = os.path.join(dst_path, "negative_sample")
positive_sample = os.path.join(dst_path, "positive_sample")
part_face = os.path.join(dst_path, "part_face")
anno_file = os.path.join(dst_path, "anno_file")

# with open("data/test.txt",mode="r",encoding="utf-8") as f1:
#     for i in islice(f1,2,None):  #读取文本中行索引为[2:]
#         print(i)

with open("data/test.txt", mode="r", encoding="utf-8") as f1:
    for num, content in enumerate(f1):
        if num < 2:
            continue
        content = content.strip().split()
        x = int(content[1])
        y = int(content[2])
        w = int(content[3])
        h = int(content[4])

        if max(w, h) < 40 or x < 0 or y < 0 or w < 0 or h < 0:
            continue

        img_path = os.path.join(img_src, content[0])
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        draw.rectangle((x, y, x + w, y + h), outline=(255, 0, 0), width=2)
        # img.show()

        for i in range(5):
            center_x = x + w / 2
            center_y = y + h / 2
            print(center_x,center_y)
            w_ = np.random.randint(-0.2 * w, 0.2 * w)
            h_ = np.random.randint(-0.2 * h, 0.2 * h)
            center_x = center_x + w_
            center_y = center_y + h_
            print(center_x, center_y)

            # draw.rectangle((center_x-w,center_y-h,center_x+w,center_y+h),outline=(0,0,255),width=2)
            img.show()