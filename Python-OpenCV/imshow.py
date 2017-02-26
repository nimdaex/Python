import cv2

while True:
    img = cv2.imread('OpenCV_Logo.png')
    cv2.imshow('image',img)
    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow('image')
