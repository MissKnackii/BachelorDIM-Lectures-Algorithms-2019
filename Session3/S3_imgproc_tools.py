# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:31:19 2019

@author: chaulaic
"""

import cv2
import numpy as np

img = cv2.imread('/Algo/BachelorDIM-Lectures-Algorithms-2019/Session3/trump.jpg')
cv2.imshow('input',img)
cv2.waitKey()

print('image shape: ',img.shape)

def invert_colors_manual(input_img):   
    for row in range(input_img.shape[0]):
        for col in range(input_img.shape[1]):
            for cha in range(input_img.shape[2]):
                img[row,col,cha] = 255-img[row,col,cha]
    return input_img
            
cv2.imshow('inverted input',invert_colors_manual(img))
cv2.waitKey()