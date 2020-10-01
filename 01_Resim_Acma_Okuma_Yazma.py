# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""

import cv2

#img2 = cv2.imread("750x750_siyah.jpg")
img = cv2.imread("750x750.jpg",0)
""" resmi img degiskenine atadik. '0' parametresi direkt olarak siyah-beyaza gecis yapar
    print(type(img)) #->numpy.ndarray """

cv2.imwrite("......./Desktop/750x750_siyah.jpg", img)
#img degiskeni siyah-beyaz olarak masaustune kaydedildi

cv2.imshow("Deneme Resmi", img) #resim ekranda gosterildi

#cv2.imshow("Deneme Resmi", img) #resim ekranda gosterildi

cv2.waitKey(0)
cv2.destroyAllWindows()
