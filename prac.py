import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    cv2.imshow("new",img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()