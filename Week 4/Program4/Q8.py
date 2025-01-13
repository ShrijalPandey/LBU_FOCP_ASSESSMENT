'''
Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value.'''

import statistics
def read_temperatures():
    temperatures=[]
    while True:
        user_input = input ("Enter a temperature (or press Enter to finish): ")
        if user_input =="":
            break
        try:
            temp = float(user_input)
            temperatures. append (temp)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return temperatures

def main():
    temperatures = read_temperatures()
    max_temp = max (temperatures)
    min_temp = min (temperatures)
    mean_temp = statistics.mean (temperatures)
    print(f"Minimum temperature: {min_temp:.2f}")
    print(f"Maximum temperature: {max_temp:.2f}")
    print(f"Mean temperature: {mean_temp: .2f}")

if __name__ == "__main__":
    main()