import cv2
import numpy as np

cap=cv2.VideoCapture("line.mp4")


while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    LW=np.array([18,94,140],)
    UW=np.array([48,255,255],)
    mask=cv2.inRange(hsv,LW,UW)
    edges=cv2.Canny(mask,75,250)
 
 
   
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    if cv2.waitKey(30)==27:
        break
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,255),5)
    cv2.imshow("mask",frame)
    cv2.imshow("original",edges)    
cap.release()
cv2.destroyAllWindows()     