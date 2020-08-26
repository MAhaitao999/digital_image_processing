"""
Created by HenryMa on 2020/8/26
"""

__author__ = 'HenryMa'


import cv2
import numpy as np


if __name__ == '__main__':

    img = cv2.imread('../pic/Fig0304(a)(breast_digital_Xray).tif', 0)

    """
    由于Canny只能处理灰度图, 所以将读取的图像转成灰度图.
    用高斯平滑处理原图像降噪.
    调用Canny函数, 指定最大和最小阈值, 其中apertureSize默认为3
    """
    img = cv2.GaussianBlur(img, (3, 3), 0)
    canny = cv2.Canny(img, 50, 150)

    cv2.imshow('origin', img)
    cv2.imshow('Canny', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
