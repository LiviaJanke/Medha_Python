#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:46:53 2026

@author: livia
"""

import numpy as np





#%%

list1 = [[1.1,2,3,4],[5,6,7,8]]


#%%

arr1 = np.array(list1)


arr2 = np.linspace(0,2,10)

arr3, step3 = np.linspace(0,2,num = 10, endpoint = False, retstep = True)

arr4 = np.arange(0,50,10)


arr5 = np.zeros((5,6))

arr6 = np.random.random((5,6))

#%%

np.savetxt("output.txt", arr6)


#%%

arr6_v2 = np.loadtxt("output.txt")

arr6_tr = arr6.T 


#%%

arr7 = np.arange(1,10)
arr8 = arr7.reshape((3,3))


#%%

str1 = 'abc'

str3 = 'def'


str1 + str3



arr_concat = np.concatenate([arr7.reshape((3,3)),arr8],axis =1)


arr_hstack = np.hstack([arr5,arr6[:,0:1]])


arr_vstack = np.vstack(([arr5,arr6[1:2,]]))

#%%


a = np.array([0, 1, 2, 3,5])
b = np.array(([2, 3, 2, 4],[5,6,7,8]))


#%%


u = [0, 1, 2]
v = [1, 2, 3]



print(np.dot(u, v))

# Matrix multiplication is:
print(np.outer(u, v))


B = np.ones((2, 3))
print(B)


#%%

a = np.array([[1,2,3], [4,5,6]])
print(a)


