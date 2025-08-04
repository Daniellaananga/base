# the computer should imagine a number
Guess_number = int(input("Guess a number between 1 and 50: "))
# lets give the computer a number the user should give, else the user is wrong
if Guess_number < 33:
    print("You are below")
elif Guess_number > 33:
    print("You are above")
else:
    print("GREAT YOU GOT IT")