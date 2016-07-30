filename = 'text_files/magic_of_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'Unicorns')
    print(line.strip())
