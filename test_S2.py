# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:11:01 2019

@author: chaulaic
"""
import S1_algotools as S1tested
import pytest

#Test average_above_zero
def test_average_above_zero():
    ##
    #Function to test the return of the good average of a list
    tab_list = [1,2,3-4,6,-9]
    test = S1tested.average_above_zero(tab_list)
    assert test == 3

def test_average_above_zero_divide_by_zero():
    ##
    #Function to test the launch of an error when division by zero 
    tab_neg = [3-4,-9]
    with pytest.raises(ValueError):
        S1tested.average_above_zero(tab_neg)
        
def test_average_above_zero_list_expected():
    ##
    #Function to test the launch of an error when the argument is not a list
    var = 25
    with pytest.raises(ValueError):
        S1tested.average_above_zero(var)

def test_average_above_zero_non_empty_list():
    ##
    #Function to test the launch of an error when the list is empty
    tab_empty = []
    with pytest.raises(ValueError):
        S1tested.average_above_zero(tab_empty)
        
def test_average_above_zero_number_list_expected():
    ##
    #Function to test the launch of an error when the list is composed by char
    tab_of_char = ['','']
    with pytest.raises(ValueError):
        S1tested.average_above_zero(tab_of_char)

#Test max_value
def test_max_value():
    ##
    #Function to test the return of the maaximum value of a list
    tab_list = [1,2,4,6,-9]
    test, i = S1tested.max_value(tab_list)
    assert test == 6
    assert i == 3

def test_max_value_list_expected():
    ##
    #Function to test the launch of an error when the argument is not a list
    var = 25
    with pytest.raises(ValueError):
        S1tested.max_value(var)
        
def test_max_value_non_empty_list():
    ##
    #Function to test the launch of an error when the list is empty
    tab_empty = []
    with pytest.raises(ValueError):
        S1tested.max_value(tab_empty)
        
def test_max_value_number_list_expected():
    ##
    #Function to test the launch of an error when the list is composed by char
    tab_of_char = ['','']
    with pytest.raises(ValueError):
        S1tested.max_value(tab_of_char)