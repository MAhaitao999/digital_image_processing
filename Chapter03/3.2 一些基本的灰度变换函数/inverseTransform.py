"""
Created by HenryMa on 2020/8/24
"""

__author__ = 'HenryMa'


import cv2
import numpy as np

img = cv2.imread('../pic/Fig0304(a)(breast_digital_Xray).tif', 0)

reverse_img = 255 - img

cv2.imshow('srcimg', img)
cv2.imshow('reverse_img', reverse_img)
cv2.waitKey(0)
