# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:58:17 2022

@author: Maciek
"""
import pytesseract
import cv2
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


img = cv2.imread('test.jpg')
# print(type(img))
# print(img.shape)

# img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow('image', img_convert)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def convertImageToText(img):
    img = cv2.imread(img)
    print(pytesseract.image_to_string(img))



convertImageToText(img)



