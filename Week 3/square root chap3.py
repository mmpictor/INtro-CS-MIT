#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:08:08 2018

@author: MASTER
"""
# bisection search
# cube root
x = 25 # start off 
epsilon = 0.01 # how close i am 
numguesses = 0 # how often run through the loop 
low = 0.0 # range initialized
high = x  # range 
ans = (high + low)/2.0 # make an initial guess/halfway in between

while abs (ans **2-x) >= epsilon:
    print ('low = ' + str(low) + 'high =' + str(high) + 'ans=' + str(ans))
    numguesses +=1
    if ans**2 < x:
        low = ans 
    else:
        high = ans 
    ans = (high + low)/2.0
print('numguesses: ' + str(numguesses))
print(str(ans) + 'is close to square root of: ' + str(x))