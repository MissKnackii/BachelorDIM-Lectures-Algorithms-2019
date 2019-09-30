# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:31:19 2019

@author: chaulaic
"""

import cv2
import numpy as np

img_gray = cv2.imread('imgGray.png',0)
img_bgr = cv2.imread('img.png',1)

print("Gray levels image shape = " + str(img_gray.shape[0]))
print("BGR image shape = " + str(img_bgr.shape))

cv2.imshow("Gray levels image",img_gray)
cv2.imshow("BGR image", img_bgr)
