import random

# List of possible numbers
numbers = [-1, 0, 1]

# Choose a random number from the list
random_choice = random.choice(numbers)

# make the coice of computer
computer = random_choice

"""
1 for snake
-1 for water 
0 for gun
"""

# taking the choice from user
youstr = input("Enter your choice: ")

# making two same data but opposite value dictionary
youDict = {"snake": 1, "water" : -1, "gun" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "gun"}

# taking the value of youstr in you from you dict
you = youDict[youstr]
 
# printing the values of you and computer
print(f"you choose {reverseDict[you]}\n computer choice is {reverseDict[computer]}")

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


print("Game is completed ✅ Run again the code to play again")
print("Thanks to play our game 🎮")