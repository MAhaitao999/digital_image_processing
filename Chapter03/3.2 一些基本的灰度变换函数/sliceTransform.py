"""
Created by HenryMa on 2020/8/24
"""

__author__ = 'HenryMa'


import math
from builtins import range, print
import numpy as np
import cv2


def sliceTransform(image):
    # 二值映射
    """
    h, w = image.shape[0], image.shape[1]
    new_img = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if image[i, j] < 190 or image[i, j] > 230:
                new_img[i, j] = 0
            else:
                new_img[i, j] = 255
    """

    # 区域映射
    h, w = img.shape[0], img.shape[1]
    new_img = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if 230 >= img[i, j] >= 190:
                new_img[i, j] = 255
            else:
                new_img[i, j] = img[i, j]

    return new_img


if __name__ == '__main__':
    img = cv2.imread('../pic/Fig0312(a)(kidney).tif', 0)
    slice_img = sliceTransform(img)
    cv2.imshow('source img', img)
    cv2.imshow('slice img', slice_img)
    cv2.waitKey(0)

