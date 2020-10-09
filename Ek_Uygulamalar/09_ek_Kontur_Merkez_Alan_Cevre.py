""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

##Kontur Uygulaması
img = cv2.imread("contour1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image for Contour App", img)

_, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, _=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(180,0,180),3)

############################################################################
##Geometri Merkezi Bulma Uygulamasi
img2 = cv2.imread("ucgen.png")
cv2.imshow("Original Triangle for Center and Area", img2)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, thresh2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY)
M = cv2.moments(thresh2)

X = int(M["m10"]/ M["m00"])
Y = int(M["m01"]/ M["m00"])

cv2.circle(img2, (X,Y), 5, (200,0,200), -1)


############################################################################
##Kontur - Alan, Çevre Uygulaması

img3 = cv2.imread("ucgen.png")
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
_, thresh3 = cv2.threshold(gray3,127,255,cv2.THRESH_BINARY)

contours3, _=cv2.findContours(thresh3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours3[0]
area = cv2.contourArea(cnt)
length = cv2.arcLength(cnt, True)
print("Area = ",area,"\nLength = ",length)


cv2.imshow("Contour",img)
cv2.imshow("Triangle Center", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()