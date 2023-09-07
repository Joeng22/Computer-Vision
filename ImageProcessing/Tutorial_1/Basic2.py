#Image Read / Display
#Matplot lib

import cv2
import matplotlib.pyplot as plt

ImgPath_1 = "car1.jpg"
img = cv2.imread(ImgPath_1,cv2.IMREAD_COLOR)

plt.imshow(img)
plt.waitforbuttonpress()
plt.close('all')
