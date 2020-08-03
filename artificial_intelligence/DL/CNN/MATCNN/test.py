# import tensorflow
from mtcnn import MTCNN
import cv2
img = cv2.cvtColor(cv2.imread("data/000001.jpg"), cv2.COLOR_BGR2RGB)
detector = MTCNN()
# ret = detector.detect_faces(img)
# print(ret)
