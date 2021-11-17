# Author: IBN (AMDG) 11/17/2021
letter = input("Give me your letter day. (A-G) ")
letter = letter.lower()

if letter == 'a':
    print("You have class today because it is A day.")
elif letter == 'c':
    print("You have class today because it is C day.")
elif letter == 'e':
    print("You have class today because it is E day.")
else:
    print("You do not have class today.")
