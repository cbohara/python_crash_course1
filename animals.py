with open('text_files/animals.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('cats','dogs')
    print(line)
