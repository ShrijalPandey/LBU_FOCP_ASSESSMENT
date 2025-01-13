'''
Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a dierent name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy liing here! Take a look at the "Brief Tour of the Standard Library" in the docs.'''
from shutil import copyfile
from sys import argv
import os

try:
    origin_filename = argv[1]

    filename, extension = os.path.splitext(origin_filename)

    target_filename = f"{filename}_backup{extension}"

    copyfile(origin_filename, target_filename)
    print(f"File copied successfully to {target_filename}")

except IndexError:
    print("Error: No file name provided. Please provide the file name as a command-line argument.")
except FileNotFoundError:
    print(f"Error: The file '{origin_filename}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
