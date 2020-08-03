import cv2
import numpy as np

img = cv2.imread("image/1.jpg")
#线
# cv2.line(img,(100,200),(200,500),color=(255,0,0),thickness=2)   #thickness=-1表示填充
#矩形
cv2.rectangle(img,(100,200),(250,250),color=(0,0,255))
#圆
# cv2.circle(img,(60,60),50,color=(255,255,0))
#文字
# cv2.putText(img,"hello word",(50,60),cv2.FONT_HERSHEY_COMPLEX,1,(255,255),thickness=2,lineType=cv2.LINE_AA)  #LINE_AA抗锯齿
#椭圆
# cv2.ellipse(img,(100,100),(50,100),0,90,360,(255,0,0))
#多边形
# pts = np.array([[100,20],[30,40],[50,60],[200,300]])
# print(pts.shape)
# cv2.polylines(img,pts,True,color=(0,0,255))
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
