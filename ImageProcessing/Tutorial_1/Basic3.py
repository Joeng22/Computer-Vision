#Image Read / Display
#Matplot lib
#cv2 used BGR color format , matplotlib used RGB color format

import cv2
import matplotlib.pyplot as plt

ImgPath_1 = "car1.jpg"
img = cv2.imread(ImgPath_1,cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img)
plt.waitforbuttonpress()
plt.close('all')
