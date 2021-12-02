import cv2


cap=cv2.VideoCapture(0)

face=cv2.CascadeClassifier("face.xml")
eye=cv2.CascadeClassifier("eye.xml")

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face.detectMultiScale(gray,1.3,4)

    for (x,y,w,h)in faces:  
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    frame2=frame[y:y+h,x:x+w] 
    gray2=gray[y:y+h,x:x+w] 
    
    eyes=eye.detectMultiScale(gray,1.3,4)
    for (ex,ey,ew,wh) in eyes:
         cv2.rectangle(frame,(ex,ey),(ex+ew,ey+wh),(0,255,0),2)
         
    cv2.imshow("frame",frame)
    if cv2.waitKey(30)==27:
         break
     
     
cap.relase()
cv2.destroyAllWindows()
     
        