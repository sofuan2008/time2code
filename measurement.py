# Measurements program

# -------------------------
# Subprograms
# -------------------------
def menu():
  while True:
    print(" 1. Feet to inches \n 2. Inches to feet \n 3. Quit")
    choise = int(input("Enter choise: "))
    if choise == 1 :
      feet = float(input("Enter number of feet: "))
      print (feet,"feet is ", feet_to_inches(feet),"inches")
    elif choise == 2 :
      inches = float(input("Enter number of inches: "))
      print (inches,"inches is ", inches_to_feet(inches),"feet")
    else:
      print("Goodbye")
      quit()

def feet_to_inches(feet):
  inches = feet * 12
  return inches

def inches_to_feet(inches):
  feet = inches / 12
  return feet
# -------------------------
# Main program
# -------------------------
program = menu()
