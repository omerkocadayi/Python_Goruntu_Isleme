""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np
import pytesseract
import imutils

img = cv2.imread("license_plate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp = cv2.bilateralFilter(gray, 7, 250, 250)
edged = cv2.Canny(temp, 50, 200)

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

screen = None

for cnt in cnts:
    epsilon = 0.018 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    if len(approx) == 4:
        screen = approx
        break

mask = np.zeros(gray.shape, np.uint8)
result = cv2.drawContours(mask, [screen], 0, (255,255,255), -1)
result = cv2.bitwise_and(img, img, mask=mask)
(x,y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(botx, boty) = (np.max(x), np.max(y))

cropped = gray[topx:botx+1, topy:boty+1]

print(pytesseract.image_to_string(cropped, lang="eng"))

cv2.imshow("Original", img)
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()