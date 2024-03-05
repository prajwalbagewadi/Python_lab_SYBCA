"""
1. Write a Python program to accept the strings which contains all vowels
"""
Str1=input("enter str one")
Str2=input("enter str two")
Str3=input("enter str three")
ilist=[Str1,Str2,Str3]
print(f"ilist={ilist} type={type(ilist)}")
vovels={'a','e','i','o','u'}
print(f"vovels={vovels} type={type(vovels)}")
def check_vovels(myset):
    for char in myset:
        if(char in vovels):
            continue
        else:
            print(f"{char} not vovel")
            return False
            break
    return True
#create a set in loop for ilist so each string can be checked for vovels
for String in ilist:
    #use set() method to seperate out chars in string and store it in the set
    myset1=set(String)
    print(f"myset1={myset1} type={type(myset1)}")
    var=check_vovels(myset1)
    print(f"myset1={myset1} type={type(myset1)} contains all vovels={var}")
