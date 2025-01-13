'''
. Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by
multiplying two other integers.
'''

n=int(input("Enter a number: "))
if n==1:
    print("1 is not a prime number")
if n>1:
    for i in range(2,n):
        if n % i==0:
            print(n,"is not a prime number.")
            break
        else:
            print(n,"is a prime number.")
            break