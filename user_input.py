# input() function pauses your program and waits for the user to enter text
# saves user input into a variable as a string

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name.title() + "!")

# build prompt over several lines
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

#name = input(prompt)
# print("Hello, " + name.title())

# use input() to prompt user
#age = input("How old are you? ")
# convert answer from string to int
#age = int(age)
#print("You are " + str(age) + " years old.")

answer = input("Give me a number: ")
answer = int(answer)
if answer % 10 == 0:
    print(str(answer) + " is divisible by ten!")
else:
    print(str(answer) + " is not divisible by ten.")
