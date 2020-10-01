# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""

""" resim uzatma
    resim aynalama
    resmi tekrar etme
    resmin etrafini sarma
    alan secme
    islemleri gerceklestirilecektir.
"""

import cv2
def pencere_kapat():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("750x750.jpg")

img_uzatma = cv2.copyMakeBorder(img,100,100,100,100, cv2.BORDER_REPLICATE) 

img_aynalama = cv2.copyMakeBorder(img,250,250,250,250, cv2.BORDER_REFLECT)

img_tekrar = cv2.copyMakeBorder(img,150,150,150,150, cv2.BORDER_WRAP)

img_sarma = cv2.copyMakeBorder(img,25,25,25,25, cv2.BORDER_CONSTANT, value = [0,150,0])


#alan secme
cv2.rectangle(img, (50,120), (140,60), [0,0,200], 2)
#cv2.rectangle(img, 1.nokta, 2.nokta, renk, kalınlık, cizgi tipi)

cv2.imshow("Orijinal",img)
pencere_kapat()
cv2.imshow("Uzatma",img_uzatma)
pencere_kapat()
cv2.imshow("Aynalama",img_aynalama)
pencere_kapat()
cv2.imshow("Tekrar",img_tekrar)
pencere_kapat()
cv2.imshow("Sarma",img_sarma)
pencere_kapat()
