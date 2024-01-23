"""
Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’.
"""
"""
Prime numbers are natural numbers that are divisible by only 1 and the number itself. 
In other words, prime numbers are positive integers greater than 1 with exactly two factors, 
1 and the number itself. 

The prime numbers from 1 to 100 are: 
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
31, 37, 41, 43, 47, 53, 59, 61, 67, 
71, 73, 79, 83, 89, 97.
"""
list=[];
print("enter the size/range_end:")
size=input()

def prime_num(n):
    # logic from gfg
    if(n==0 or n==1):
        return n,False
    else:
        #for i in range(1,n+1):
            if(n%1==0 and n%n==0):
                if(n==2):
                    return n,True
                for i in range(2,n+1):
                    if(n%i==0):
                        return n,False
                        break
                    if(i==n-1):
                        return n,True
                        break
                   
print(end="\n")
for n in range(int(size)):
    # calling a function in if statement
    var=prime_num(n)
    print(var,end=" ")

    if(prime_num(n)[1]==True):
        list.append(n)
            
print(end="\n")       
print("list:",end="\n")    
for j in range(0,len(list)):
    print(list[j],end=" ")
#output
"""
There are 8 prime numbers under 20: 2, 3, 5, 7, 11, 13, 17 and 19
hp@hp-Presario-CQ58-Notebook-PC:~/python_programs$ /bin/python3 /home/hp/python_programs/chap1_setB_Q1.py
enter the size/range_end:
10

(0, False) (1, False) (2, True) (3, True) (4, False) (5, True) (6, False) (7, True) (8, False) (9, False) 
list:
2 3 5 7 
"""    
# testing of logic
"""
i=2
n=9
//n=2
for i in range(2,int(n)+1):
    if(n%i==0):
        print("if",i)
    else:
        print("else",i)

output:
else 2
if 3
else 4
else 5
else 6
else 7
else 8
"""
#logic testing for 7
"""
n=7
if(n%1==0 and n%n==0):
    print("n%1",n%1,"n%n",n%n)
    if(n==2):
        print("its 2") 
    for i in range(2,n):
        if(n%i==0):
            print("false:",i,"n%i",n%i)
            break;    
                #return False
            #   else :
            #     return True
        else:
            print("True:",i,"n%i",n%i) 
            break;
            #return True
output:
n%1 0 n%n 0
True: 2 n%i 1
"""
# logic test for 9 updated with test issue for 9 from previous logic 
"""
n=9
if(n%1==0 and n%n==0):
    print("n%1",n%1,"n%n",n%n)
    if(n==2):
        print("its 2") 
    for i in range(2,n+1):
        if(n%i==0):
            print("false:",i,"n%i",n%i)
            break    
                #return False
            #   else :
            #     return True
        if(i==n-1):
            print("True:",i,"n%i",n%i) 
            break
            #return True
output:
n%1 0 n%n 0
false: 3 n%i 0            
"""
# logic test for 7 updated with test issue for 9 from previous logic 
"""
n=7
if(n%1==0 and n%n==0):
    print("n%1",n%1,"n%n",n%n)
    if(n==2):
        print("its 2") 
    for i in range(2,n+1):
        if(n%i==0):
            print("false:",i,"n%i",n%i)
            break    
                #return False
            #   else :
            #     return True
        if(i==n-1):
            print("True:",i,"n%i",n%i) 
            break
            #return True
output: 
hp@hp-Presario-CQ58-Notebook-PC:~/python_programs$ /bin/python3 /home/hp/python_programs/codetest.py
n%1 0 n%n 0
True: 6 n%i 1           
"""
