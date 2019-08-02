# -*- coding: utf-8 -*-
"""@author: omerkocadayi"""
""" 
    RGB (Red,Green,Blue) olarak bildigimiz renk kanalları
    OpenCV mantiginda BGR (Blue,Green,Red) olarak calismaktadir.
    (0-255, 0-255, 0-255) arasi degerler alirlar, yani sadece
    sayidan ibaretler. Bilgisayar ise bu sayilari anlamlandirarak
    bize renk karsiliklarini sunmaktadir.
    
"""

import cv2

img = cv2.imread("C:/Users/omerkocadayi/Desktop/750x750.jpg")

print("img.type : ",type(img)) #numpy.ndarray -> n dimensional(boyutlu) array

print("img.dtype : ",img.dtype) #resmin data tipi -> uint8 -> 8 bitten olusuyor. bu yuzden max 255 degerini alabiliyor.

print("img.shape : ",img.shape) #(yukseklik,genislik,renk kanali sayisi) seklinde cikti verir.

print("img.size : ",img.size) #(yukseklik * genislik * renk kanali) -> resmin kac pikselden olustugunu yazdirir.

#print("img matrisi : ",img) #komutuyla; resmimizin BGR(0-255) karsiliklarini matris seklinde gormekteyiz.

"""
    deneme olarak programa aldiginiz resmin; yukaridaki print komutlariyla beraber
    ne kadar buyuk boyutlara sahip oldugunu goreceksiniz. ve tahmin edersiniz ki
    o boyutlarda calismak oldukca zorlu olacak. bu yuzden goruntu isleme uygulamalarina
    resimlerin boyutlarini dusurerek baslayacagiz. bunun icin en basit yontem : 
    resmi siyah-beyaz olarak almaktir. resmi bir kez daha (siyah-beyaz) okuyarak
    boyut degerlerinin karsilastirmasini yapacagiz. PRINT CIKTILARINI (size,shape,img matris)
    KONTROL EDINIZ.
"""

img2 = cv2.imread("C:/Users/omerkocadayi/Desktop/deneme.jpg",0)

print("img.type (siyah-beyaz) : ",type(img2))

print("img.dtype (siyah-beyaz) : ",img2.dtype)

print("img.shape (siyah-beyaz) : ",img2.shape)

print("img.size (siyah-beyaz) : ",img2.size)

print("50,50 pikseldeki renk degeri : ",img.item(50,50)) #rengin 0-255 arasindaki degerini verir

#print("img matrisi (siyah-beyaz) : ",img2)



cv2.waitKey(0)
cv2.destroyAllWindows()
