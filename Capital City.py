# Capital city program

# -------------------------
# Subprograms
# -------------------------
def check_answer(country, city):
    if country == "England" and city == "London":
        return True
    if country == "France" and city == "Paris":
        return True
    if country == "Spain" and city == "Madrid":
        return True
    else:
        return False


def capital_cities():
    correct = False
    while not correct:
        city = input("What is the capital city of England? : ")
        correct = check_answer("England", city)
    
    correct = False    
    while not correct:
        city = input("What is the capital city of France? : ")
        correct = check_answer("France", city)
        
    correct = False    
    while not correct:
        city = input("What is the capital city of Spain? : ")
        correct = check_answer("Spain", city)


# -------------------------
# Main program
# -------------------------
capital_cities()
print("The quiz is complete.")
