# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:48:59 2020

@author: omerkocadayi
"""

import cv2
import numpy as np

def nothing(i):
    pass

img = np.zeros((480,480, 3), np.uint8)
cv2.namedWindow("trackbar_test")

cv2.createTrackbar("B", "trackbar_test", 0, 255, nothing)
cv2.createTrackbar("G", "trackbar_test", 0, 255, nothing)
cv2.createTrackbar("R", "trackbar_test", 0, 255, nothing)

while True:
    cv2.imshow("Test", img)
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break
    
    b = cv2.getTrackbarPos("B", "trackbar_test")
    g = cv2.getTrackbarPos("G", "trackbar_test")
    r = cv2.getTrackbarPos("R", "trackbar_test")
    
    img[:] = [b,g,r]
    
cv2.destroyAllWindows()