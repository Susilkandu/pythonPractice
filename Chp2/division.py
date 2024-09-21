# Write a Python program to do division untill user not press 0
num=1
div=1
print("This Program is for division")
print("\n press 0 for stor the program")
while(1):
    num = float(input("Enter the divident number \t"))
    if(num==0):
        print("you have been terminated Program \n")
        exit()
    div = float(input("Enter divisor \t"))
    result= num/div
    print(f"{num}/{div} = {result}")