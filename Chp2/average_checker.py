# Write a Python program to check average of two number entered by the user
import logging
try:
    print("this program is average checker of any two number \n")
    print("***Note Press 0 for exit the program \n")
    while(1):
        x = int(input("Enter first Number"))
        if(x==0):
            print("You have been exited from progran")
            exit()
        y = int(input("Enter second Number"))
        print(f"average of {x} and {y} is {(x+y)/2}")
except Exception as e:
    logging.error(f"Error:{e}")
