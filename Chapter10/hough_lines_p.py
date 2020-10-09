"""
Created by HenryMa on 2020/10/9
"""

__author__ = 'HenryMa'

from builtins import print

"""
cv2.HoughLinesP(dst, lines, 1, CV_PI/180, 50, 50, 10)
    dst: 输出图像. 它应该是个灰度图(但事实上是个二值化图)
    lines: 储存着检测到的直线的参数对(x_{start}, y_{start}, x_{end}, y_{end})的容器
    rho: 参数极径 r 以像素值为单位的分辨率. 我们使用 1 像素.
    theta: 参数极角 theta 以弧度为单位的分辨率. 我们使用1度 (即CV_PI/180)
    threshold: 设置阈值: 一条直线所需最少的的曲线交点. 超过设定阈值才被检测出线段, 值越大, 基本上意味着检出的线段越长, 检出的线段个数越少
    minLinLength: 能组成一条直线的最少点的数量. 点数量不足的直线将被抛弃.
    maxLineGap: 能被认为在一条直线上的两点的最大距离.
"""


import cv2
import numpy as np

img = cv2.imread('./pic/jianzhu.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gray, (3, 3), 0)
edges = cv2.Canny(gauss, 50, 150, apertureSize=3)

# 经验参数
minLineLength = 200
maxLineGap = 15
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 80, minLineLength, maxLineGap)
print(lines[0])
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
