"""
Created by HenryMa on 2020/10/9
"""

__author__ = 'HenryMa'

from builtins import print, int

"""
cv2.HoughLines()
    dst: 输出图像, 它应该是个灰度图(但事实上是个二值化图)
    lines: 储存着检测到的直线的参数对(r, theta)的容器
    rho : 参数极径 r 以像素值为单位的分辨率. 我们使用 1 像素.
    theta: 参数极角 theta 以弧度为单位的分辨率. 我们使用 1度 (即CV_PI/180)
    threshold:    设置阈值： 一条直线所需最少的的曲线交点
    srn and stn: 默认参数为0
"""

import cv2
import numpy as np


origin_img = cv2.imread('./pic/jianzhu.png', 0)
print(origin_img)
img = cv2.resize(origin_img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)


img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 118)  # 这里对最后一个参数使用了经验型的值
result = img.copy()
for line in lines:
    rho = line[0][0]  # 第一个元素是距离rho
    theta = line[0][1]  # 第二个元素是角度theta
    print(rho)
    print(theta)
    if (theta < (np.pi/4.)) or (theta > (3.*np.pi/4.0)):  # 垂直直线
        pt1 = (int(rho/np.cos(theta)), 0)  # 该直线与第一行的交点
        pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)), result.shape[0])  # 该直线与最后一行的交点
        cv2.line(result, pt1, pt2, 255)  # 绘制一条白线
    else:
        pt1 = (0, int(rho/np.sin(theta)))  # 该直线与第一列的交点
        pt2 = (result.shape[1], int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))  # 该直线与最后一列的交点
        cv2.line(result, pt1, pt2, 255, 1)  # 绘制一条直线

cv2.imshow('edges', edges)
cv2.imshow('Result', result)
cv2.waitKey()
cv2.destroyAllWindows()
