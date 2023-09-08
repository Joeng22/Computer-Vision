#Image Read /  / Write
#Matplot lib
#Display gray scale image
#cv2 used BGR color format , matplotlib used RGB color format

import cv2
import matplotlib.pyplot as plt

ImgPath_1 = "car1.jpg"
#Read Image as gray scale
img = cv2.imread(ImgPath_1,cv2.IMREAD_GRAYSCALE)

ImageSavePath = "saveCar1.jpg"
cv2.imwrite(ImageSavePath,img)