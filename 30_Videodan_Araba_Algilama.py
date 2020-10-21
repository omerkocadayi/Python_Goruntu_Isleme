""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

vid = cv2.VideoCapture("car1.mp4")
carCascade = cv2.CascadeClassifier("haarcascade\\car.xml")

while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = carCascade.detectMultiScale(gray, 
                                 scaleFactor=1.05, 
                                 minNeighbors=2, 
                                 minSize=(50, 50),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

    for (a,b,c,d) in cars:
        cv2.rectangle(frame, (a,b), (a+c, b+d), (0,255,255), 2)
        
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()