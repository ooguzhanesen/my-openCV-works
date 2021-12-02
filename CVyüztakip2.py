import cv2 

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("face.xml")

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.4,4)#ölçek, pencere sayısı
    for(x,y,w,h)in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) 
    cv2.imshow("frame",frame)
    if cv2.waitKey(30)==27:
        break
    
cap.relase()
