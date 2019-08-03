# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""
""" goruntu alirken nesnelerin uzaklik-yakinliklarina gore
    o anki kapladigi alan, piksel degerleri degisebilmektedir.
    daha rahat islem yapabilmek adina resimleri buyutmek,kucultmek,
    piramit yapisi kullanmak bize fayda saglayacaktir."""

import cv2
import numpy as np

img = cv2.imread("C:/Users/omerkocadayi/Desktop/06_zongi.jpg")

buyuk_img = cv2.pyrUp(img)     #resmi 2 kat buyuttuk
kucuk_img = cv2.pyrDown(img)  #resmi 2 kat kuculttuk

print("Orijinal boyut\t: ",img.shape,
      "\nbuyutulmus\t: ",buyuk_img.shape,
      "\nkucultulmus\t: ",kucuk_img.shape)

resim = np.zeros((500,500,3), dtype="uint8")
#500x500 piksel ve 3 renk kanalina sahip siyah bir resim elde ettik
cv2.rectangle(resim, (150,350), (350,150), (150,50,50), 2)

cv2.imshow("np.zeros",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()