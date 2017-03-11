import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frame = None

while True:
    _, frame = cap.read()
    cv2.imshow("img",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.imwrite("img4.jpg",frame)
cv2.destroyAllWindows()