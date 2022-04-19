# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:59:24 2020

@author: siava
"""

import time

def time_function(f,*args):
    tic = time.time()
    f(*args)
    toc = time.time()
    return toc-tic

def Fib(n):
    
    if n==1 or n==2:
        return 1
            
    else:
        return Fib(n-1)+Fib(n-2)


    
memo = {}    
def Fib_memo(n):
    if n in memo:
        f = memo[n]
    elif n==1 or n==2:
        f = 1
          
    else:
        f = Fib_memo(n-1)+Fib_memo(n-2)
    memo[n] = f
        
    return f
        
fib = {}
def Fib_Bottomup(n):
    for i in range(1,n+1):
        if i==1 or i==2:
            f = 1
        else:
            f = fib[i-1]+fib[i-2]
        fib[i] = f
    return fib[n]

      

recursion = time_function(Fib,30)
print("Recursion takes %f seconds" % recursion)

memoization = time_function(Fib_memo,1000)
print("Memoization takes %f seconds" % memoization)

Bottom_up = time_function(Fib_Bottomup,1000)
print("Bottom_up takes %f seconds" % Bottom_up)