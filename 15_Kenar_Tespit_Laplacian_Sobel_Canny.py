""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

cap = cv2.VideoCapture(0)
img = cv2.imread("06_batman.jpg",0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    canny = cv2.Canny(frame, 80,180)
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Canny", canny)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Sobel X", sobelx)
    cv2.imshow("Sobel Y", sobely)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""
#Fotograf uzerinden yapilan ornekler

canny1 = cv2.Canny(img, 80,180)
laplacian1 = cv2.Laplacian(img,cv2.CV_64F)
sobelx1 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely1 = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow("Original", img)
cv2.imshow("Canny", canny1)
cv2.imshow("Laplacian", laplacian1)
cv2.imshow("Sobel X", sobelx1)
cv2.imshow("Sobel Y", sobely1)   
cv2.waitKey(0)
"""
  
cap.release()
cv2.destroyAllWindows()