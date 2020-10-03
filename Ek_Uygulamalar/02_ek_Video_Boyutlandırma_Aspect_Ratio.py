# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:21:47 2020

@author: omerkocadayi
"""
import cv2

def resizeAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):
      dimension = None
      (h,w) = img.shape[:2]
      
      if width is None and height is None:
            return img
      
      if width is None:
            r = height / float(h)
            dimension = (int(w*r), height)
      else:
            r = width / float(w)
            dimension = (width, int(h*r))
      
      return cv2.resize(img, dimension, interpolation = inter)



img = cv2.imread("deneme.jpg")
img1 = resizeAspectRatio(img, None, 450, cv2.INTER_AREA)

cv2.imshow("orjinal", img)
cv2.imshow("resized", img1)
#img = cv2.resize(img, (200,500)) #boyut ayarlama (en/boy oranı dikkate alınmalı)

cv2.waitKey(0)
cv2.destroyAllWindows()