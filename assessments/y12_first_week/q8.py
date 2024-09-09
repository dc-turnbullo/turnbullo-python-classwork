def change(char):
    if char == "0":
        return "zero"
    elif char == "1":
        return "one"
    elif char == "2":
        return "two"
    elif char == "3":
        return "three"
    elif char == "4":
        return "four"
    elif char == "5":
        return "five"
    elif char == "6":
        return "six" 
    elif char == "7":
        return "seven"
    elif char == "8":
        return "eight"
    elif char == "9":
        return "nine"
    else:
        return char 

string = input("Enter a string: ")
new_string = ""  

for char in string:
    new_string += change(char)

print(new_string)