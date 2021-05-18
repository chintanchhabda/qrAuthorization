from pyzbar.pyzbar import decode
import cv2
import numpy as np


capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

with open('myData') as f:
    dataList = f.read().splitlines()

while True:
    success, image = capture.read()
    for info in decode(image):
        codeData = info.data.decode('utf-8')
        print(codeData)
        if codeData in dataList:
            Output = 'Authorised'
        else:
           Output = 'Unauthorised'
        points = np.array([info.polygon],np.int32)
        points = points.reshape((-1,1,2))
        cv2.polylines(image, [points],True,(0,255,0),5)

        cv2.putText(image,Output,(info.rect[0],info.rect[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,255,0),2)

    cv2.imshow('Output',image)
    cv2.waitKey(1)
