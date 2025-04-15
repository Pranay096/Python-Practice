email = input("Enter your email: ")
correct_password = "tanvitupe096"

while True:
    password = input("Enter  your password: ")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("incorrect password. Please try again")