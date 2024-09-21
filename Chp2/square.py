# Write a program to check square of the given number by the user
import logging
try:
    print("This program is square checker of any number \n")
    print("**Note*** Press 0 for terminat the program")
    while(1):
        num = float (input("Enter any number \t"))
        if(num==0):
            print("You have been terminated the program Successfully !")
            exit()
        print(f"{num}*{num} = {num**2} \n")
except Exception as error:
    logging.error(f"Error Occured: {error}")