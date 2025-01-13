
'''''1.Functions are often used to validate input. Write a function that accepts a single 
integer as a parameter and returns True if the integer is in the 
range 0 to 100 (inclusive), or False otherwise. 
Write a short program to test the function.'''

def input(number):
	return number in range(0,100)

def input_test():
	values =[12,79,-66,0,564]
	for value in values:
		result=input(value)
		print(f"input {value} is validation: {result}")

input_test()