import torch
from iou import single_iou
import numpy as np
import cv2
from PIL import Image, ImageDraw


# y = y_predict[y_predict[:,-1].argsort()]
# y_predict[:,-1].argsort()   #tensor([3, 5, 1, 2, 4, 0])从小到大的index


def nms_box(box):
    threshold = 0.2
    target = []
    while True:
        box = box[box[:, -1].argsort()]
        target.append(box[-1])
        remain = []
        for x in box[:-1]:
            ret = single_iou(x[0:4], box[-1][0:4])
            if ret <= threshold:
                remain.append(x)
        if remain:
            box = torch.stack(remain)
        else:
            return target


if __name__ == '__main__':
    y = torch.tensor([[100, 100, 300, 300, 0.95],
                      [50, 50, 250, 400, 0.8],
                      [100, 100, 250, 400, 0.85],
                      [350, 350, 500, 500, 0.4],
                      [400, 400, 600, 600, 0.9],
                      [350, 350, 500, 500, 0.7]])
    ret = nms_box(y)
    print(ret)
    img = np.zeros((800, 800, 3), dtype=np.uint8)
    img[...,] = [255, 255, 255]
    for i in ret:
        rec = i.numpy()
        cv2.rectangle(img, (rec[0], rec[1]), (rec[2], rec[3]), color=(0, 255, 0), thickness=2)
    # for i in y:
    #     rec = i.numpy()
    #     cv2.rectangle(img,(rec[0],rec[1]),(rec[2],rec[3]),color=(0,0,255),thickness=2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
