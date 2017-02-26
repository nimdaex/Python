import cv2
import numpy as np
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_licence_plate_rus_16stages.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(gray, 165, 255, cv2.THRESH_BINARY)
    gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155,1)

    faces = face_cascade.detectMultiScale(threshold, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(gaus, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(gaus, 'OpenCV', ((x + h), y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('thresh', threshold)
    cv2.imshow('gaus', gaus)

    key = cv2.waitKey(20)
    if key == 27:
      break

cap.release()
cv2.destroyAllWindows()