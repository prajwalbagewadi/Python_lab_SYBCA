"""
4. Write a Python program to calculate the Length of a String without using a Library Function.
"""
str_val=input("enter str val:")

#logic to calculate length 
count=0
"""
for loop:
For loops are used for sequential traversal. 
For example: traversing a list or string or array etc. 
In Python, there is “for in” loop which is similar to foreach loop in other languages. 

For Loop Syntax:

for iterator_var in sequence:
    statements(s)
"""
for char in str_val:
    count+=1

print("final length of the string:",count)
