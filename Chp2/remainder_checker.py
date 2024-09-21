# Write a python program to check remainder of a number when divided by x
try:
    print("This is remainder checker program")
    print("\press 0 to exit from progrm")
    while(1):
        num = int(input("Enter the number"))
        if(num==0):
            print("You have been exited from program")
            exit()
        x = int(input("Enter the Value of x \t"))
        print(f"{num}%{x} = {num%x}")

except ValueError:
    print("number and x value must be only inter type")    