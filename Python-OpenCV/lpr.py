import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_licence_plate_rus_16stages.xml')
cap = cv2.VideoCapture('cam2.mp4')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    retval, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155,1)

    faces = face_cascade.detectMultiScale(threshold)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        #cv2.putText(frame, 'OpenCV', ((x + h), y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


    cv2.imshow('thresh', threshold)
    cv2.imshow('frame', frame)
    cv2.imshow('gaus', gaus)

    key = cv2.waitKey(20)
    if key == 27:
      break

cap.release()
cv2.destroyAllWindows()