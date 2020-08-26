"""
Created by HenryMa on 2020/8/26
"""

__author__ = 'HenryMa'

from builtins import range

import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 读取图片
    img = cv2.imread('../pic/Fig0335(a)(ckt_board_saltpep_prob_pt05).tif')

    # result = cv2.blur(img, (3, 3))
    result = cv2.boxFilter(img, -1, (2, 2), normalize=1)

    # 显示图形
    titles = ['Source Image', 'Blur Image']
    images = [img, result]
    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
