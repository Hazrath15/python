#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:17:02 2019

@author: hazrath
"""
import datetime
name=input("Enter your name:")
age=int(input("Enter your age:"))
x = datetime.datetime.now()
y=int(x.year)
age=100-age
year = age+y
print(name,"will be 100 years old in",year)