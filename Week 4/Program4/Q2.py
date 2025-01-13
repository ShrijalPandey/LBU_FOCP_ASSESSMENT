'''Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.'''

def prog(word):
    
    uppercase = 0
    lowercase = 0
    for char in word:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
    return uppercase, lowercase

word = 'Merry Christmas and a Happy New Year'
uppercase_count, lowercase_count = prog(word)

print(f'UPPERCASE LETTERS: {uppercase_count}')
print(f'lowercase letters: {lowercase_count}')


