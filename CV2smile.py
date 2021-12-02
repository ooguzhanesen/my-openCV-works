import cv2 

face=cv2.CascadeClassifier("face.xml")
 
smile=cv2.CascadeClassifier("smile.xml")

img=cv2.imread("smile.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face.detectMultiScale(gray,1.4,5)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
img2=img[y:y+h,x:x+w]  
gray2=gray[y:y+h,x:x+w]   
similes=smile.detectMultiScale(gray2,1.4,5)  

for (ex,ey,ew,eh) in similes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,255,0),2) 

 
    
    
    
    
    
    
cv2.imshow("img",img)    
cv2.waitKey(0)
cv2.destroyAllWindows()