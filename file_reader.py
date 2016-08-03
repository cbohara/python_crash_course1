filename = 'text_files/pi_to_million.txt'

with open(filename) as file_object:
    # readlines() method takes each line from the file and stores it in a list
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in pi!")
else:
    print("Whomp womp")
