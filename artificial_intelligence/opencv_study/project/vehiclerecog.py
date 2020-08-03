import cv2

src = cv2.imread("../image/23.jpg")
# print(src.dtype)
img = cv2.GaussianBlur(src,(3,3),1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(img,-1,1,1)
sobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
Lap = cv2.Laplacian(img,-1)
#二值化
ret,sobelx = cv2.threshold(sobelx,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
ret,sobely = cv2.threshold(sobely,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
ret,sobel = cv2.threshold(sobel,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
ret,Lap = cv2.threshold(Lap,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# #形态学操作
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(17,5))
sobelx = cv2.morphologyEx(sobelx,cv2.MORPH_CLOSE,kernel)
# sobely = cv2.morphologyEx(sobely,cv2.MORPH_CLOSE,kernel)
# sobel = cv2.morphologyEx(sobel,cv2.MORPH_CLOSE,kernel)
# Lap = cv2.morphologyEx(Lap,cv2.MORPH_CLOSE,kernel)
kernelx = cv2.getStructuringElement(cv2.MORPH_RECT,(20,1))
kernely = cv2.getStructuringElement(cv2.MORPH_RECT,(1,19))
sobelx = cv2.dilate(sobelx,kernelx)
sobelx = cv2.erode(sobelx,kernelx)
sobelx = cv2.erode(sobelx,kernely)
sobelx = cv2.dilate(sobelx,kernely)
#平滑处理，中值滤波
sobelx = cv2.medianBlur(sobelx,3)
#查找轮廓
contour,dierarchy = cv2.findContours(sobelx,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for item in contour:
    x,y,w,h = cv2.boundingRect(item)
    if w>3*h:
        vehicle = src[y:y+h,x:x+w]
        cv2.imshow("vehicle",vehicle)

# contour,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# img_contour = cv2.drawContours(src,contour,-1,(0,0,255),2)
# ret,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# cv2.imshow("Lap",Lap)
cv2.imshow("sobelx",sobelx)
# cv2.imshow("sobely",sobely)
# cv2.imshow("sobel",sobel)
cv2.waitKey(0)