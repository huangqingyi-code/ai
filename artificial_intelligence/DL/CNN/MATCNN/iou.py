import torch


def single_iou(x, y):
    x1, x2, x3, x4 = x[0], x[1], x[2], x[3]
    y1, y2, y3, y4 = y[0], y[1], y[2], y[3]
    # 方框左上角的坐标(a1,a2)
    a1 = max(x1, y1)
    a2 = max(x2, y2)
    # 方框右下角的坐标(b1,b2)
    b1 = min(x3, y3)
    b2 = min(x4, y4)
    if a1 >= b1 or a2 >= b2:
        return 0
    intersection_are = (b1 - a1) * (b2 - a2)
    union = (x3 - x1) * (x4 - x2) + (y3 - y1) * (y4 - y2)
    iou = intersection_are / (union - intersection_are)
    return iou


# 求多个的平均iou
def multavg_iou(y, lable):
    n = len(y)
    score = 0
    for x_box, y_box in zip(y, lable):
        score += single_iou(x_box, y_box)
    return score / n


if __name__ == '__main__':
    x = [400.0000, 400.0000, 600.0000, 600.0000]
    y = [350.0000, 350.0000, 500.0000, 500.0000]
    # x = [[0,0,1,1],[0,0,1,1]]
    # y = [[2,2,3,3],[0.5,0.5,1,1]]
    # ret1 = multavg_iou(x, y)
    ret2 = single_iou(x, y)
    print(ret2)
