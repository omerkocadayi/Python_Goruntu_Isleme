# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""

#cv2.imshow pencere ciktilarini ayri ayri inceleyiniz.

import cv2
def pencere_kapat():
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
img = cv2.imread("750x750.jpg")

blue, green, red = cv2.split(img) #split metodu resmi bgr 3 renk kanalina ayirmaktadir.
                                  #tek kanalda islem yapmamız gerektiginde bu metodu uygulayabiliriz.

#kanallari ayrilmis resmi nasil tek parcaya toplariz ?
yeni_img = cv2.merge((blue,green,red)) #cv2.merge metodu ile kanallari siralayarak  islemi gerceklestirebiliriz.

cv2.imshow("Orijinal Resim",img)
pencere_kapat()
cv2.imshow("Resim BLue Kanali",blue)
pencere_kapat()
cv2.imshow("Resim Green Kanali",green)
pencere_kapat()
cv2.imshow("Resim Red Kanali",red) 
pencere_kapat()
cv2.imshow("Ayri Kanallari Birlestirme (Merge)",yeni_img) 
pencere_kapat()


#_____________________________________________________________________________

yeni_img[240:450,320:650,0] = 255 # virgulden sonraki 0 parametresi blue, 1 parametresi green, 2 parametresi red'i temsil eder
""" y1=240, y2=320
    x1=450, x2=650 araligindaki bolgenin mavi kanalini maksimum degere yukselttik """
cv2.imshow("Blue Kanala 255 Atama",yeni_img) 
pencere_kapat()


#_____________________________________________________________________________

for i in range(100):
    img[i,i] = [255,255,255]
    """cv2 kutuphanesi resimleri np.ndarray formatinda almaktadir.
    diziler uzerinde yaptigimiz islemleri resimler uzerinde de gerceklestirebilmekteyiz.
    bu dongu ile resmin 0;0 pikselinden itibaren capraz olarak 100 piksellik
    beyaz bir cizgi cekmis olacagiz."""
cv2.imshow("Cizgi Deneme",img)
pencere_kapat()


#_____________________________________________________________________________

kesit = img[150:250,300:500]
""" resmin y1 = 150, y2 = 300 ; x1 = 250, x2 = 500 araligindaki bolgesini
    kesit degiskenine atamis olduk. resmin sadece belli bolgesinde islem yapmak
    istiyorsak bu benzeri yontemleri kullancagiz."""

cv2.imshow("Kesit Deneme",kesit)
pencere_kapat()


#_____________________________________________________________________________

for i in range(200):
    img[100,i] = [255,255,255]
    if i < 100:
        img[i,200] = [255,255,255]
    
img[0:100,0:200] = kesit
""" resmin y1 = 0, y2 = 0; x1 = 100, x2 = 200 araligindaki bolgesine
    kesit degiskeninde tutulan bolgeyi kopyala-yapistir yapmis olduk
    ve 2. for dongusuyle bu kesitin etrafina beyaz cizgi cektik"""

cv2.imshow("Kesit Yapistirma + Cerceve Deneme",img)
pencere_kapat()
