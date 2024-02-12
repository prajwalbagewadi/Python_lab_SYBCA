"""
1. Remove special symbols/Punctuation from a given string.
"""
"""
Given:
str1 = "/*Sachin is @Cricketer& kind person"
Expected Output:
“Sachin is Cricketerkind person”
"""

#input string
str_i="/*Sachin is @Cricketer& kind person"
print("raw str=",str_i)

#import for symbols/Punctuation
import string
punc_symbols=string.punctuation
print("symbols/Punctuation=",punc_symbols)
print("symbols/punctuation type=",type(punc_symbols))

#logic to search and replace
def remove_punctuation(str_in,punc_symbols):
    str_out=""
    for char in str_in:
        #to compare a single char to a collection of characters(str) at once use (in) operator
        if char in punc_symbols:
            print("char to remove=",char)
            str_out+=''
            print("str_out=",str_out)
        else:
            str_out+=char
            print("str_out=",str_out)

    return str_out
            

#function call
str_res=remove_punctuation(str_i,punc_symbols)
print("clean str=",str_res)
