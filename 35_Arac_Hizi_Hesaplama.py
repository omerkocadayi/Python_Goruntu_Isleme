""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import time

vid = cv2.VideoCapture("cars.mp4")
carCascade = cv2.CascadeClassifier("haarcascade/car1.xml")

crd = [[620,220],[740,220],[580,500],[815,500]]
distance, t1, t2, speed, p_frame, n_frame, cnt = 0.025, 0, 0, "", 0, 0, 0

while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = carCascade.detectMultiScale(gray, 
                                 scaleFactor=1.1, 
                                 minNeighbors=3, 
                                 minSize=(100, 100),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

    cv2.line(frame, (crd[0][0],crd[0][1]),(crd[1][0],crd[1][1]),(0,0,255), 2)
    cv2.line(frame, (crd[0][0],crd[0][1]),(crd[2][0],crd[2][1]),(0,0,255), 2)
    cv2.line(frame, (crd[2][0],crd[2][1]),(crd[3][0],crd[3][1]),(0,0,255), 2)
    cv2.line(frame, (crd[1][0],crd[1][1]),(crd[3][0],crd[3][1]),(0,0,255), 2)
        
    for (a,b,c,d) in cars:
        cx, cy = int(a+c/2), int(b+d/2)
        
        if(cx >= crd[2][0] and cx <= crd[3][0] and cy >= (crd[2][1]-10) and cy <= (crd[3][1]+5)):
            cv2.circle(frame,(cx,cy),4,(0,255,255),-1)
            cv2.line(frame, (crd[2][0],crd[2][1]),(crd[3][0],crd[3][1]),(0,255,0), 2) 
            t1 = time.time()
    
        if(cx >= crd[0][0] and cx <= crd[1][0] and cy >= (crd[0][1]-10) and cy <= (crd[1][1]+5)):
            cv2.circle(frame,(cx,cy),4,(0,255,255),-1)
            cv2.line(frame, (crd[0][0],crd[0][1]),(crd[1][0],crd[1][1]),(0,255,0), 2)
            t2 = time.time()
            fps = cnt/(t2-t1)
            if t2-t1 > 0:
                sp = distance/((t2-t1)/3600)
                if  sp * (30/fps) < 250:
                    if sp * (30/fps) > 50 :
                        speed = str(sp* (30/fps))
                    else:
                        speed = str(sp)
                cnt = 0
                break;
    
    if speed != "" : cv2.putText(frame,""+str(speed[:5])+"km/h",(crd[0][0]-20,crd[0][1]-20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),1,cv2.LINE_AA)
                
    cv2.imshow("Frame", frame)
    cnt+=1
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()