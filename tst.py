import cv2
import numpy as np

img = cv2.imread("written.jpg")
img2 = img[120:250,300:500]
img[0:130,0:200] = img2
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
