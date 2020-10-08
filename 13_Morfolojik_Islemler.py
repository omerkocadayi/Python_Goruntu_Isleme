""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

img = cv2.imread("morph.png",0)
img1 = cv2.imread("opening.png",0)
img2 = cv2.imread("closing.png",0)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
cv2.imshow("Original", img)
#cv2.imshow("Erosion", erosion)
#cv2.imshow("Dilation", dilation)

opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
#cv2.imshow("Original for Open", img1)
#cv2.imshow("Opening", opening)

closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
#cv2.imshow("Original for Close", img2)
#cv2.imshow("Closing", closing)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#cv2.imshow("Gradient", gradient)

top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#♠cv2.imshow("Top Hat", top_hat)

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#cv2.imshow("Black Hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()