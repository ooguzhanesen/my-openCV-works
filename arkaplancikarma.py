import cv2
import numpy as np
 
cap=cv2.VideoCapture("car.mp4")

subtractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=75,detectShadows=True)#arka planı cıkarma


 
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480)) 
    mask=subtractor.apply(frame)
     
     
     
     
     
     
    cv2.imshow("mask",mask)
    cv2.imshow("frame",frame)
    if cv2.waitKey(30)==27:
         break
     
cap.relase()
cv2.destroyAllWindows()

