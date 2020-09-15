"""
Created by HenryMa on 2020/9/15
"""

__author__ = 'HenryMa'

from builtins import *

import cv2
import numpy as np

img = cv2.imread('../pic/car_license_number.png', cv2.IMREAD_GRAYSCALE)
thresh, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
print(img)
# cv2.imshow('binary image', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

arr = np.array(img)
mat = [np.array([[-1, -1, -1], [0, 1, 0], [1, 1, 1]]),
       np.array([[0, -1, -1], [1, 1, -1], [1, 1, 0]]),
       np.array([[1, 0, -1], [1, 1, -1], [1, 0, -1]]),
       np.array([[-1, -1, -1], [0, 1, 0], [1, 1, 1]]),
       np.array([[1, 1, 0], [1, 1, -1], [0, -1, -1]]),
       np.array([[1, 1, 1], [0, 1, 0], [-1, -1, -1]]),
       np.array([[-1, 0, -1], [-1, 1, 1], [-1, 0, 1]]),
       np.array([[-1, -1, 0], [-1, 1, 1], [0, 1, 1]])]

height, width = arr.shape
print(height, width)

while True:  # 迭代至无变化
    before = arr.copy()
    print('before is: ', before)
    for m in mat:  # 使用八个模板进行变换
        mark = []
        for i in range(height - 2):
            for j in range(width - 2):
                reg = True
                for im in range(3):
                    for jm in range(3):
                        if not arr[i+1][j+1] == 255:
                            continue
                        if m[im][jm] == 1 and arr[i+im][j+jm] == 0:
                            reg = False
                        if m[im][jm] == -1 and arr[i+im][j+jm] == 255:
                            reg = False
                if reg:  # 找到标记, 删除
                    mark.append((i+1, j+1))
        for it in mark:
            x, y = it
            arr[x][y] = 0
    if (before == arr).all():
        break


cv2.imshow('binary pic', img)
cv2.imshow('thin pic', arr)
cv2.waitKey(0)
cv2.destroyAllWindows()




