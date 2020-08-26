"""
Created by HenryMa on 2020/8/24
"""

__author__ = 'HenryMa'


import math
from builtins import range, print
import numpy as np
import cv2


def gammaTransform(c, gamma, image):
    # 彩色图像
    """
    h, w, d = image.shape[0], image.shape[1], image.shape[2]
    new_img = np.zeros((h, w, d), dtype=np.float32)
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i, j, k] = c*math.pow(image[i, j, k], gamma)

    cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    print(new_img)
    new_img = cv2.convertScaleAbs(new_img)
    print(new_img)
    """

    # 灰度图
    h, w = image.shape[0], image.shape[1]
    new_img = np.zeros((h, w), dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * math.pow(image[i, j], gamma)
    cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)

    return new_img


if __name__ == '__main__':
    img = cv2.imread('../pic/Fig0309(a)(washed_out_aerial_image).tif', 0)
    # gamma_img1 = gammaTransform(1, 0.6, img)
    # gamma_img2 = gammaTransform(1, 0.4, img)
    # gamma_img3 = gammaTransform(1, 0.3, img)
    gamma_img4 = gammaTransform(1, 3.0, img)
    gamma_img5 = gammaTransform(1, 4.0, img)
    gamma_img6 = gammaTransform(1, 5.0, img)
    cv2.imshow('origin', img)
    # cv2.imshow('gamma_img1', gamma_img1)
    # cv2.imshow('gamma_img2', gamma_img2)
    # cv2.imshow('gamma_img3', gamma_img3)
    cv2.imshow('gamma_img4', gamma_img4)
    cv2.imshow('gamma_img5', gamma_img5)
    cv2.imshow('gamma_img6', gamma_img6)

    cv2.waitKey(0)


