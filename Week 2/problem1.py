# -*- coding: utf-8 -*-

#x = int (input('enter an integer: '))
#
#if x % 2 == 0:
#    print ('')
#    print ('Even')
#else:
#    print ('')
#    print ('odd')
#print ('done with conditional')

#x =float (input("enter a number for x: "))
#y =float (input("enter a number for y: "))
#if x == y:
#    print ("x and y are equal")
#    if y!= 0 :
#        print ("therefore, x / y is", x/y)
#elif x < y :
#    print ("x is smaller")
#else:
#    print ("y is smaller")
#print ("thanks!!")
#n=5
#if n>2:
#    print (n)
#    n-=1
#print (n)
#print ('hello')
#n=10
#while n>0:
#    print(n)
#n-=2
#iteration = 0
#count = 0
#while iteration < 5:
#    for letter in "hello, world":
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 2


s = str(input('phrase: '))

countvowels= 0
for char in s:
    
    if char == 'a' or char == 'e' or char == 'i'\
    or char == 'o' or char == 'u':
        countvowels +=1
        
print( 'Number of vowels: '+ str(countvowels))
        
    























