import cv2
import pytesseract
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time 

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

img = cv2.imread('images/test_2.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

###########################################
########## Detecting Characters ###########
###########################################
imgHeight, imgWidth, _ = img.shape

boxes = pytesseract.image_to_data(img)
print(boxes)

for x, box in enumerate(boxes.splitlines()):
    box = box.split()
    if x != 0 and len(box) == 12:
        x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
        word = box[11]
        cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
        cv2.putText(img, word, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)