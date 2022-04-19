# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:43:07 2020

@author: siava
"""

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    right = [x for x in arr if x>pivot]
    middle = [x for x in arr if x==pivot]
    return quicksort(left)+middle+quicksort(right)



#print (quicksort(list(A)))
    
print(quicksort([90,1,34,12,89,76,56,45,12,45,10]))