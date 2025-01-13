"""
Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].

"""

def get_unique_sorted_letters(input_string):
    letters_only = [char.lower() for char in input_string if char.isalpha()]
    
    unique_sorted_letters = sorted(set(letters_only))
    
    return unique_sorted_letters

if __name__ == "__main__":
    test_string = "cheese"
    print(get_unique_sorted_letters(test_string))  

    print(get_unique_sorted_letters("Hello World!"))  
    print(get_unique_sorted_letters("123ABCabc"))      
    print(get_unique_sorted_letters("Python."))       
