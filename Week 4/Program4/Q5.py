'''
Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).'''

def temperature(celsius):
	fahrenheit=celsius*(9/5)+32
	return fahrenheit

def temp(fahrenheit):
	celsius=(fahrenheit-32)*(5/9)
	return celsius

c_to_f=(temperature(100))
f_to_c=(temp(100))
print(f'{c_to_f:.2f}')
print(f'{f_to_c:.2f}')
