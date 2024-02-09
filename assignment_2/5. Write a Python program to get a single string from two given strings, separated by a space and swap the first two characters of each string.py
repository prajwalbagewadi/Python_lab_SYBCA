"""
5. Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.
Sample String: 'ppk', 'abc’
Expected Result: 'abkppc’
"""
#string declaration
str_var=input("Enter the string with space:")
print(str_var)

#split the string
new_str=str_var.split(" ")
print(new_str)

#swap logic
def swapper(a_str,b_str):
    """
    The String replace() method replaces a character with a new character. 
    You can remove a character from a string by providing the character(s) 
    to replace as the first argument and an empty string as the second argument.
    eg :
    s = 'ab\ncd\nef'
    print(s.replace('\n', ''))
    Output:
        abcdef
    """
    res1=b_str.replace(b_str[:2],a_str[:2])
    res2=a_str.replace(a_str[:2],b_str[:2])
    print(res2+res1)

#function call
swapper(new_str[0],new_str[1])
