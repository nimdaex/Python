
import cv2
import urllib
import urllib.request
import numpy as np

stream=urllib.request.urlopen('http://10.1.11.54/video.cgi')
bytes=''
while True:
    bytes += stream.read(16384)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('i',i)
       
    key = cv2.waitKey(20)
    if key == 27:
      break

#cam.release()
cv2.destroyAllWindows()