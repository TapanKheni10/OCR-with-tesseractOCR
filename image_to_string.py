import cv2
import pytesseract
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time 

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

img = cv2.imread('images/test_3.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

###########################################
########### Detecting Strings #############
###########################################
imgHeight, imgWidth = imgGray.shape

strings = pytesseract.image_to_string(imgGray)
print(strings)

cv2.imshow('Result', img)
cv2.waitKey(0)