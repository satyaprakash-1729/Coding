import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('../../data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../../data/haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('../../data/haarcascades/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(roi_gray,scaleFactor=1.7,minNeighbors = 15, minSize=(25,25),flags=0)
        for (ex,ey,ew,eh) in smile:
            cv2.imwrite("written.jpg",img)
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()