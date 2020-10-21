""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

img = cv2.imread("car.jpg")
img1 = cv2.imread("car1.jpeg")
carCascade = cv2.CascadeClassifier("haarcascade\\car.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = carCascade.detectMultiScale(gray, 
                                 scaleFactor=1.05, 
                                 minNeighbors=4, 
                                 minSize=(60, 60),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cars1 = carCascade.detectMultiScale(gray1, 
                                 scaleFactor=1.03, 
                                 minNeighbors=3, 
                                 minSize=(60, 60),
                                 flags=cv2.CASCADE_SCALE_IMAGE)
for (a,b,c,d) in cars:
    cv2.rectangle(img, (a,b), (a+c, b+d), (0,255,255), 2)
    
for (a,b,c,d) in cars1:
    cv2.rectangle(img1, (a,b), (a+c, b+d), (0,255,255), 2)

cv2.imshow("Image", img)
cv2.imshow("Image 1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()