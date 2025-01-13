'''
Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.

'''
def get_unique_sorted_letters(input_string):

    letters_only = [char.lower() for char in input_string if char.isalpha()]
    
    unique_sorted_letters = sorted(set(letters_only))
    
    return unique_sorted_letters

def letters_in_either(word1, word2):

    return sorted(set(word1.lower()) | set(word2.lower()))

def letters_in_both(word1, word2):

    return sorted(set(word1.lower()) & set(word2.lower()))

def letters_in_either_but_not_both(word1, word2):

    return sorted(set(word1.lower()) ^ set(word2.lower()))

if __name__ == "__main__":

    print(letters_in_either("apple", "pear"))          # Expected output: ['a', 'e', 'l', 'p', 'r']
    print(letters_in_both("apple", "pear"))            # Expected output: ['a', 'p']
    print(letters_in_either_but_not_both("apple", "pear"))  # Expected output: ['e', 'l', 'r']
