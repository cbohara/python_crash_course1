filename = 'text_files/programming.txt'

# open() now has 2 arguments - name of the file we want to open AND
# 'w' which tells Python we want to open the file in write mode
# no second argument? defaults to 'r' (read only mode)
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")

# append 'a' mode = add content to a file instead of writing over existing content
with open(filename, 'a') as file_object:
    file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
