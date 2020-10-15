""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

img = cv2.imread("test.jpg")
temp = cv2.imread("test1.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_temp= cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray_img, gray_temp, cv2.TM_CCORR_NORMED)
location = np.where(result >= 0.99)

w,h = gray_temp.shape[::-1]

for point in zip(*location[::-1]):
    cv2.rectangle(img, point, (point[0]+ w,point[1]+h), (0,255,255), 2)

cv2.imshow("Original Img", img)
cv2.imshow("Template", temp)
cv2.waitKey(0)
cv2.destroyAllWindows()