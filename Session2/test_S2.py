# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:11:01 2019

@author: chaulaic
"""
import S1_algotools as S1tested
import pytest

#Test average_above_zero

def test_averageAboveZero_ReturnAver():
    ##
    #Function to test the return of the good average of a list
    tab_list = [1,2,3-4,6,-9]
    test = S1tested.average_above_zero(tab_list)
    assert test == 3

def test_averageAboveZero_divideByZero():
    ##
    #Function to test the launch of an error when division by zero 
    tab_neg = [3-4,-9]
    with pytest.raises(ValueError):
        S1tested.average_above_zero(tab_neg)
        
def test_averageAboveZero_listExpected():
    ##
    #Function to test the launch of an error when the argument is not a list
    var = 25
    with pytest.raises(ValueError):
        S1tested.average_above_zero(var)

def test_averageAboveZero_nonEmptyList():
    ##
    #Function to test the launch of an error when the list is empty
    tab_empty = []
    with pytest.raises(ValueError):
        S1tested.average_above_zero(tab_empty)
        
def test_averageAboveZero_numberListExpected():
    ##
    #Function to test the launch of an error when the list is composed by char
    tab_of_char = ['','']
    with pytest.raises(ValueError):
        S1tested.average_above_zero(tab_of_char)

#Test max_value
def test_maxValue_returnMax():
    ##
    #Function to test the return of the maaximum value of a list
    tab_list = [1,2,4,6,-9]
    test, i = S1tested.max_value(tab_list)
    assert test == 6
    assert i == 3

def test_maxValue_listExpected():
    ##
    #Function to test the launch of an error when the argument is not a list
    var = 25
    with pytest.raises(ValueError):
        S1tested.max_value(var)
        
def test_maxValue_nonEmptyListExpected():
    ##
    #Function to test the launch of an error when the list is empty
    tab_empty = []
    with pytest.raises(ValueError):
        S1tested.max_value(tab_empty)
        
def test_maxValue_numberListExpected():
    ##
    #Function to test the launch of an error when the list is composed by char
    tab_of_char = ['','']
    with pytest.raises(ValueError):
        S1tested.max_value(tab_of_char)

#Reverse table

def test_reverseTable_returnReverseTable():
    tab_list=[1,2,3,-4,6,-9] 
    assert s1.reverse_table(tab_list) == [-9, 6,-4, 3, 2, 1]

def test_reverseTable_listExpected():
    with pytest.raises(ValueError):
        s1.reverse_table(3)

def test_reverseTable_nonEmptyListExpected():
    with pytest.raises(ValueError):
        s1.reverse_table([]) 

#Bounding Box

import cv2
import numpy as np

def test_roiBbox_correct():
    img=cv2.imread('img.png',0)
    assert (s1.roi_bbox(img) == np.array([[ 91,  95], [ 91, 523], [434, 523], [434,  95]])).prod()

def test_roiBbox_NumpyArrayExpected():
    with pytest.raises(TypeError):
        s1.roi_bbox(3)

def test_roiBbox_nonEmptyArrayExpected():
    with pytest.raises(ValueError):
        s1.roi_bbox(np.array([])) 