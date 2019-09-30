# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:11:01 2019

@author: chaulaic
"""
import S1_algotools as S1tested
import pytest

'''def test_list_expected(tab):
    tab_list = [1,2,3-4,6,-9]
    print('Moyenne = ' + str(S1tested.average_above_zero(tab_list))'''

def test_average_above_zero():
    tab_list = [1,2,3-4,6,-9]
    test = S1tested.average_above_zero(tab_list)
    assert test == 3

def test_average_divide_by_zero():
    tab_empty = []
    tab_neg = [3-4,-9]
    with pytest.raises(ZeroDivisionError):
        S1tested.average_above_zero(tab_empty)
        S1tested.average_above_zero(tab_neg)


    