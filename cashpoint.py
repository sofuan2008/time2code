# Cashpoint program

# -------------------------
# Subprograms
# -------------------------
def dispense(amount):
  amount = amount
  print("W" , amount)
  while amount >=20:
    amount = amount - 20
    print("D 20" )
    
  
  while amount >=10:
    amount = amount - 10
    print("D 10")
    
    
  while amount >=5:
    amount = amount - 5
    print ("D 5")

# -------------------------
# Main program
# -------------------------
amount = int(input("Enter amount you want to dispense: "))
cashpoint = dispense(amount)
