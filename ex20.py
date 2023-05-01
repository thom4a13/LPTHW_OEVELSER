from sys import argv 
# Import the argv module from the sys package

script, input_file = argv
# Assign the script name and the input file name to argv

def print_all(f):
    print(f.read())
# Define a function named print_all that takes a file object as an argument and prints the whole file

def rewind(f):
    f.seek(0)
# Define a function named rewind that takes a file object as an argument and sets the current position to the beginning of the file

def print_a_line(line_count, f):
    print(line_count, f.readline())
# Define a function named print_a_line that takes a line number and a file object as arguments and prints the line number and the line of the file

current_file = open(input_file)
# Open the input file and assign the file object to current_file

print("First let's print the whole file:\n")

print_all(current_file)
# Print the whole file

print("Now let's rewind, kind of like a tape.")

rewind(current_file)
# Set the current position to the beginning of the file

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
# Print the first line of the file

current_line = current_line + 1
print_a_line(current_line, current_file)
# Print the second line of the file. Adds 1 to the number

current_line = current_line + 1
print_a_line(current_line, current_file)
# Print the third line of the file Adds 1 to the number