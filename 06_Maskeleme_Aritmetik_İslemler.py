# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""
""" Kodu; paylasmis oldugum 06_zongi.jpg ve 06_batman.jpg ile birlikte calistirin.
    Maskeleme isleminin anlasilmasi acisindan sizin adiniza iyi olacaktir.
    pencere ciktilarini adim adim incelemek istiyorsaniz yorum satırlarını aktif
    hale getirebilirsiniz."""
import cv2

def pencere_kapat():
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def main():
    img = cv2.imread("06_zongi.jpg")
    img2 = cv2.imread("06_batman.jpg")
    bat_gri = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Zongi",img)
    cv2.imshow("Batman",img2)
    #cv2.imshow("Batman_Gri",bat_gri)
    pencere_kapat()
    
    img_h, img_w, img_ch = img2.shape #yukseklik-h , genislik-w, renk kanali-ch
    roi = img[0:img_h , 0:img_w]
    
    ret, mask = cv2.threshold(bat_gri, 20, 255, cv2.THRESH_BINARY)
    #mask degiskenine ndarray formatinda maskelenmis resim atanir.
    ters_mask = cv2.bitwise_not(mask)
    
    sonuc = cv2.add(cv2.bitwise_and(roi,roi, mask = ters_mask), img2)
    img[0:img_h, 0:img_w] = sonuc
    
    #cv2.imshow("Maske",mask)
    #cv2.imshow("Ters Maske",ters_mask)
    cv2.imshow("Zongi-Batman-Final",img)
    pencere_kapat()
    
if __name__ == "__main__":
    main()
