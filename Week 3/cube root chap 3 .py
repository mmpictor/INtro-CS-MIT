#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:58:17 2018

@author: MASTER
"""

cube = 27 # start off with some value/im try to find the cube root of.
epsilon = 0.01 #how close i want to get to the answer 
guess = 0.0    #where i'm going to start 
increment = 0.0001 # the size in wich i'm going to increase my guess as i move along.
num_guesses = 0 # how many times do i go through the loop as i do this 
#while the differences between the guess cube and the thing im trying to find. while that difference still bigger than epsilon 
while abs (guess ** 3 - cube) >= epsilon:
        guess += increment # im poing to keep going by incrementing guess
        num_guesses += 1 #changing by 1/i've done another guess & keep going
print ('num_guesses =', num_guesses) #return how many guesses did i run 
if abs (guess ** 3 - cube ) >= epsilon:
    print ('failed on cube root of', cube)
else:
    print (guess, 'is close to the cube root of',cube)#some inf.about did i find the right answer
#step colud be any small number 
#if too small, takes along time to find the solution
#if too large, might skip over answer without getting close enough
#in general will take x/step times through code to find the solution