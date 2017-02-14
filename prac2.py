import numpy as np
import os
import sys
import cv2
face_cascade = cv2.CascadeClassifier('../../data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../../data/haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('../../data/haarcascades/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
dfg=False
count = 0
flag = False
while True and cap:
    _,img = cap.read()
    rty = True
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 6)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eye = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.1,minNeighbors = 10, minSize=(15,15),flags=0)
        for (ex,ey,ew,eh) in eye:
            rty=False
            dfg=True
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        if rty and dfg:
            count+=1
            dfg = False
            print count
    if count==10 and flag==False:
        flag = True
        cv2.destroyAllWindows()
        cap.release()
        os.system('sudo smplayer -fullscreen ~/Downloads/Berserk\ 2016\ -\ Hai\ Yo\ \[Oh\ Ashes\]\ \(REALLY\ FULL\ VERSION\)\ HD\ \(320\ \ kbps\).mp3')
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

if flag==False:
    cap.release()
    cv2.destroyAllWindows()