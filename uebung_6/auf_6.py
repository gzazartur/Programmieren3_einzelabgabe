#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:53:44 2018

@author: pyoneer
"""
import math
from functools import reduce

def f():
    return map(lambda x : math.cos(x)* math.exp(-x**2), range(0,7))

def f_reduce(lis):
    return reduce((lambda a,b : a if a > b else b),lis)


print("Ohne Reduce")
print(f())

print("Mit Reduce")

max_liste = [3,9,5,7,5,2,99]
print(f_reduce(max_liste))