#Opencv Image Read / Display
#Opencv cv mat read / write

import cv2

ImgPath_1 = "car1.jpg"
img = cv2.imread(ImgPath_1,cv2.IMREAD_COLOR)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


