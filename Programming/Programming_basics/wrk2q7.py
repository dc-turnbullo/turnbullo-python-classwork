print("Answer all questions with a lowercase y or n standing for yes or no.")
if str(input("do you have a temperature")) == "y":
    if str(input("Do you have a sore throat")) == "y":
        print("you may have a throat infection.")
    elif (str(input())) == "n":
        if str(input("do you have a cough")) == "y":
            print("you may have a chest infection")
        else:
            print("you may have a fever")
else:
    print("you are fine")