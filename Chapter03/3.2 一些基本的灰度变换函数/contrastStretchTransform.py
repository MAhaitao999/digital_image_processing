"""
Created by HenryMa on 2020/8/24
"""

__author__ = 'HenryMa'


import math
from builtins import range, print
import numpy as np
import cv2


def contrastStretchTransform(image):
    """
    灰度拉伸
    定义: 灰度拉伸, 也称对比度拉伸, 是一种简单的线性点运算.
    作用: 扩展图像的直方图, 使其充满整个灰度等级范围内.
    公式: A = min[f(x, y)], 最小灰度级;
         B = max[f(x, y)], 最大灰度级;
         f(x, y)为输入图像, g(x, y)为输出图像.
    缺点: 如果灰度图像中最小值A=0, 最大值B=255, 则图像没有什么改变.
    """
    # 彩色图像
    h, w, d = image.shape[0], image.shape[1], image.shape[2]
    new_img = np.zeros((h, w, d), dtype=np.float32)
    A = image.min()
    B = image.max()
    print(A, B)
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i, j, k] = 255.0 / (B - A) * (image[i, j, k] - A) + 0.5
    new_img = cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)

    return new_img


if __name__ == '__main__':
    img = cv2.imread('../pic/beizi.png', 1)
    contrast_img = contrastStretchTransform(img)
    cv2.imshow('src img', img)
    cv2.imshow('contrast img', contrast_img)
    cv2.waitKey(0)

