""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

img = cv2.imread("face.jpg")
img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
faceCascade = cv2.CascadeClassifier("haarcascade\\haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade\\haarcascade_eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, 
                                 scaleFactor=1.3, 
                                 minNeighbors=4, 
                                 minSize=(50, 50),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

for (a,b,c,d) in faces:
    cv2.rectangle(img, (a,b), (a+c, b+d), (0,255,255), 3)
    
roi = img[b:b+d, a:a+c]
gray1 = gray[b:b+d, a:a+d]

eyes = eyeCascade.detectMultiScale(gray1)

for (a,b,c,d) in eyes:
    cv2.rectangle(roi, (a,b), (a+c, b+d), (180,0,180), 3)
    
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
