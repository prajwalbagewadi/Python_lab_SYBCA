"""
Write a program which prints Fibonacci series of a number.
"""

"""
Fibonacci series :
0   1   1   2   3   5  8 .. n
0 + 1 = 1
    1 + 1 = 2
        1 + 2 = 3
            2 + 3 = 5
                3 + 5 = 8   
"""
print("Fibonacci Series:")
print("enter the num to find:")
n=input()
num1=0
num2=1

print( )
for i in range(1,int(n)+1):
    temp=num1+num2
    if(temp>=int(n)):
        break
    else:
        print(num1,"+",num2,"=",temp)
        num1=num2
        num2=temp
