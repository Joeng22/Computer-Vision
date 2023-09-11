import numpy as np
import cv2
img = cv2.imread('car1.jpg',1)
h, w = img.shape[:2]

cv2.circle(img, (50,50), 10, (0, 215, 255), 10)

center = (w / 2, h / 2)
mat = cv2.getRotationMatrix2D(center, 90, 1)
print("Rotation Matrix:",mat)

rotimg = cv2.warpAffine(img, mat, (h, w))
cv2.imshow('original',img)
cv2.imshow('rotated', rotimg)
cv2.waitKey(0)
cv2.destroyAllWindows()