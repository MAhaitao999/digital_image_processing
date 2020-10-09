"""
Created by HenryMa on 2020/10/9
"""

__author__ = 'HenryMa'


from builtins import *

import cv2
import numpy as np


# Read image as color-scale
img = cv2.imread('./pic/eye.png', cv2.IMREAD_COLOR)
print(img)

# Convert to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce noise
img_blur = cv2.medianBlur(gray, 5)

# Apply hough transform on the image
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, img.shape[0]/64,
                           param1=200, param2=10, minRadius=5, maxRadius=30)

print(circles)

img_copy = img.copy()
# Draw detected circles
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw outer circle
        cv2.circle(img_copy, (i[0], i[1]), i[2], (0, 255, 0), 2)

        # Draw inner circle
        cv2.circle(img_copy, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('origin image', img)
cv2.imshow('gray image', gray)
cv2.imshow('blur image', img_blur)
cv2.imshow('result image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
