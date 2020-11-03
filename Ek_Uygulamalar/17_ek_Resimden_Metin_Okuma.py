""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

from PIL import Image
import pytesseract

img = Image.open("kose_algila.jpg")
text = pytesseract.image_to_string(img, lang = "tur")
print(text)
