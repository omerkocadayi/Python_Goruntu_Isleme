""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

img1 = cv2.imread("bitwise1.png")
img2 = cv2.imread("bitwise2.png")

cv2.imshow("Original Image 1", img1)
cv2.imshow("Original Image 2", img2)

bit_and = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
bit_not = cv2.bitwise_not(img1,img2)
bit_xor = cv2.bitwise_xor(img1,img2)

#cv2.imshow("Bitwise AND", bit_and)     # 1&1=1 , gerisi 0
#cv2.imshow("Bitwise OR", bit_or)       # 0|0=0 , gerisi 1
#cv2.imshow("Bitwise NOT", bit_not)     # 0~0=1 , 0~1=1 , gerisi 0
#cv2.imshow("Bitwise XOR", bit_xor)     # 0^0=0 , 1^1=0, gerisi 1

cv2.waitKey(0)
cv2.destroyAllWindows()