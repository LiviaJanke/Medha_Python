#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:56:23 2026

@author: livia
"""

import numpy as np


#%%


"""
Q1: Create a 2D NumPy array
• Create a 5x2 integer array from a range between 100 and 200 such that the difference
between each element is 10.
• Print the array and its shape.
Hint:
• Use NumPy arange() and reshape().
"""


array_1 = np.arange(100,200,10)

array_1 = array_1.reshape((5,2))


#%%

"""
Q2: Reverse a 1D array
Write a function to reverse an array (the first element becomes the last).
"""


print("Original array:")
a = np.array([1, 2, 5, 10, 15, 86])
print(a)

a_reversed = a[::-1]

# Can't reverse while indexing????


#%%


"""
Q3: Multiply a 2D array by a scalar
Given a 2D array (matrix), return an array, which is equal to the original matrix multiplied by
2.
"""

a2 = np.array([[1,2,3],[4,5,6]])

print(a2 * 2)


def array_doubler(arr):
    
    return arr * 2
































