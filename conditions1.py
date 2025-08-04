# lets ask the user to enter his mark
a= int(input("Eneter score : "))
# lets test and see if the nark is 
if a >= 16:
    print("Excellent!")
elif a >= 12:
    print("Good!")
elif a >= 10:
    print("Passed!")
else:
    print("Insufficient!")