filename = "text_files/guest.txt"

with open(filename, 'w') as file_object:
    user = ''
    while user != 'quit':
        user = input("What is your name? ")
        file_object.write(user + "\n")
