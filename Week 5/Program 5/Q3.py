'''
Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them.'''

import sys
from sys import argv

list=argv[1:]
list.sort(key=len)
print(list)
try:
    print(f"the shortest word is :{list[0]}")
except:
    print("Word not passed")