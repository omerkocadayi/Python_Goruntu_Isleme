# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:51:53 2020

@author: omerkocadayi
"""

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 1)
    
    if ret == False:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    cv2.imshow("Test RGB to GRAY", frame)

cv2.destroyAllWindows()