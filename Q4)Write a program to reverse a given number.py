"""
Q4)Write a program to reverse a given number.
"""
"""
Syntax:
slice(stop)
slice(start, stop, step)
Parameters: 
start: Starting index where the slicing of object starts. 
stop: Ending index where the slicing of object stops. 
step: It is an optional argument that determines the increment between each index for slicing. 
Return Type: Returns a sliced object containing elements in the given range only. 

arr[start:stop]         # items start through stop-1
arr[start:]             # items start through the rest of the array
arr[:stop]              # items from the beginning through stop-1
arr[:]                  # a copy of the whole array
arr[start:stop:step]    # start through not past stop, by step
"""
print("Enter num to reverse:",end="\n")
print("Enter num:")
num=str(input())
print("original num:",num)
print("reverse num:",num[::-1])
