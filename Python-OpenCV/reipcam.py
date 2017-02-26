import cv2
import numpy as np


cam = cv2.VideoCapture('rtsp://admin:304048215076@192.168.1.108:554')

while True:
    ret, frame=cam.read()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.imshow('frame',frame)

    key = cv2.waitKey(20)
    if key == 27:
      break

#cam.release()
#cv2.destroyAllWindows()