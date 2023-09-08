#Opencv Image Read / Display
#Opencv cv mat read 

import cv2

ImgPath_1 = "car1.jpg"
img = cv2.imread(ImgPath_1,cv2.IMREAD_COLOR)


print(type(img))
cv2.imshow("Frame", img)   #1. Window name , 2 Opencv numpy array
cv2.waitKey(0)
cv2.destroyAllWindows()


