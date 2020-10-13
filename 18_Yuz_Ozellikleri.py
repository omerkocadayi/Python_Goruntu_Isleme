""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np
import math

def findMaxContour(contours):
    max_i = 0
    max_area =0
    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])
        
        if max_area<area_face:
            max_area=area_face
            max_i = i
        try:
            c = contours[max_i]            
        except:
            contours = [0]
            c = contours[0]
        return c  

cap  =cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    
    roi = frame[80:320, 230:420] #y1:y2 , x1:x2
    cv2.rectangle(frame, (230,80), (420,320), (180,0,180), 2)

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lowerColor = np.array([0,40,80], dtype = np.uint8)
    upperColor = np.array([20,150,255], dtype = np.uint8)
    
    kernel = np.ones((4,4), np.uint8)
    mask = cv2.inRange(hsv, lowerColor, upperColor)
    mask = cv2.dilate(mask, kernel, iterations=2) 
    mask = cv2.medianBlur(mask, 15)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
      
        c = findMaxContour(contours)
            
        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        extBot = tuple(c[c[:, :, 1].argmax()][0])

        cv2.circle(roi,extLeft,5,(0,255,0),2)
        cv2.circle(roi,extRight,5,(0,255,0),2)
        cv2.circle(roi,extTop,5,(0,255,0),2)
        cv2.circle(roi,extBot,5,(0,255,0),2)

        cv2.line(roi,extLeft,extTop,(255,0,0),2)
        cv2.line(roi,extTop,extRight,(255,0,0),2)
        cv2.line(roi,extRight,extBot,(255,0,0),2)
        cv2.line(roi,extBot,extLeft,(255,0,0),2)

        a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1])**2)
        b = math.sqrt((extBot[0]-extRight[0])**2+(extBot[1]-extRight[1])**2)
        c = math.sqrt((extBot[0]-extTop[0])**2+(extBot[1]-extTop[1])**2)

        try:
            angle_ab= int(math.acos((a**2+b**2-c**2)/(2*b*c))*57)
            cv2.putText(roi,str(angle_ab),(extRight[0]-100+50,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
        except:
            cv2.putText(roi," ? ",(extRight[0]-100+50,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
   
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
