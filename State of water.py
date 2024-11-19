# States of water program

# -------------------------
# Subprograms
# -------------------------
def water_state(temperature):
  if temperature >= 100:
    state = "gas"  
    return state
    
  elif temperature < 100 and temperature > 0:
    state = "liquid"
    return state
    
  else:
    state = "solid"
    return state
  
    


# -------------------------
# Main program
# -------------------------
temperature = int(input("Enter the temperature in centigrade: "))
state = water_state(temperature)
print("The water is in a", state, "state.")
