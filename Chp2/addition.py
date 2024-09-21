print("This is additon program \n when you enter any number it do subTotal")
print("press '0' for exit \n")
total=0
def addition(total):
    num=1
    while(num!=0):
        num = float(input("Enter Number"))
        total+=num
        print(total)
    print("you have been ternminated program\n")
try:
    addition(total)
except ValueError:
    print("You can add only integer and decimal point number")
