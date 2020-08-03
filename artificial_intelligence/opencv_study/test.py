import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

src = cv2.imread("image/3.jpg")
src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(src_gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
contours,hierachy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# perimeter = cv2.arcLength(contours[0],True)
# print(perimeter)
# epsilon = 0.02*perimeter
# approx = cv2.approxPolyDP(contours[0],epsilon,True)
# img_contour = cv2.drawContours(src,[approx],-1,(0,0,255),2)

# x,y,w,h = cv2.boundingRect(contours[0])
# cv2.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)

rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
print(box)

cv2.imshow("src",src)
cv2.waitKey(0)