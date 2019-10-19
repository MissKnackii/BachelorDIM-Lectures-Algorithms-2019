# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:04 2019

@author: chaulaic
"""

import numpy as np

''' Averaging '''
    
def average_above_zero(tab:list):
    ##
    #Function that compute the average of positive value of an array
    # @param array 
    # return float

    if not (isinstance(tab, list)):
      raise ValueError('average_above_zero, expected a list as input')
    if len(tab) == 0:
        raise ValueError('expected a non empty list as input')
    if not(isinstance(tab[0], (int,float))):
        raise ValueError('average_above_zero, expected a list of numbers')
    
    som = 0
    n = 0
    for id in range(len(tab)):
        if tab[id] > 0 :
            som = som + tab[id]
            n = n + 1
    if n == 0: 
        raise ValueError('Division by 0 !!')
    
    return som / n


''' Maximum Value '''

'''
Max <- 0
for i <- 1 to NMAX do 
    if Tab[i] > Max then 
        Max <- Tab[i]

Display(Max)
'''

'''
Max <- 0
Index_Max <- 0
for i <- 1 to NMAX do 
    if Tab[i] > Max then 
        Max <- Tab[i]
        IndexMax <- i

Display(Max,i)
'''

def max_value(tab:list):
    ##
    #Function that compute the maximum value of an array
    # @param array
    # returns table
    
    if not(isinstance(tab, list)):
        raise ValueError('max_value, expected a list as input')
    if len(tab) == 0:
        raise ValueError('expected a non empty list as input')
    if not(isinstance(tab[0], (int,float))):
        raise ValueError('average_above_zero, expected a list of numbers')
    
    max = 0
    index_max = 0

    for id in range(len(tab)):
        if tab[id] > max:
            max = tab[id]
            index_max = id
    return max,index_max


''' Reverse table '''
'''
Size <- NMAX
Index <- Size - 1
it <- Size/2

for i <- 1 to it do 
    Temp <- Tab[Index]
    Tab[Index] <- Tab[i]
    Tab[i] <- Temp
    Index <- Index-1
Display(Tab)
'''

def reverse_table(tab):
    ##
    #Function to reverse a table
    # @param array
    # returns table
    
    if not(isinstance(tab, list)):
        raise ValueError('max_value, expected a list as input')
    if len(tab) == 0:
        raise ValueError('expected a non empty list as input')
    
    size = len(tab)
    index = size -1
    it = size // 2
    
    for id in range(it):
        temp = tab[index]
        tab[index] = tab[id]
        tab[id] = temp
        index = index - 1
    return tab


''' Bounding Box'''

def roi_bbox(input_image):
    ##
    #Function to compute the bounding box coordinates of an object
    # @param numpy array
    # returns numpy array

    if not(isinstance(input_image,np.ndarray)):
        raise ValueError('roi_bbox, expected a numpy array as input')
    if len(input_image) == 0:
        raise ValueError('roi_bbox, expected a non empty array as input')
    
    minCol = input_image.shape[1]
    minRow = input_image.shape[0]
    maxCol = 0
    maxRow = 0
    
    for idRow in range(input_image.shape[0]):
        for idCol in range(input_image.shape[1]):
            pixVal = input_image[idRow,idCol]
            if pixVal != 0:
                if idRow > maxRow:
                    maxRow = idRow
                if idCol > maxCol:
                    maxCol = idCol
                if idRow < minRow:
                    minRow = idRow
                if idCol < minCol:
                    minCol = minRow
    bbox = np.array([[minCol,minRow], [maxCol,minRow], [minCol, maxRow], [maxCol,maxRow]])
    return bbox