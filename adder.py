# Adder program

# -------------------------
# Subprograms
# -------------------------
def adder():
    total = 0
    top = 0
    count = 0
    ave = 0
    complete = False
    while not complete:
        number = input("Enter number: ")
        if  number != "e" :
            number = float(number)
            total = total + number
            count = count + 1
            if number > top:
                top = number
        else:
            complete = True
            if count > 0:
                ave = total / count
            else:
                ave = 0
    print("Total:", total, "Top:", top, "Ave:", ave)


# -------------------------
# Main program
# -------------------------
adder()
