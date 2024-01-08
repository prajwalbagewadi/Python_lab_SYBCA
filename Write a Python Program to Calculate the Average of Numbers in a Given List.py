"""
Q)Write a Python Program to Calculate the Average of Numbers in a Given List. 
"""
"""
print('enter the msg');
msg=input();
print(msg)
"""
# list declaration
list=[]

# list initilization using while loop
i=0
while(i<5):
    print("enter item:")
    temp=input()
    list.append(temp)
    i=i+1

#list printing using while loop
print("\n")
i=0
while(i<5):
    print("item",list[i])
    i=i+1;

#list average using for loop
total=0
n=5
for i in range(0,n): 
    """
    Explicit Type Conversion in Python :
        In this method, Python needs user involvement to convert the variable data type into the required data type. 
    Mainly type casting can be done with these data type functions:
        Int(): Python Int() function take float or string as an argument and returns int type object.
        float(): Python float() function take int or string as an argument and return float type object.
        str(): Python str() function takes float or int as an argument and returns string type object.

    """    
    total+=int(list[i])
#example of implicit type conversion or type casting
avg=total/len(list)
print("average of list=",avg)
