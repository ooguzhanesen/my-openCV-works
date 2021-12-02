import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("settings")

cv2.createTrackbar("lowe-hue","settings",0,180,nothing)
cv2.createTrackbar("lowe-saturation","settings",0,255,nothing)
cv2.createTrackbar("lowe-value","settings",0,255,nothing)
cv2.createTrackbar("upper-hue","settings",0,180,nothing)
cv2.createTrackbar("upper-saturation","settings",0,255,nothing)
cv2.createTrackbar("upper-value","settings",0,255,nothing)

font=cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos("lowe-hue","settings")
    ls=cv2.getTrackbarPos("lowe-saturation","settings")
    lv=cv2.getTrackbarPos("lowe-value","settings")
    uh=cv2.getTrackbarPos("upper-hue","settings")
    us=cv2.getTrackbarPos("upper-saturation","settings")
    uv=cv2.getTrackbarPos("upper-value","settings")
    
    lower_color=np.array([lh,ls,lv])
    upper_color=np.array([uh,us,uv])
    mask=cv2.inRange(hsv, lower_color,upper_color)
    
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.erode(mask,kernel)  # resimin beyaz kısımlarındakı siyah noktaları azaltmak için
    
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area= cv2.contourArea(cnt)# belli bir değernden küçukse çokgen arama
        epsilon=0.02*cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epsilon,True) #konturlara daha cok yaklaştık
        
        x=approx.ravel()[0]#konturların başladığı değerler
        y=approx.ravel()[1]
        if area>4000:
            cv2.drawContours(frame,[approx],0,(0,255,0),5)
            if len(approx)==3:
                cv2.putText(frame,"ucgen",(x,y),font,3,(255,0,45))
            elif len(approx)==4:
                cv2.putText(frame,"dortgen",(x,y),font,3,(255,0,45))
            elif len(approx)>6:
                cv2.putText(frame,"daire gibi bisey bu",(x,y),font,1,(255,0,45))
                      
         
    
    
    
    
    cv2.imshow("mas",mask)
    cv2.imshow("frame",frame)
    if cv2.waitKey(30)==27:
        break
    
cap.relase()
cv2.destroyAllWindows()    
        