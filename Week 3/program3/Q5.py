BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password = input("Enter your password (the password must be between 8 and 12 characters): ")
    
    if 8 <= len(password) <= 12:
        if password not in BAD_PASSWORDS:
            password2 = input("Enter password again: ")
            if password == password2:
                print("Password accepted")
                break
            else:
                print("Passwords don't match. Please try again.")
        else:
            print("Password is not accepted because it's too common. Please try again.")
    else:
        print("Password must be between 8 and 12 characters. Please try again.")
