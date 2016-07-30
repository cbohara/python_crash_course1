"""
open() function requires 1 argument - the name of the file to be opened
looks for this file in the directory where the program that is currently being
executed is stored

if the file is not in the same directory, the file path needs to be specified

keyword 'with' closes the files once access to it is no longer needed
"""
with open('text_files/pi_digits.txt') as file_object:
    # read() methods reads the entire contents of the file and stores it as one
    # long string in contents variable
    contents = file_object.read()
    print(contents.strip())

###############################################################################
# alternative approach - store file name into a variable
file1 = 'text_files/pi_digits.txt'

# execute for loop that prints each line of the text_file
with open(file1) as file_object:
    for line in file_object:
        print(line.rstrip())

################################################################################
"""
when you use 'with', the file object returned by open() is only available
inside the with block that contains it
to retain access outside the 'with' block, store the file's lines in a list inside
the block and then work with that list
"""

file2 = 'text_files/pi_to_million.txt'

with open(file2) as file_object:
    # readlines() method takes each line from the file and stores it in a list
    # list is stored in lines variable
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print first 50 decimal places
# print(pi_string[:52] + "...")
# print(len(pi_string))

# is my birthday contained in the number pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
# search for birthday string in first million digits of pi
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
