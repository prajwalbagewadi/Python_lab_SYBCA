"""
1. Write a program to replace all occurrences of ‘a’ with $ in a String. (Ex. apple then output is
$pple).
"""

#string input
str_i="apple"
#original string
print("org_str="+str_i)
"""
string.replace:(method)
The replace string method returns a new string with some characters
from the original string replaced with new ones.
The original string is not affected or modified.

Syntax:
string.replace(old_char, new_char, count)
"""
#new string var to store the result string 
new_str=str_i.replace("a","$");
#print new string
print("new_str="+new_str)
