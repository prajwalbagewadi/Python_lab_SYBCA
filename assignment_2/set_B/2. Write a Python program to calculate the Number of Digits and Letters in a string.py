"""
Write a Python program to calculate the Number of Digits and Letters in a string.
"""
#calculate = finc the total 

#input a string 
str_v=input("enter the string:")
print("orginal_str=",str_v)

#calculate digits
def find_digits(str_v):
    count=0
    for char in str_v:
        """
        isdigit():Returns true if string contains only digits and false otherwise.
        we use it with str.object
        """
        if(char.isdigit()):
            count+=1
    
    return count

#calculate alphabets
def find_alpha(str_v):
    count=0
    for char in str_v:
        """
        isalpha():Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
        we use it with str.object
        """
        if(char.isalpha()):
            count+=1
    
    return count

#function call
digit_count=find_digits(str_v)
print("total digits in string=",digit_count)

#function call
alpha_count=find_alpha(str_v)
print("total alphabets in string=",alpha_count)
