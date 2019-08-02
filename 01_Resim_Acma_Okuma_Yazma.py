# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""

import cv2

#img2 = cv2.imread("C:/Users/omerkocadayi/Desktop/deneme_siyah_beyaz.jpg")
img = cv2.imread("C:/Users/omerkocadayi/Desktop/deneme.jpg",0)
""" resmi img degiskenine atadik. '0' parametresi direkt olarak siyah-beyaza gecis yapar
    print(type(img)) #->numpy.ndarray """

cv2.imwrite("C:/Users/omerkocadayi/Desktop/deneme_siyah_beyaz.jpg", img)
#img degiskeni siyah-beyaz olarak masaustune kaydedildi

cv2.imshow("Deneme Resmi", img) #resim ekranda gosterildi

#cv2.imshow("Deneme Resmi", img) #resim ekranda gosterildi

cv2.waitKey(0)
cv2.destroyAllWindows()