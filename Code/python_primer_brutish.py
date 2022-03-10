# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:34:28 2021

@author: Ariel
"""
import math
#make sure to download or use pip to get networkx and numpy
#Can everyone see this?

#Everything is data.

string = 'this is a string'
array = [1,2,3,'words', 'here is something I\'m saying', [math.pi, 5.4124]]

my_int = 1412415

my_int // 6


for value in array:
    
    print(type(value))
    
    if value == 3:
        print('moo')
    else:
        print('sheep')
    
    if type(value) == list:
        for value_in_list in value:
            print(value_in_list)
    elif type(value) == str:
        print(value + 'here is string addition')
    elif type(value) == int:
        print(value * math.pi)
        


#The dict class is the same idea as a hash map
my_dict = {1 : 'Ariel',
 2: 'Nancy',
 3: 'Jassem'}

for key, value in my_dict.items():
    print(key, value)
    
#A hashmap is good for pointing to object locations and a hash table is like a table with functions to convert objects

my_nested_dict = {
    
    
    0 : 1243124,
    17: 'julie',
    
    'names' : {1: 'Ariel', 2: 'Steven'}
    
    }


#Make a list using a for loop with all prime numbers from 1 to 100
#How do we check a number is prime? We can make a table or we can check every number up to that number's square root and see if it's prime:
    
#let's say our number is 19:

#16 : 16 would be composite.

# Give me a list of all perfect squares from 1: 100.

#use something called range

for num in range(10):
    print(num)

my_list_of_perfect_squares = []
for num in range(11):
    my_list_of_perfect_squares.append(num**2)
    
#You want to go to numbers up to 440:
list2 = []
num = 0
while num**2 < 440:
    list2.append(num**2)
    num += 1




for num in range(1,101):
    for factor in range(2,math.ceil(math.sqrt(num))):
        if num % factor == 0:
            print(num, ' this is a composite')
    print(num, '\t\tafter second for loop')
    



list_of_nums = []
for num in range(1,101):
    list_of_nums.append(num)
#The one below and above is equivalent
list_nums = [x for x in range(1,101)]
        

def is_prime(num, something = None):
    for value in range(2, math.ceil(math.sqrt(num))):
        if num % value == 0:
            return False
    return True


list_of_primes = []
for num in list_of_nums:
    if is_prime(num):
        list_of_primes.append(num)