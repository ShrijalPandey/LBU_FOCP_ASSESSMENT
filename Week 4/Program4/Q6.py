'''
Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.'''
def value(celsius):
    fahrenheit=celsius*(9/5)+32
    return fahrenheit
temperature=input("Enter a temp in C:")

if temperature[-1].upper()=='C':
    print(f"{value(float(temperature[:-1]))}F")
else:
    print("Invalid")