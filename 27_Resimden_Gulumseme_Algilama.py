""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

img = cv2.imread("smile.jpeg")
img = cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
faceCascade = cv2.CascadeClassifier("haarcascade\\haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("haarcascade\\haarcascade_smile.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, 
                                 scaleFactor=1.3, 
                                 minNeighbors=5, 
                                 minSize=(200, 200),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

for (a,b,c,d) in faces:
    cv2.rectangle(img, (a,b), (a+c, b+d), (0,255,255), 3)
    
roi = img[b:b+d, a:a+c]
gray1 = gray[b:b+d, a:a+d]

smiles = smileCascade.detectMultiScale(gray1, 
                                 scaleFactor=1.3, 
                                 minNeighbors=5, 
                                 minSize=(80, 80),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

for (a,b,c,d) in smiles:
    cv2.rectangle(roi, (a,b), (a+c, b+d), (180,0,180), 3)
    
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
