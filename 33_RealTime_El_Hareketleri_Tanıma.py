""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

while True:
    try:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        roi = frame[75:350, 350:620]
        cv2.rectangle(frame, (350,75), (620,350), (255,0,255), 2)
        
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            
        lowerColor = np.array([0,40,80], dtype = np.uint8)
        upperColor = np.array([20,150,255], dtype = np.uint8)
        
        kernel = np.ones((4,4), np.uint8)
        mask = cv2.inRange(hsv, lowerColor, upperColor)
        mask = cv2.dilate(mask, kernel, iterations=3) 
        mask = cv2.GaussianBlur(mask, (5,5), 100)
        
        contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        cnt = max(contours, key=lambda x:cv2.contourArea(x))
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        
        hull = cv2.convexHull(cnt)
        area_hull = cv2.contourArea(hull)
        area_cnt = cv2.contourArea(cnt)    
        area_ratio = ((area_hull-area_cnt) / area_cnt) * 100
        
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)
        
        dc = 0
        
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            
            a = math.sqrt((end [0]-start[0]) **2 + (end[1]-start[1]) **2)
            b = math.sqrt((far [0]-start[0]) **2 + (far[1]-start[1]) **2)
            c = math.sqrt((end [0]-far[0]) **2 + (end[1]-far[1]) **2)
            
            s = (a+b+c) / 2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            d = (2*area) / a
            
            angle = math.acos((b**2+c**2-a**2) / (2*b*c))*57
            if angle <= 90 and d>30:
                dc += 1
                cv2.circle(roi, far, 3, [255,0,0], -1)
            
            cv2.line(roi,start, end, [0,255,0], 2)    
            
        dc += 1
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        if dc == 1:
            if area_cnt < 2000:
                cv2.putText(frame, "Put your hand in the box", (50,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
            else:
                if area_ratio < 12:
                    cv2.putText(frame, "0", (0,50), font, 2, (0,0,255), 2, cv2.LINE_AA)
                
                elif area_ratio < 17.5:
                    cv2.putText(frame, "Good Job", (0,50), font, 2, (0,0,255), 2, cv2.LINE_AA)
                
                else:
                    cv2.putText(frame, "1", (0,50), font, 2, (0,0,255), 2, cv2.LINE_AA)
                    
        elif dc==2:
            cv2.putText(frame,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif dc==3:
            if area_ratio<27:
                cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            else:
                cv2.putText(frame,'ok',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
        
        elif dc==4:
            cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif dc==5:
            cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif dc==6:
            cv2.putText(frame,'reposition',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        else :
            cv2.putText(frame,'reposition',(10,50), font, 2, (0,0,255), 3, cv2.LINE_AA)                    
                    
    except:
        pass   
            
    cv2.imshow("Frame", frame)
      
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()