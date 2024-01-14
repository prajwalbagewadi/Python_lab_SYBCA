"""
Write a program which accepts 6 integer values and prints “DUPLICATES” 
if any of the values entered are duplicates otherwise it prints “ALL UNIQUE”.
Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed.
"""
"""
    no	Method	    Description
    1	append()	Used for adding elements to the end of the List. 
    2	copy()	    It returns a shallow copy of a list
    3	clear()	    This method is used for removing all items from the list. 
    4	count()	    These methods count the elements.
    5	extend()	Adds each element of an iterable to the end of the List
    6	index()	    Returns the lowest index where the element appears. 
    7	insert()	Inserts a given element at a given index in a list. 
    8	pop()	    Removes and returns the last value from the List or the given index value.
    9	remove()	Removes a given object from the List. 
    10	reverse()	Reverses objects of the List in place.
    11	sort()	    Sort a List in ascending, descending, or user-defined order
    12	min()	    Calculates the minimum of all the elements of the List
    13	max()	    Calculates the maximum of all the elements of the List
"""
#list declaration
nums=[]
print("enter size:")
n=input()
flag=0

# dynamic initialization of list
print( )
for i in range(0,int(n)-1):
    print("val:")
    temp=input()
    nums.append(temp)

# print list
print( )
print("Org list:")
for i in range(0,int(n)-1):
    print(nums[i])
    
# logic to check if duplicates exist
for i in range(0,int(n)-1):
    for j in range(i+1,int(n)-1):
        # is operator  - True if the operands are identical
        if(nums[i] is nums[j]):
            flag=1
            
print( )
if(flag==1):
    print("Duplicates!")
else:
    print("All Unique!")  
