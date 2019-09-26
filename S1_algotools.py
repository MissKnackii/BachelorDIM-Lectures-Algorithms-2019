# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:04 2019

@author: chaulaic
"""

print('Hello World!')

myVar = 6
print('MyVariable = ',myVar)

'''If Som initialization is forgotten, Som will not be correct because the initialization will be ramdom'''
'''The value of N and Som will stay at 0 so the program will crash because to initialize Moy we will divide by 0'''

########
tab_list = [1,2,3-4,6,-9]

import numpy as np
tab_zeros = np.zeros(12, dtype=np.int32) 
tab_from_list = np.array(tab_list)
#print('tab[' + str(id) + ']=' + str(tab_from_list[id]))
#print('tab[{index}]={val}'.format(index=id, val=tab_from_list[id]))
    
def average_above_zero(tab):
    ##
    #Function that compute the average of positive value of an array
    # @param array
    
    som = 0
    n = 0
    for id in range(len(tab)):
        if tab[id] > 0 :
            som = som + tab[id]
            n = n + 1
    moy = som / n
    return moy

print('Moyenne = ' + str(average_above_zero(tab_from_list)))