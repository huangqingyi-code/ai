import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

class Recognition():
    def __init__(self,path):
        self.img = cv2.imread(path)
    def get_plate(self):
        src =self.img
        src = cv2.GaussianBlur(src,(3,3),1)
        src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(src_gray,cv2.CV_16S,1,0)
        sobelx = cv2.convertScaleAbs(sobelx)
        ret, thresh = cv2.threshold(sobelx, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(17,5))
        thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=4)
        kernelx = cv2.getStructuringElement(cv2.MORPH_RECT,(19,1))
        kernely = cv2.getStructuringElement(cv2.MORPH_RECT,(1,19))
        thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernelx)
        thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernely)
        thresh = cv2.medianBlur(thresh,3)
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in contours:
            x,y,w,h = cv2.boundingRect(i)
            if w>3*h and w<5*h:
                plate = src[y:y+h,x:x+w]
        #         # cv2.imwrite("image/plate.jpg",plate)
        #         cv2.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
        #         cv2.imshow("src", plate)
                return plate
    def split(self):
        src = self.get_plate()
        img = cv2.GaussianBlur(src,(3,3),1)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
        img = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
        # img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel1)
        # img = cv2.dilate(img,kernel)
        contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  #数字内的轮廓不匹配
        # img_contour = cv2.drawContours(src,contours,-1,(0,0,255),1)
        # cv2.imshow("img_contour",img_contour)
        # cv2.waitKey(0)
        contour_list = []
        for i in contours:
            x,y,w,h = cv2.boundingRect(i)
            contour_list.append([x,y,w,h])
        contour_list.sort(key=lambda x:x[0])   #车牌是有序的
        split_list = []
        for i in contour_list:
            if (i[3]>i[2]*1.5)and(i[3]<i[2]*3.5):
                # cv2.rectangle(src,(i[0],i[1]),(i[0]+i[2],i[1]+i[3]),(0,0,255),1)
                # cv2.imshow("src",src)
                # cv2.waitKey(0)
                img0 = src[i[1]:i[1]+i[3],i[0]:i[0]+i[2]]
                # cv2.imshow(f"{i}", img0)
                # cv2.waitKey(0)
                split_list.append(img0)
        return split_list
    def match(self):
        split_list = self.split()
        template = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'A','B','C','D','E','F','G','H','J','K','L','M',
                    'N','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '藏','川','鄂','甘','赣','贵','桂','黑','沪','吉','冀',
                    '津','晋','京','辽','鲁','蒙','闽','宁','青','琼','陕','苏','皖','湘','新','渝','豫','粤','云','浙']
        #第一个中文字的匹配
        chines_name = []
        for i in range(34,64):
            provice_name = []
            for filename in os.listdir("refer1/"+template[i]):
                provice_name.append(f"./refer1/{template[i]}/{filename}")
            chines_name.append(provice_name)
        #二值化处理要匹配的文字
        img1 = split_list[0]
        dst1 = cv2.GaussianBlur(img1,(3,3),1)
        dst1 = cv2.cvtColor(dst1,cv2.COLOR_BGR2GRAY)
        ret,dst1 = cv2.threshold(dst1,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

        for i in chines_name:
            score = []
            for j in i:
                template_img = cv2.imdecode(np.fromfile(j,dtype=np.uint8),1)
                template = cv2.cvtColor(template_img,cv2.COLOR_BGR2GRAY)
                template = cv2.GaussianBlur(template,(3,3),1)
                ret,template = cv2.threshold(template,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
                cv2.imshow("template",template)
                cv2.waitKey(0)
                exit()
        cv2.imshow("dst1",dst1)
        cv2.waitKey(0)

        print(chines_name)


car = Recognition("image/test2.png")
img = car.match()
# cv2.imshow("img",img)
# cv2.waitKey(0)