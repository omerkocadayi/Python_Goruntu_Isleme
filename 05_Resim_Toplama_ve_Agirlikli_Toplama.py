""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

"""resimlerin saglikli olarak toplanabilmesi icin boyutlarinin denk olmasi gerekmektedir."""

import cv2

img = cv2.imread("05_600x400.jpg")
img2 = cv2.imread("05_600x400_2.jpg")

print("[175,250] pikselleri icin\n\n"
      "img\t: ",img[175,250],"\nimg2\t: ",img2[175,250],
      "\n\nduz toplama (mod)\t= ",img[250,250]+img2[250,250])

""" kodu benim kullanmis oldugum gorseller ile calistirirsaniz;
    print ciktilari incelendiginde doygunluk kaybimiz oldugunu goreceksiniz.
    blue ve green kanallari toplaminda iki renk de max noktasi olan 255 degerini
    geciyor. yani en doygun noktayi.. fakat buraya 255 degerini degil, toplamin
    255e modunu yaziyor. bu doygunluk kaybini yasamamak icin cv2.add
    metodunu kullanacagiz. toplam degeri 255in uzerine cikan bolumlerde
    tam doygun noktayi, yani 255'i yazacagiz.
    
    print ciktilarini dogru inceleyebilmeniz icin 05_600x400 ve 05_600x400_2
    isimli gorselleri indirerek calismalariniza devam etmenizi oneririm."""
  
toplam = cv2.add(img,img2)    
print("cv2.add sonucu\t\t: ",toplam[175,255])

agirlikli_toplam = cv2.addWeighted(img,0.225,img2,0.775,0)
print("cv2.Addweihgt sonucu\t: ",agirlikli_toplam[175,250])
#addWeighted metoduna girilen agirlik parametreleri toplami 1 olmak zorundadir.

cv2.imshow("600x400 - IMG 1",img)
cv2.imshow("600x400_2 - IMG 2",img2)
cv2.imshow("TOPLAM",toplam)
cv2.imshow("AGIRLIKLI TOPLAM",agirlikli_toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()
