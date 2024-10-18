# Nitrate program

# -------------------------
# Subprograms
# -------------------------
def calculate_dose(nitrate):
  carbon_dose = 0
  if nitrate >= 10 :
    carbon_dose = 3
  elif  nitrate >= 2.5:
    carbon_dose = 2
  elif nitrate >= 1:
    carbon_dose= 1
  elif nitrate < 1:
    carbon_dose = 0.5
  else:
    print("invalue")
  return carbon_dose


# -------------------------
# Main program
# -------------------------
nitrate = float(input("Enter the nitrate level from the exam: "))
carbon_dose= calculate_dose(nitrate)
print("For", nitrate, "nitrate dose", carbon_dose, "ml of carbon.")
