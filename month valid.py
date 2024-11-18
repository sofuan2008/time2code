# Valid month program

# -------------------------
# Subprograms
# -------------------------
def validate_month(month):
  validate_month = False
  while validate_month == False:
    if month >= 1 and month <=12:
      validate_month = True
      return True
    else:
      month = int(input("Enter month 1-12: "))
      


# -------------------------
# Main program
# -------------------------
month = int(input("Enter month 1-12: "))
valid_month = validate_month(month)
print("Thank you. Input accepted.")
