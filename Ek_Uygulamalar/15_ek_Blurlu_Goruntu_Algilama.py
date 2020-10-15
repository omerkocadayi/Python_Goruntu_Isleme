""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

img = cv2.imread("batman.jpg")
blur = cv2.medianBlur(img, 3)

laplacian_img = cv2.Laplacian(img, cv2.CV_64F).var()
laplacian_blur = cv2.Laplacian(blur, cv2.CV_64F).var()

print("Original img laplacian value : "+str(laplacian_img)+"\nBlurry img laplacian value : "+str(laplacian_blur) )

if laplacian_blur <= 500:
    print("\nBlurry Image !")

cv2.imshow("Original", img)
cv2.imshow("Blurry", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()