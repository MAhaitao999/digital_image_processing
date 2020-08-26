"""
Created by HenryMa on 2020/8/26
"""

__author__ = 'HenryMa'


import cv2
import numpy as np


if __name__ == '__main__':

    img = cv2.imread('../pic/Fig0304(a)(breast_digital_Xray).tif')
    gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
    dst = cv2.convertScaleAbs(gray_lap)  # 转回uint8

    cv2.imshow('origin', img)
    cv2.imshow('laplacian', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
