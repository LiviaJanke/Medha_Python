#!/usr/bin/env python3
# -*- coding: utf-8 -
"""
Created on Sat Feb 28 17:38:38 2026

@author: livia
"""
import numpy as np




#%%

"""
Q2: Return multiple values from a function
Write a program to create function calculation() such that it can accept two variables and
calculate addition and subtraction. Also, it must return both addition and subtraction in a
single return call.
Hint:
• Separate return values with a comma.
"""

def calculation(a,b):
    
    return a+b, a-b
 
result = calculation(2,5)   
    
added, subtracted = calculation(3,7)  


#%%

"""
Q3: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the
current and previous number.
Hint:
• Create a variable called previous_num and assign it to 0.
• Iterate the first 10 numbers one by one using for loop and built-in function range().
• Next, display the current number (i), previous number, and the addition of both numbers
in each iteration of the loop. At last, change the value previous number to current number
(previous_num = i).
"""


print("Printing current and previous number and their sum in a range(10)")


previous_num = 0

for i in range(0,11,1):
    print(i+previous_num)
    previous_num = i
    




"""
Q4: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5.
"""

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')


for num in num_list:
    
    if num % 5 == 0:
        
        print(num)

# '%'  is the modulus operator

print('Non-divisible items')

for num in num_list:
    
    if num % 5 != 0:
        
        print(num)


#%%

"""
Q5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers
are different then return False.
"""

# comment

def first_last_same(a):
    
    if a[0] == a[-1]:
        return True
        
    else:
        return False

print(first_last_same(num_list))

num_list2 = [1,2,3,4,56,1]

print(first_last_same(num_list2))


"""
Q6: Create a new list from two lists using the following condition
Given two lists of numbers, write a program to create a new list such that the new list should
contain odd numbers from the first list and even numbers from the second list.
Hint:
• Create an empty list named result_list.
• Iterate first list using a for loop.
• In each iteration, check if the current number is odd number using num % 2 != 0 formula.
If the current number is an odd number, add it to the result list.
• Now, Iterate the first list using a loop.
• In each iteration, check if the current number is odd number using num % 2 == 0 formula.
If the current number is an even number, add it to the result list.
"""

num_list = [10, 20, 33, 46, 55]

num_list2 = [1,2,3,4,56,1]

result_list = []

for i in num_list:
    
    if i % 2 != 0:
        
        result_list.append(i)
    
for i in num_list2:
    
    if i % 2 == 0:
        
        result_list.append(i)

#%%


def merge_list(a,b):
    
    result_list = []

    for i in a:
        
        if i % 2 != 0:
            
            result_list.append(i)

    for i in b:
        
        if i % 2 == 0:
            
            result_list.append(i)
    
    return result_list
    

merge_list(num_list,num_list2)


#%%

"""
Q7: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new
string. For example:
• remove_chars("pynative", 4) so output must be tive. Here we need to remove first
four characters from a string.
• remove_chars("pynative", 2) so output must be native. Here we need to remove first
two characters from a string.
Hint: - Use string slicing to get the substring. For example, to remove the first four characters
and the remeaning use s[4:].
"""

string1 = 'Learn to use the debugger...'

print(string1[27])

n = 5

#%%

def chopper(strin, n):
    reduced_string = strin[n:]

    return reduced_string


chopper("pynative",2)


#%%

"""
Q8: Calculate income tax for the given income by adhering to the below rules


Taxable Income  | Rate in %
______________________________
First $10,000   |     0
______________________________
Next 10,000     |    10 
______________________________
The Remaining   |    20

 
Example:
• Suppose the taxable income is 45000 the income tax payable is 10000*0% + 10000*10%
+ 25000*20% = $6000

"""

income = 45000

pay = 0

if income <= 10000:
    pay = 0

elif income <= 20000:
    pay = (0.1 * (income - 10000))
    
else:
    pay = (0.1 * 10000)+ (0.2 * (income -  20000))


print(pay)



def income_tax(a):
    
    pay = 0

    if a <= 10000:
        pay = 0

    elif a <= 20000:
        pay = (0.1 * (a - 10000))
        
    else:
        pay = (0.1 * 10000)+ (0.2 * (a -  20000))

    return pay


#%%

"""
Q9: Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of each element and create a
dictionary to show the count of each element.
"""
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)






"""
Q10: Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in
the middle of s1.
Hint:
• Use built-in function len(s1) to get the string length.
• Next, get the middle index number by dividing string length by 2.
"""


























