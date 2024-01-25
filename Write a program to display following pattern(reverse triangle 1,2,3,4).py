# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
"""
Write a program to display following pattern.
1 2 3 4
1 2 3
1 2
1
"""
def disp_pattern():
    for row in reversed(range(1,4+1)):
        var=int(row)
        #print("row_num=",var,end="\n")
        #print(row,end="\n")
        temp=1
        for col in range(1,var+1):
            #print(col,end="\n")
            print(temp,end="\t")
            temp=temp+1
        print(end="\n")     

disp_pattern()            
            
