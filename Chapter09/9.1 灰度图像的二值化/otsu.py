"""
Created by HenryMa on 2020/9/14
"""

__author__ = 'HenryMa'

import time
from builtins import *

import cv2
import numpy as np


def OTSU_enhance(img_gray, th_begin=0, th_end=256, th_step=1):
    assert img_gray.ndim == 2, 'must input a gray image'

    max_g = 0
    suitable_th = 0
    for threshold in range(th_begin, th_end, th_step):
        bin_img = img_gray > threshold
        bin_img_inv = img_gray <= threshold
        # print(bin_img)
        # print(bin_img_inv)
        fore_pix = np.sum(bin_img)  # 前景像素总数
        back_pix = np.sum(bin_img_inv)  # 背景像素总数
        if 0 == fore_pix:
            break
        if 0 == back_pix:
            continue

        w0 = float(fore_pix) / img_gray.size
        u0 = float(np.sum(img_gray * bin_img)) / fore_pix
        w1 = float(back_pix) / img_gray.size
        u1 = float(np.sum(img_gray * bin_img_inv)) / back_pix

        # intra-class variance
        g = w0 * w1 * (u0 - u1) * (u0 - u1)
        if g > max_g:
            max_g = g
            suitable_th = threshold

    return suitable_th


if __name__ == '__main__':
    img = cv2.imread('/home/transwarp/Downloads/cat.jpg', 0)
    # cv2.imshow('原图', img)
    suit_th = OTSU_enhance(img)
    print(suit_th)
    # for i in range(img.shape[0]):
    #     for j in range(img.shape[1]):
    #         img[i, j] = 0 if img[i, j] < suit_th else 255
    # cv2.imshow('二值图', img)
    t1 = time.time()
    result = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    t2 = time.time()
    print("binary cost time: {}ms".format((t2-t1)*1000))
    print(result[0])
    print(result[1])
    cv2.imshow('binary image', result[1])
    cv2.waitKey()
    cv2.destroyAllWindows()
