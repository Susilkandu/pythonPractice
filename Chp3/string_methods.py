letter = "   Dear Harry , this {} course is {}. Thanks! "
print(f"{letter.upper() }\n")
print(f"{letter.lower() }\n")
print(f"{letter.strip() }\n")
print(f"{letter.split() }\n")
print(f"{letter.join(['Hello','sister'])} \n")
print(f"{letter.find('H')}\n")
print(f"{len(letter)}\n")
print(f"{letter.startswith('s')}\n")
print(f"{letter.endswith('h') }\n")
print(f"{letter.format('Python','hrry')}\n")

price = 34.5434

print("${:.3f}".format(price))   #it shows only only 3 value after decimal

greeting = "Good"
print("{:.3s}".format(greeting))
print("Text:{:>10}".format('Morning')) #it add in right side after 10 to the 'Morning'
print("Text:{:<10}".format('Morning')) #it add in left side before 10 to the 'Morning'
