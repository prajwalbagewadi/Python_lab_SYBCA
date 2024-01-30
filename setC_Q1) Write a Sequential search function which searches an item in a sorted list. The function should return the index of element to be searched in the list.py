"""
setC_Q1) Write a Sequential search function which searches an item in a sorted list. The function
should return the index of element to be searched in the list.
"""
"""
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
"""
#create a tuple
print("Sequential Search:",end="\n")
Tuple=(5,4,3,2,1)
print("original tuple:",Tuple,end="\n")
#sort the tuple 
srt_tuple=tuple(sorted(Tuple))
print("sorted tuple:",srt_tuple,end="\n")

def seq_search(Tup,key):
    for i,val in enumerate(Tup):
        """
        Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop.
        This enumerate object contains a count (from the start, which always defaults to 0) and a value obtained from iterating over the iterable object.
        """
        print("i=",i,"val=",val)
        if val==key :
            return i

        

# search function
print("Enter the Element to Search:")
key=input()
val=seq_search(srt_tuple,int(key))
#print("element of tuple  not found") index = None
print("element of tuple found at index:",val)
