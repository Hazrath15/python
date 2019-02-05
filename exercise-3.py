#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 23:15:00 2019

@author: hazrath
"""
# Ask the user for a string and print out whether this string is a palindrome or not.

raw = str(input("Enter a string: "))
raw.replace(" ", "")
set1 = str.lower(raw[::-1])
set2 = str.lower(raw[0::])
if set2 == set1:
    print("Palindrome")
else:
    print("Not a palindrome")