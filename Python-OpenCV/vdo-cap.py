import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0, 0, 255),2)
        cv2.putText(frame, 'OpenCV', ((x+h), y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('frame',frame)
    #cv2.imshow('gray', gray)

    key = cv2.waitKey(20)
    if key == 27:
      break

cap.release()
cv2.destroyAllWindows()