import cv2
import numpy as np

url = 'rtsp://admin:admin@192.168.0.179:8554/live'
cap = cv2.VideoCapture(url)

while True:
    ret,frame = cap.read()
    low_val = np.array([0,43,46])
    high_val = np.array([10,255,255])
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv,low_val,high_val)
    contours,hierachy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    img_contour = cv2.drawContours(frame,contours,-1,(0,0,255))
    dst = cv2.bitwise_and(frame,frame,mask=mask)
    # cv2.imshow("dst",dst)
    # cv2.imshow("frame",frame)
    # cv2.imshow("mask",mask)
    if cv2.waitKey(40)&0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()