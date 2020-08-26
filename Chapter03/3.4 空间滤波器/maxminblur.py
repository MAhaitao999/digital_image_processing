"""
Created by HenryMa on 2020/8/26
"""

__author__ = 'HenryMa'

from builtins import range, Exception

import numpy as np
import cv2
import matplotlib.pyplot as plt


def max_min_blur(image, ksize=3, mode=1):
    """
    :param image: 原始图像
    :param ksize: 卷积核大小
    :param mode: 最大值: 1 或 最小值 0
    :return:
    """
    img = image.copy()
    rows, cols, channels = img.shape

    if channels == 3:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    padding = (ksize - 1) // 2
    new_img = cv2.copyMakeBorder(img, padding, padding, padding, padding, cv2.BORDER_CONSTANT, value=255)

    for i in range(rows):
        for j in range(cols):
            roi_img = new_img[i:i+ksize, j:j+ksize].copy()
            min_val, max_val, min_index, max_index = cv2.minMaxLoc(roi_img)
            if mode == 1:
                img[i, j] = max_val
            elif mode == 0:
                img[i, j] = min_val
            else:
                raise Exception('please Select a mode: max(1) or min(0)')

    return img


if __name__ == '__main__':
    # 读取图片
    img = cv2.imread('../pic/Fig0335(a)(ckt_board_saltpep_prob_pt05).tif')

    result = max_min_blur(img, 2, 0)

    # 显示图形
    titles = ['Source Image', 'Blur Image']
    images = [img, result]
    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

