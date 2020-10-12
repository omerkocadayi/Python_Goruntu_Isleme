""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
import numpy as np

img = cv2.imread("klavye.jpg")
img2 = cv2.imread("h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)
edges2 = cv2.Canny(gray2, 75, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 150, maxLineGap = 75)
lines2 = cv2.HoughLinesP(edges2, 1, np.pi/180, 50, maxLineGap = 125)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (180,0,180), 1)

for line in lines2:
    x1, y1, x2, y2 = line[0]
    cv2.line(img2, (x1,y1), (x2,y2), (180,0,180), 2)


cv2.imshow("Original Image 1", img)
cv2.imshow("Edges of Image1", edges)

cv2.imshow("Original Image 2", img2)
cv2.imshow("Edges of Image2", edges2)

cv2.waitKey(0)
cv2.destroyAllWindows()