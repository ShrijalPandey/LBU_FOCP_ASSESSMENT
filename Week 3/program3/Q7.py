'''
Modify your "Times Table" program so that the user enters the number of the table they require.
This number should be between 0 and 12 inclusive. 
'''
number=int(input("Enter a number:"))
for i in range(13):
    print(f"{i} x {number}={i*number}")