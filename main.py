import random
import time 

# List of possible numbers
numbers = [-1, 0, 1]

# Choose a random number from the list
random_choice = random.choice(numbers)

# make the coice of computer
computer = random_choice

"""
1 for Snake
-1 for Water 
0 for Gun
"""

# taking the choice from user
youstr = input("Enter your choice: ")

# making two same data but opposite value dictionary
youDict = {"Snake": 1, "Water" : -1, "Gun" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

# taking the value of youstr in you from you dict
you = youDict[youstr]
 
# printing the values of you and computer
print(f"you choose {reverseDict[you]}\n computer choice is {reverseDict[computer]}")
time.sleep(0.5)
print("Calculating result...")
time.sleep(0.5)
time.sleep(0.5)

# according to the condition we can choose the winner and draw or lose of game 
if (computer == you ):
    print("it's a draw")
else:
    if (computer == -1 and you == 1):
        print("You win ")

    elif (computer == -1 and you == 0):
        print("you lose")

    elif (computer == 1 and you == -1 ):
        print("you lose")

    elif (computer == 1 and you == 0 ):
        print("you win")

    elif (computer == 0 and you == 1 ):
        print("you lose")

    elif (computer == 0 and you == -1 ):
        print("you win")

    else: 
        print("Something went worng")

time.sleep(0.5)
time.sleep(0.5)


print("========================= Game is completed ✅. Run again the code to play again =========================")
print("=================================== Thanks to play our game 🎮 ======================================")

# Write feedback in a file 
class Feedback:
    name = input("Enter your name please: ")
    feedback = input("Give your feedback please: ")

time.sleep(0.5)
print("Saving your feedback...")
time.sleep(0.5)
time.sleep(0.5)
print("Feedback saved successfully. Thank you!")

f = open(f"Snake-Water-Gun_Game-Python-/Feedback/{Feedback.name}_feedback.txt", "w")
f.write(f"Name: {Feedback.name}\nFeedback: {Feedback.feedback}")
f.write(f"Choices: You chose {reverseDict[you]}, Computer chose {reverseDict[computer]}\n")
f.close()
