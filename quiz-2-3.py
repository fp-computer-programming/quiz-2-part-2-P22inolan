# Author: IBN (ADMG) 11/17/2021
import random
entry = input("What are your 3 numbers? (1-50) ")
entry_lst = entry.split()
choice1 = str(random.randint(1, 50))
choice2 = str(random.randint(1, 50))
choice3 = str(random.randint(1, 50))

print("The lucky numbers are: " + choice1 + ', ' + choice2 + ', ' + choice3)

if entry_lst[0] == choice1 and entry_lst[1] == choice2 and entry_lst[2] == choice3:
    print("You win!")
elif entry_lst[0] == choice1 and entry_lst[1] == choice2:
    print("You got two numbers!")
elif entry_lst[0] == choice1 and entry_lst[2] == choice3:
    print("You got two numbers!")
elif entry_lst[1] == choice2 and entry_lst[2] == choice3:
    print("You got two numbers!")
elif entry_lst[0] == choice1:
    print("You got one number!")
elif entry_lst[1] == choice2:
    print("You got one number!")
elif entry_lst[2] == choice3:
    print("You got one number!")
else:
    print("You got none of the numbers.")
