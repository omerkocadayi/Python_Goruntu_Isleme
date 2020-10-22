""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

cap = cv2.VideoCapture("cars.mp4")
cap2 = cv2.VideoCapture("cars.mp4")

ret, firstFrame = cap.read()
firstFrame = cv2.resize(firstFrame, (640,480))
firstGray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
firstGray = cv2.GaussianBlur(firstGray, (3,3), 0)

subtractor = cv2.createBackgroundSubtractorMOG2(history = 100, varThreshold = 75, detectShadows = True)


while True:
    ret, frame = cap.read()
    ret, frame1 = cap2.read()
    
    frame = cv2.resize(frame, (640,480))
    frame1 = cv2.resize(frame1, (640,480))
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3,3), 0)

    diff = cv2.absdiff(firstGray, gray)
    ret, diff = cv2.threshold(diff, 40, 355, cv2.THRESH_BINARY)
    
    mask = subtractor.apply(frame)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Opencv Function Result", mask)
    cv2.imshow("Manuel Result", diff)        
    
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
