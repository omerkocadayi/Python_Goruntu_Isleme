""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """
"""
Spyder IDE kullananlar için plt.show() çalışmayabilir.
Tools->Preferences->IPython Console->Graphics->Graphics Backend-> Backend = 'Automatic' olarak seçin
Bu şekilde düzelecektir. Aksi takdirde plt.show() yerine plt.draw() metodunu deneyiniz.
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("test.jpg")
b,g,r = cv2.split(img)

plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
#plt.hist(img.ravel(), 256, [0,256])

cv2.imshow("Image", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()