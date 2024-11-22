# PIN program

# -------------------------
# Subprograms
# -------------------------
def get_pin():
  for x in range (1,4):
    pin = int(input("Enter pin :"))
    if pin == 7528:
      print ("Security check passed")
      exit()
      
  print("Locked out")

# -------------------------
# Main program
# -------------------------
get_pin()
