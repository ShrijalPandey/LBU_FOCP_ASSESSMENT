'''
One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the dierent symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes.

'''

def analyze_frequency(message):
    message = message.lower()  # Convert to lowercase
    counts = {char: message.count(char) for char in 'abcdefghijklmnopqrstuvwxyz'}  # Count letters
    most_common = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:6]  # Sort and take top 6
    for letter, count in most_common:
        print(f"{letter}: {count}")

message = "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
analyze_frequency(message)
