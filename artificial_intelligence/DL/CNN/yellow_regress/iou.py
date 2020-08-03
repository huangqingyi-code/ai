# def cal_iou(x,y):
#     #1.左上角在框内
#     if x[0]<=y[0] and x[1]<=y[1]:
#         #右下角在框外
#         if x[2]<=y[2] and x[3]<=y[3]:
#             intersection = (x[2]-y[0])*(x[3]-y[1])
#             union = (x[2]-x[0])*(x[3]-x[1])+(y[2]-y[0])*(y[3]-y[1])-intersection
#             iou =intersection/(union)
#             return iou
#         #右下角在框内
#         elif x[2]>=y[2] and x[3]>=y[3]:
#             intersection = (y[2]-y[0])*(y[3]-y[1])
#             union = (x[2]-x[0])*(x[3]-x[1])
#             iou =intersection/(union)
#             return iou
#         elif x[2] >= y[2] and x[3] <= y[3]:
#             intersection = (y[2] - y[0]) * (x[3] - y[1])
#             union = (x[2] - x[0]) * (x[3] - x[1]) + (y[2] - y[0]) * (y[3] - y[1]) - intersection
#             iou = intersection / (union)
#             return iou
#         elif x[2] <= y[2] and x[3] >= y[3]:
#             intersection = (x[2] - y[0]) * (y[3] - y[1])
#             union = (x[2] - x[0]) * (x[3] - x[1]) + (y[2] - y[0]) * (y[3] - y[1]) - intersection
#             iou = intersection / (union)
#             return iou
#     #左上角在框左边


from PIL import Image, ImageDraw
# 交并比 获取两组坐标的IOU均值，如果是列表获取列表均值
# 左上坐标系
#       a矩形框的左上角点：a[0], a[1]
#       a矩形框的右下角点：a[2], a[3]
#       b矩形框的左上角点：b[0], b[1]
#       b矩形框的右下角点：b[2], b[3]
import torch
def cal_iou(a,b):
    x_min1, y_min1, x_max1, y_max1 = a[0], a[1], a[2], a[3]
    x_min2, y_min2, x_max2, y_max2 = b[0], b[1], b[2], b[3]

    x_min = max(x_min1, x_min2)  # 求交集部分左上角的点
    y_min = max(y_min1, y_min2)
    x_max = min(x_max1, x_max2)  # 求交集部分右下角的点
    y_max = min(y_max1, y_max2)
    if x_min >= x_max or y_min >= y_max:
        return torch.tensor(0.)   #不能.item()
    s1 = (x_max1 - x_min1) * (y_max1 - y_min1)  # 计算输入的两个矩形的面积
    s2 = (x_max2 - x_min2) * (y_max2 - y_min2)
    s = s1 + s2  # 计算两个输入框总面积
    inter_area = (x_max - x_min) * (y_max - y_min)  # 计算交集
    iou_num = inter_area / (s - inter_area)
    return torch.tensor(0.) if iou_num <= 0 else iou_num.cpu()  # 小于0或=0说明没有交集


# 循环多组坐标点 求IOU均值
def multi_iou(x_box, y_box):
    sum_score = 0
    num = len(x_box)
    for a, b in zip(x_box, y_box):
        sum_score += cal_iou(a, b)
    return sum_score / num


if __name__ == '__main__':
    # a = [[222, 7, 299, 84]]#不交
    a = [[117, 51, 186, 134]]
    b = [[79.09252, 88.69598, 153.04361, 161.03293]]
    print("multiple_iou   ", multi_iou(a, b))  # 多组坐标循环




