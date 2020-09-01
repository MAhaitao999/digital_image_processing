"""
Created by HenryMa on 2020/8/31
"""

__author__ = 'HenryMa'

from builtins import *

import cv2
import numpy as np


def colormap_name(id):
    switcher = {
        0: 'COLORMAP_AUTUMN',
        1: "COLORMAP_BONE",
        2: "COLORMAP_JET",
        3: "COLORMAP_WINTER",
        4: "COLORMAP_RAINBOW",
        5: "COLORMAP_OCEAN",
        6: "COLORMAP_SUMMER",
        7: "COLORMAP_SPRING",
        8: "COLORMAP_COOL",
        9: "COLORMAP_HSV",
        10: "COLORMAP_PINK",
        11: "COLORMAP_HOT"
    }

    return switcher.get(id, 'NONE')


if __name__ == '__main__':
    img = cv2.imread('../pic/baboon.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (800, 600))
    print(img.shape)
    img_out = np.zeros(img.shape, np.uint8)

    for i in range(0, 4):
        for j in range(0, 3):
            k = i + j * 4
            img_color = cv2.applyColorMap(img, k)
            cv2.putText(img_color, colormap_name(k), (30, 180),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
            ix200 = i * 200
            jx200 = j * 200
            img_out[jx200: jx200 + 200, ix200: ix200 + 200, :] = img_color

    cv2.imshow('result', img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





