""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

img_0 = cv2.imread("06_batman.jpg")
#img_1 = cv2.imread("median_noise.png")
#img_2 = cv2.imread("bilateral_noise.jpg")

img_0_0 = cv2.blur(img_0, (5,5))
img_0_1 = cv2.GaussianBlur(img_0, (5,5), cv2.BORDER_DEFAULT)

cv2.imshow("Original - No Blur", img_0)
cv2.imshow("Blur", img_0_0)
cv2.imshow("Gaussian Blur", img_0_1)


#img_1_0 = cv2.medianBlur(img_1, 7)
#cv2.imshow("Original - With Median Noise", img_1)
#cv2.imshow("Smooting Median", img_1_0)


#img_2_0 = cv2.bilateralFilter(img_2, 10, 90, 90)
#cv2.imshow("Original - With Bilateral Noise", img_2)
#cv2.imshow("Smooting Bilateral", img_2_0)

cv2.waitKey(0)
cv2.destroyAllWindows()