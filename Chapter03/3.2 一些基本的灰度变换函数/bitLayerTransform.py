"""
Created by HenryMa on 2020/8/24
"""

__author__ = 'HenryMa'


import math
from builtins import range, print
import numpy as np
import cv2


def bitLayerTransform(image, layerNum):

    if layerNum == 1:
        new_img = np.where((image >= 0) & (image < 2), 255, 0)
    elif layerNum == 2:
        new_img = np.where((image >= 2) & (image < 4), 255, 0)
    elif layerNum == 3:
        new_img = np.where((image >= 4) & (image < 8), 255, 0)
    elif layerNum == 4:
        new_img = np.where((image >= 8) & (image < 16), 255, 0)
    elif layerNum == 5:
        new_img = np.where((image >= 16) & (image < 32), 255, 0)
    elif layerNum == 6:
        new_img = np.where((image >= 32) & (image < 64), 255, 0)
    elif layerNum == 7:
        new_img = np.where((image >= 64) & (image < 128), 255, 0)
    elif layerNum == 8:
        new_img = np.where((image >= 128) & (image < 256), 255, 0)
    else:
        new_img = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
        print('Please enter the number of bit layers from 1 to 8')

    return new_img.astype(np.uint8)


if __name__ == '__main__':
    img = cv2.imread('../pic/Fig0314(a)(100-dollars).tif', 0)
    bit_img1 = bitLayerTransform(img, 1)
    bit_img2 = bitLayerTransform(img, 2)
    bit_img3 = bitLayerTransform(img, 3)
    bit_img4 = bitLayerTransform(img, 4)
    bit_img5 = bitLayerTransform(img, 5)
    bit_img6 = bitLayerTransform(img, 6)
    bit_img7 = bitLayerTransform(img, 7)
    bit_img8 = bitLayerTransform(img, 8)
    cv2.imshow('source img', img)
    # print(bit_img)
    cv2.imshow('slice img1', bit_img1)
    cv2.imshow('slice img2', bit_img2)
    cv2.imshow('slice img3', bit_img3)
    cv2.imshow('slice img4', bit_img4)
    cv2.imshow('slice img5', bit_img5)
    cv2.imshow('slice img6', bit_img6)
    cv2.imshow('slice img7', bit_img7)
    cv2.imshow('slice img8', bit_img8)
    cv2.waitKey(0)
