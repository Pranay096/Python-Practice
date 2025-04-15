a = (input("Enter any value between 5 to 9: "))
b= "quit"
if a == b:
    print("Exiting the program.")
elif int(a) < 5 or int(a) > 9:
    raise ValueError("The value must be between 1 and 9.")
else:
    print("You entered:", a)