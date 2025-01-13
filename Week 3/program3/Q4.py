'''
Modify your program again so that the chosen password cannot be one of a list of 
common passwords, defined thus: 
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] 
'''

password= input("Enter your password (the password must be between 8 and 12 characters): ")
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbibe'] 

if 8 <= len(password) and len(password) <= 12:
    if password in BAD_PASSWORDS:
        print("Password is not valid")
    else:
        password2=input("Enter password again:")
        if password==password2:
            print("Password accepted")
        else:
            print("Passwords don't match")
else:
    print("Password must be between 8 and 12 characters")  