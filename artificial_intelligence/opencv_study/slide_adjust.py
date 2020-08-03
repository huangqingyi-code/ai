import cv2

# 定义回调函数，此程序无需回调，所以Pass即可
def callback(object):
    pass
cv2.namedWindow("thresh")
cv2.createTrackbar("low_val","thresh",127,255,callback)
img = cv2.imread("image/1.jpg", 0)
while True:
    x = cv2.getTrackbarPos("low_val","thresh")
    ret, binary = cv2.threshold(img, x, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresh", binary)
    if cv2.waitKey(40)&0xFF == ord("q"):
        break
cv2.destroyAllWindows()