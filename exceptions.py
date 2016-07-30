# exceptions = manage errors that arise
# instead of tracebacks, users will see friendly error messages

# if code inside a try block works, Python skips over the except block
# if code inside a try block fails, Python looks for an except block whose error
# matches the one that was raised and runs the code in that block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    # additional code that should run only if the try block was successful
    else:
        print(answer)
