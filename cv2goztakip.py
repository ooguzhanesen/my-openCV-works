import cv2
import numpy as np



cap=cv2.VideoCapture("eye_motion.mp4")

while True:
    ret,frame=cap.read()
    
    if ret==False:
        break
    
    roi=frame[50:290,200:500]
    rows,cols,_=roi.shape
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,thresh=cv2.threshold(gray,1,255,cv2.THRESH_BINARY_INV)#SİYAH KISIMLARI BEYAZ YAPIYOR INV
    
    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x), reverse=True)    

    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)#kordinat çekme
        cv2.rectangle(roi,(x,y),(x+w,h+y),(255,0,45),2)
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,45),2)
        cv2.line(roi,(0,int(y+h/2)),(cols,int(y+h/2)),(0,255,45),2)
        break
    
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("gray",gray)
    cv2.imshow("thrash",thresh)
    
    
    
    
    
    if cv2.waitKey(50  )==27:
        break
    
cap.relase()
cv2.destroyAllWindows()