"""
Created by HenryMa on 2020/9/13
https://www.cnblogs.com/wojianxin/p/12542004.html
"""

__author__ = 'HenryMa'

from builtins import *

import cv2
import numpy as np
import matplotlib.pyplot as plt


# Gray scale
def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.7222 * b
    out = out.astype(np.uint8)

    return out


# Otsu Binarization
def otsu_binarization(img, th=128):
    H, W = img.shape
    out = img.copy()

    max_sigma = 0
    max_t = 0

    # determine threshold
    for _t in range(1, 255):
        v0 = out[np.where(out < _t)]
        m0 = np.mean(v0) if len(v0) > 0 else 0.
        w0 = len(v0) / (H * W)
        v1 = out[np.where(out >= _t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0.
        w1 = len(v1) / (H * W)
        sigma = w0 * w1 * ((m0 - m1) ** 2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t

    # Binarization
    print("threshold >>", max_t)
    th = max_t
    out[out < th] = 0
    out[out >= th] = 255

    return out


# Morphology Dilate
def Morphology_Dilate(img, Dil_time=1):
    H, W = img.shape

    # Kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(Dil_time):
        tmp = np.pad(out, (1, 1), 'edge')
        for y in range(1, H+1):
            for x in range(1, W+1):
                if np.sum(MF * tmp[y-1: y+2, x-1: x+2]) >= 255:
                    out[y-1, x-1] = 255

    return out


# Morphology Erode
def Morphology_Erode(img, Erode_time=1):

    H, W = img.shape
    out = img.copy()

    # kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each erode
    for i in range(Erode_time):
        tmp = np.pad(out, (1, 1), 'edge')
        # erode
        for y in range(1, H+1):
            for x in range(1, W+1):
                if np.sum(MF * tmp[y-1: y+2, x-1: x+2]) < 255 * 4:
                    out[y-1, x-1] = 0

    return out


if __name__ == '__main__':
    # Read image
    origin_img = cv2.imread('../pic/test.png').astype(np.float32)

    # Grayscale
    gray = BGR2GRAY(origin_img)
    print(gray)

    # Otsu's binarization
    otsu = otsu_binarization(gray)

    cv2.imshow('otsu', otsu)

    # Morphology - dilate
    dilate_result = Morphology_Dilate(otsu, Dil_time=1)
    # Morphology - erode
    erode_result = Morphology_Erode(otsu, Erode_time=1)
    cv2.imshow('dilate_result', dilate_result)
    cv2.imshow('erode_result', erode_result)
    cv2.waitKey()
    cv2.destroyAllWindows()




        



