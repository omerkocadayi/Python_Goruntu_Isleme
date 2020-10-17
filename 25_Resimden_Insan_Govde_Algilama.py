""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

img = cv2.imread("body.jpg")
img = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
bodyCascade = cv2.CascadeClassifier("haarcascade\\haarcascade_upperbody.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies = bodyCascade.detectMultiScale(gray,
                                      scaleFactor = 1.02,
                                      minNeighbors = 5,
                                      minSize = (30, 50),
                                      flags = cv2.CASCADE_SCALE_IMAGE)

for (a,b,c,d) in bodies:
    cv2.rectangle(img, (a,b), (a+c, b+d), (0,255,255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()