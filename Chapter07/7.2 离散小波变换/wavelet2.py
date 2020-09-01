"""
Created by HenryMa on 2020/9/1
"""

__author__ = 'HenryMa'


import numpy as np
import pywt
import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    img = cv2.imread('../pic/cat.png')
    img = cv2.resize(img, (448, 448))
    # 将多通道图像变为单通道图像
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)

    plt.figure('二维小波一级变换')
    coeffs = pywt.dwt2(img, 'haar')

    cA, (cH, cV, cD) = coeffs

    # 将各个子图进行拼接, 最后得到一张图
    AH = np.concatenate([cA, cH], axis=1)
    VD = np.concatenate([cV, cD], axis=1)
    img = np.concatenate([AH, VD], axis=0)

    # 显示为灰度图
    plt.imshow(img, 'gray')
    plt.title('result')
    plt.show()

    # img_out = cv2.resize(cA, (448, 448))
    # plt.imshow(img_out, 'gray')
    # plt.show()

