import cv2
import numpy as np
from PIL import Image
#读取图像
# img = cv2.imread("img/1.jpg")    #<class 'numpy.ndarray'>，后面可以0表示灰度图
# img = img[...,::-1]     #PIL是RGB通道，CV2是BGR
# img = Image.fromarray(img)
# img.show()

# print(img.shape)
# cv2.imshow("hainan",img)    #用opencv自带的窗口显示图片，是个非阻塞方法
# cv2.waitKey(10000)    #0表示一直开着，其他数字表示毫秒
# cv2.destroyAllWindows()  #关闭所有窗口

#图片创建
# import numpy as np
# import cv2
# img = np.zeros((200,300,3),dtype=np.uint8)
# img[...,] = [255,255,255]
# cv2.imwrite("img.jpg",img)
# cv2.imshow("img",img)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()

#视频读取  本地视频/文件流
#创建视频对象
# url = 'rtsp://admin:admin@192.168.0.179:8554/live'
# cap = cv2.VideoCapture(url)   #读取手机摄像头
cap = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv6hd.m3u8")  #0,1表示前置和后置摄像头
while True:
    ret,frame = cap.read()  #ret bool类型，表示视频是否读取成功；frame每帧的画面
    cv2.imshow("frame",frame)
    if cv2.waitKey(40) & 0xFF == ord("q"):  #若此参数置零，则代表在捕获并显示了一帧图像之后，程序将停留在if语句段中一直
                                            # 等待 ‘q’ 被键入。检测在上一次显示图像的时间段内按键 ‘q’ 有没有被按下
        break                               #cv2.waitKey(1) 与 0xFF（1111 1111）相与是因为cv2.waitKey(1) 的返回值
                                            # 不止8位，但是只有后8位实际有效，为避免产干扰，通过 ‘与’ 操作将其余位置0。
cap.release()
cv2.destroyAllWindows()