value = float(input("enter the value of your order: "))
if value > 15:
    if input("do you want to pay £5 extra for next day delivery y/n") == "y":
        value = value + 5
else:
    value = value + 3.5
    if input("if you want to pay £5 for next day delivery press 1 otherwise press 2 for normal £3.50 delivery") == "1":
        value = value + 1.5

print("the final cost is £", value)