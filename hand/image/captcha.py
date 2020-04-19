#!/usr/bin/env python3

from PIL import Image
import pytesseract

def getstr(imagepath):
    imageObject=Image.open(imagepath)
    return pytesseract.image_to_string(imageObject)
