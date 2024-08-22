import cv2
import pytesseract
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time 

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

img = cv2.imread('images/test_1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

###########################################
########## Detecting Characters ###########
###########################################
imgHeight, imgWidth, _ = img.shape
config = r'--oem 3 --psm 6 outputbase digits'

boxes = pytesseract.image_to_boxes(img)
print(boxes)

for box in boxes.splitlines():
    box = box.split(' ')
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    text = box[0]
    cv2.rectangle(img, (x, imgHeight - y), (w, imgHeight - h), (0, 0, 255), 3)
    cv2.putText(img, text, (x, imgHeight - y + 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50, 50, 255), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)