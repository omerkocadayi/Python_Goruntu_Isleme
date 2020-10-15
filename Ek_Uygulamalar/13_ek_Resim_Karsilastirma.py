""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

path1 = "batman.jpg"

img1 = cv2.imread(path1)
img2 = cv2.imread(path1)
img3 = cv2.medianBlur(img1,3)

if img1.shape == img2.shape:
    print("Img1 and Img2 are the same size")
else:
    print("Img1 and Img2 are not the same size")

diff = cv2.subtract(img1,img3)
b,g,r = cv2.split(diff)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 :
    print("completely equal")
else:
    print("NOT completely equal")

cv2.imshow("Difference",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()