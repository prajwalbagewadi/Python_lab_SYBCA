"""
2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String: google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

#input string
istr="google.com"

 
#logic to find char freq in string
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*,
changeable and do not allow duplicates.
"""

#create a dictionary
freq={}

#add key and val in dictionary count=0 as val
cnt=0;
for char in istr:
    freq[char]=int(cnt)
    
#print the dictionary
print("inital_str:",end="\n")
print(freq)

#extract keys from the dict into a seperate list

freq_keys=freq.keys();
print("keys extracted:",end="\n")
print(freq_keys)

#compare keys from extracted list with orginal str
# is exist increment the count by one
for key in freq_keys:
    for char in istr:
        if key == char:
            freq[char]+=1
        
#print the result dictionary with frequencies
print("Frequency of each char in str:",end="\n")            
print(freq)
