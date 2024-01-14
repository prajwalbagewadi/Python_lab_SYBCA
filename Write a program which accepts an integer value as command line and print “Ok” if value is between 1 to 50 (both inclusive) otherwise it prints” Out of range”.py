"""
Write a program which accepts an integer value as command line and print “Ok” if value is
between 1 to 50 (both inclusive) otherwise it prints” Out of range”
"""
"""
sys. argv is a list in Python that contains all the command-line arguments passed to the script. 
It is essential in Python while working with Command Line arguments. 
"""
import sys
n=len(sys.argv)
for i in range(1,n):
    print( )
    print(sys.argv[i])
    print( )
    var=int(sys.argv[i])
    if(var in range(1,50)):
        print("ok.")
    else:
        print("Out of range.")
