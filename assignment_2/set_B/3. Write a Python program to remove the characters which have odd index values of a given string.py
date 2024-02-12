"""
3. Write a Python program to remove the characters which have odd index values of a given string.
"""

#input string
str_v=input("enter string:")

#find odd index characters
"""
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
"""
def remove_odd_index(str_in):
  even_str=""
  odd_str=""
  for i in range(0,len(str_in)):
    if i%2==0:
      print("even=",i,"=",str_in[i])
      """
      list1 = {'1', '2', '3', '4', '4'} 
      # put any character to join
      s = "-#-"
      # joins elements of list1 by '-#-'
      # and stores in string s
      s = s.join(list1)
 
      # join use to join a list of
      # strings to a separator s
      print(s)
      """
      """ 
      join() method:The join() method takes all items in an iterable and joins 
      them into one string.
      A string must be specified as the separator.
      The join() method in Python is used to concatenate a sequence 
      (e.g., a list, tuple, or string) of elements into a single string. 
      It returns a string where elements of the sequence are joined together using 
      the specified delimiter.
      """
      even_str+=even_str.join(str_in[i])
    else:
      print("odd=",i,"=",str_in[i])
      odd_str+=odd_str.join(str_in[i])
      
  return odd_str,even_str  


out_result=remove_odd_index(str_v)
print("even indexed string=",out_result[0])
print("odd indexed string=",out_result[1])
