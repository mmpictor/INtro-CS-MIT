#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:42:44 2018

@author: MASTER
"""

s = str(input('input a lower case char: '))

countbob = 0 

for index in range (len(s)) :
    if s[index] == 'b'and s[index + 1]== 'o' and s[index + 2] == 'b':
        countbob += 1
print('Number of times bob occur is: ' + str(countbob))


