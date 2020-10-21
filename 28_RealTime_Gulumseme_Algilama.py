""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade\\haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("haarcascade\\haarcascade_smile.xml")


while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (1280,960))
    frame = cv2.flip(frame, 1)    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 
                                 scaleFactor=1.3, 
                                 minNeighbors=5, 
                                 minSize=(100, 100),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

    for (a,b,c,d) in faces:
        cv2.rectangle(frame, (a,b), (a+c, b+d), (0,255,255), 3)
        
        roi = frame[b:b+d, a:a+c]
        gray1 = gray[b:b+d, a:a+d]
        smiles = smileCascade.detectMultiScale(gray1, 
                                 scaleFactor=1.3, 
                                 minNeighbors=5, 
                                 minSize=(70, 70),
                                 flags=cv2.CASCADE_SCALE_IMAGE)
    
        for (a,b,c,d) in smiles:
            cv2.rectangle(roi, (a,b), (a+c, b+d), (180,0,180), 3)
    
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()