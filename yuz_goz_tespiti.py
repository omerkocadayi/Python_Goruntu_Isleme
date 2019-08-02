# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""

import cv2

""" opencv kurulumuyla beraber gelen xml
    dosyalarını program içine entegre ediyoruz """
    
yuz_csd = cv2.CascadeClassifier('C:\\Users\\omerkocadayi\\Desktop\\opencv\\sources\\samples\\winrt\\FaceDetection\\FaceDetection\\Assets\\haarcascades_frontalface_default.xml')
goz_csd = cv2.CascadeClassifier('C:\\Users\\omerkocadayi\\Desktop\\opencv\\sources\\data\\haarcascades_cuda\\haarcascades_eye.xml')

cam = cv2.VideoCapture(0)

""" (0) -> pc kamerasını kullanır
    (1) -> usb kamera kullanır
    ("dosyauzantisi.mp4") -> hazır bir video kullanır. """

while True:
    ret, frame = cam.read()
    if ret is True:
        gri_ton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #görüntüyü siyah-beyaz alıyoruz
    else:
        continue
    
    yuzler = yuz_csd.detectMultiScale(gri_ton, 1.3, 5)#yüz tespit et
    
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)#yüzü kare içine al
        roi_gri_ton = gri_ton[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        gozler = goz_csd.detectMultiScale(roi_gri_ton)#göz tespit et
        
        for(gx,gy,gw,gh) in gozler:
            cv2.rectangle(roi_color, (gx+gy), (gx+gw,gy+gh), (0,255,0), 2)
    
    cv2.imshow('gray', gri_ton)
    if cv2.waitKey(1) & 0xFF == ord('q'): #q tuşu ile programdan çıkış yapıyoruz
        break
    
cam.release()
cv2.destroyAllWindows()