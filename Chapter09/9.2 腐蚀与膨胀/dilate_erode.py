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


# Otsu Binarization
def otsu_binarization(img, th=128):
    H, W = img.shape
    out = img.copy()

    max_sigma = 0
    max_t = 0

    # determine threshold
    for _t in range(1, 255):
        v0 = out[np.where(out < _t)]
        



