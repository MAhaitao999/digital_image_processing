"""
Created by HenryMa on 2020/8/31
"""

__author__ = 'HenryMa'

from builtins import *

import cv2
import numpy as np


# def colormap_name(id):
#     switcher = {
#         0: 'COLORMAP_AUTUMN',
#         1: "COLORMAP_BONE",
#         2: "COLORMAP_JET",
#         3: "COLORMAP_WINTER",
#         4: "COLORMAP_RAINBOW",
#         5: "COLORMAP_OCEAN",
#         6: "COLORMAP_SUMMER",
#         7: "COLORMAP_SPRING",
#         8: "COLORMAP_COOL",
#         9: "COLORMAP_HSV",
#         10: "COLORMAP_PINK",
#         11: "COLORMAP_HOT"
#     }
#
#     return switcher.get(id, 'NONE')


if __name__ == '__main__':
    img = cv2.imread('../pic/baboon.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (200, 200))

    img_out = np.zeros((600, 800, 3), dtype=np.uint8)

    for i in range(3):
        for j in range(4):
            k = i * 4 + j
            img_tmp = cv2.applyColorMap(img, k)
            img_out[i*200: i*200+200, j*200: j*200+200, :] = img_tmp
    cv2.imshow('result',  img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





