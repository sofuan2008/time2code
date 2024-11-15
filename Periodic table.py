def details (element):
  if element == "Li" or element == "Lithium":
    print("Lithium (Li) \n Atomic Weight = 6.94 \n Group (Alkali Metal)")
  elif element =="Na" or element == "Sodium":
    print ("Sodium (Na) \n Atomic Weight = 22.99 \n Group (Alkali Metal) ")
  elif element == "K" or element == "Potassium":
    print ("Potassium (K) \n Atomic Weight = 39.098 \n Group (Alkali Metal)")
  elif element == "F" or element == "Flourine":
    print ("Flourine (F) \n Atomic Weight == 18.998 \n Group (Halogens)")
  elif element == "Cl" or element == "Chlorine":
    print ("Chlorine (Cl) \n Atomic Weight == 35.45 \n Group (Halogens)")
  elif element == "Br" or element == "Bromine":
    print ("Bromine (Br) \n Atomic Number = 79.904 \n Group (Halogens)")
    
  
element = input("Enter Element: ")
output= details(element)
