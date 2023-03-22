#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
def f(x):
    return x**4+8*x**2-9
def df(x):
    return 4*x**3+16*x
x0 = 1
tolerance = 1e-6
max_iterations=100
count=0

for i in range(max_iterations):
    fx = f(x0)
    dfx = df(x0)
    x1 = x0 - (f(x0)/dfx)
    
    if abs (f(x1)) < tolerance:
        print(f"Root found at x={x1:.6f}")
        break
    
    else:
        x0=x1
          
print(count)
    

