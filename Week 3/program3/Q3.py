'''
3. Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long. 
'''

password= input("Enter your password (the password must be between 8 and 12 characters): ")

if 8 <= len(password) and len(password) <= 12:
    password2=input("Enter password again:")
    if password==password2:
        print("Password accepted")
    else:
        print("Passwords don't match")
else:
    print("Password must be between 8 and 12 characters")  