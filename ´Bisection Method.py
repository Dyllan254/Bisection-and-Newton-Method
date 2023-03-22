#!/usr/bin/env python
# coding: utf-8

# In[11]:


import math

def f(x):
    return x**4+8*x**2-9
a = 1
b = -1

tolerance = 1e-6
max_iterations=100

for i in range (max_iterations):
    c = (a+b)/2
    if abs(f(c))<tolerance:
        print(f"Root found at x = {c: .6f}")
        break
        
    elif f(c)*f(a)<0:
            b=c
    else:
        a=c
 

