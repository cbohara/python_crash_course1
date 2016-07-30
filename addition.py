def addition():
    """Add 2 numbers and check for exceptions"""
    num1 = input("Number 1: ")
    num1 = int(num1)
    num2 = input("Number 2: ")
    num2 = int(num2)
    try:
        answer = num1 + num2
        with open('text_files/addition.txt', 'w') as file_object:
            file_object.write(answer)
    except TypeError:
        print("You attempted to print ints instead of a string answer!")

addition()
