# lets ask the user to enter a number 
num=input("Enter number : ")
# now the computer will determine the date corresponding to the number the user will enter
if num == 1:
    pirnt("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Sarturday")
elif num == 7:
    print("Sunday")
    # if there is a number else than this 1-7,
else:
    print("No Date Found On This Number")