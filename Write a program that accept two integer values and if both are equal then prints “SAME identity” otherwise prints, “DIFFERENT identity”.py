"""
Write a program that accept two integer values and if both are equal then prints “SAME identity” otherwise prints, “DIFFERENT identity”.
"""
print("enter two Integer numbers to Check identity",end="\n")
print("enter First int:")
int1=int(input())
print("enter Second int:")
int2=int(input())
"""
is and is not are the identity operators both are used to check if two values are located on the
same part of the memory. Two variables that are equal does not imply that they are identical.
is - True if the operands are identical
is not - True if the operands are not identical
"""
#if(int1 is int2):
if(int1 == int2):
    print("SAME identity",int1,"==",int2)
else :
    print("DIFFERENT identity",int1,"==",int2) 
