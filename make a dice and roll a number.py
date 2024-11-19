# Polyhedral dice program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def roll_dice(face):
    return random.randint(1, face)


# -------------------------
# Main program
# -------------------------

face = int (input("Enter the amount of face in the dice"))

random.seed()
number = roll_dice(face)
print("You rolled a", number)
