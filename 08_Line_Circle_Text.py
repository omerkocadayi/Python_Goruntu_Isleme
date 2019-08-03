"""@author: omerkocadayi"""

import cv2
import numpy as np

def main():
    img = np.zeros((500,500,3), dtype = "uint8")
    img.fill(255) #tum matrisi tek bir degerle doldurur. 0-255 arasi
    
    cv2.line(img, (50,100),(250,250),(150,120,255), 3)
    #baslangic : 50:100, bitis : 250:250 araliginda bir cizgi cektik
    
    cv2.circle(img, (400,100), 50, (30,200,30), 2)
    #merkez : 400:100 , yaricap : 50 degerlerinde cember cizimi
    
    cv2.putText(img, "OmerKocadayi_GoruntuIsleme", (75,400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,50,50), 1)
    #baslangic : 75:400, yazi_tipi:HERSHEY_COMPLEX_SMALL, boyut:1, renk (255,50,50), kalinlik 1
    
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()