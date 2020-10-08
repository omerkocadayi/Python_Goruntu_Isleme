""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

img = cv2.imread("threshold.jpg", 0)

ret, th1 = cv2.threshold(img, 160, 250, cv2.THRESH_BINARY) # renk değeri 160'tan büyük ise 250'ye eşitle, gerisi 0
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 21, 5)

cv2.imshow("Original Image", img)
cv2.imshow("With Threshold", th1)
cv2.imshow("With Mean Threshold - Adaptive", th2)
cv2.imshow("With Gaussian Threshold - Adaptive", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()