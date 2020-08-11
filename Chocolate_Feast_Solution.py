#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

tests = int(input())
for i in range(tests):

    raw = input().split(" ")
    cash = int(raw[0])
    price = int(raw[1])
    trades = int(raw[2])
    
    # Total candy
    total = 0
    
    candy = math.floor(cash / price)
    
    total += candy
    wrappers = candy
    
    
    while wrappers >= trades and trades > 0:
        extra = math.floor(wrappers / trades)
        total += extra
        wrappers = wrappers - extra*trades + extra
        
    print(total)

