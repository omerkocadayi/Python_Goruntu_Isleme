""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

def main():
    img = np.zeros((500,500,3), dtype = "uint8")
    img.fill(255) #tum matrisi tek bir degerle doldurur. 0-255 arasi
    
    cv2.line(img, (50,100),(250,250),(150,120,255), 3)
    #baslangic : 50:100, bitis : 250:250 araliginda bir cizgi cektik
    
    cv2.circle(img, (400,100), 50, (30,200,30), 2)
    #merkez : 400:100 , yaricap : 50 degerlerinde cember cizimi
    
    cv2.rectangle(img, (10,10), (50,50), (0,255,0), thickness=-1)
    cv2.rectangle(img, (400,350), (480,480), (0,255,0), thickness=-1)
    #dikdörtgen cizimleri
    
    pts = np.array([[[100, 200], [300, 250], [230, 420], [400,100]]], np.int32)
    cv2.polylines(img, [pts], True, (0,50,0), 2)
    #cokgen cizimleri
    
    cv2.putText(img, "OmerKocadayi_GoruntuIsleme", (75,400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,50,50), 1)
    #baslangic : 75:400, yazi_tipi:HERSHEY_COMPLEX_SMALL, boyut:1, renk (255,50,50), kalinlik 1
    
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
