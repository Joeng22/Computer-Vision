# To find Bilateral Blur of an Image

import cv2
import os

ImgPath_1 = "car1.jpg"
SavePath_1 = "Bilateral_blur.jpg"
#Adding a safety, execute the below codes only if file exists

if os.path.exists(ImgPath_1):
    img = cv2.imread(ImgPath_1,cv2.IMREAD_COLOR)


    Bilateral = cv2.bilateralFilter(img, 9, 75, 75) #Opencv api for finding Bilateral filter blur of an image

    cv2.imshow('Bilateral Blur', Bilateral)

    cv2.imshow("Frame", img)   #1. Window name , 2 Opencv numpy array

    cv2.imwrite(SavePath_1,Bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("error.Image Not Found \n")