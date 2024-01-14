"""
Write a program which finds sum of digits of a number.
Example n=130 then output is 4 (1+3+0).
"""
print("Enter int val:")
#type cast input to string
var=str(input())
ans=0

for i in var:
    # type cast char to int
    ans+=int(i)

print("result=",ans)    
