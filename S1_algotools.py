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
    
def average_above_zero(tab:list):
    ##
    #Function that compute the average of positive value of an array
    # @param array
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

print('Moyenne = ' + str(average_above_zero(tab_list)))

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
    
    if not(isinstance(tab, list)):
        raise ValueError('max_value, expected a list as input')
    
    max = 0
    index_max = 0

    for id in range(len(tab)):
        if tab[id] > max:
            max = tab[id]
            index_max = id
    return max,index_max

print('Valeur max et index : ' + str(max_value(tab_list)))

'''
Reverse table 

A<-0
B<-0
C<-0
for i <- 1 to NMAX do 
    A<-Tab[i]
    B<-Tab[NMAX - i]
    C<-B
    A<-B
    B<-C
Display(Tab)
'''
a = 0
b = 0
c = 0

for id in range(len(tab_list)):
    a = tab_list[id]
    b = tab_list[len(tab_list) - id]
    c = b
    a = b
    b = c

print(str(tab_list))