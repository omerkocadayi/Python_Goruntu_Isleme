""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

vid = cv2.VideoCapture("gozler.mp4")

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (960,540))
    if ret is False:
        break
    
    roi = frame[190:250,350:470]
    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY_INV)
    
    contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x : cv2.contourArea(x), reverse = True)   
    
    rows, cols, _ = roi.shape
    
    for cnt in contours:
        (a,b,c,d) = cv2.boundingRect(cnt)
        cv2.rectangle(roi, (a,b), (a+c, b+d), (0,255,0), 3)
        cv2.line(roi, (a+int(c/2),0), (a+int(c/2), rows), (180,0,180), 2)
        cv2.line(roi, (0,b+int(d/2)), (cols,b+int(d/2)), (180,0,180), 2)
        
        break
    frame[190:250,350:470] = roi
    
    cv2.imshow("Eye Tracking", frame)
    #cv2.imshow("Roi", roi)
    #cv2.imshow("Threshold", threshold)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()