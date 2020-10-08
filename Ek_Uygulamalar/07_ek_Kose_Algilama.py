""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

img = cv2.imread("kose_algila.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 75, 0.01, 10)
corners = np.int0(corners)

for crn in corners:
    x,y = crn.ravel()
    cv2.circle(img, (x,y), 3, (180,0,180), -1)
    
cv2.imshow("Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()