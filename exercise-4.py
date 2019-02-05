#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:48:39 2019

@author: hazrath
"""

import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result_overlap = [i for i in set(a) if i in b]
result = []
for element in result_overlap:
  if element not in result:
    result.append(element)
print(a)
print(b)   
print(result)