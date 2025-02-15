# Save the change program

# -------------------------
# Subprograms
# -------------------------
def nearest_pound(amount):
    return int(amount) + 1


def save_the_change(amount):
    if int(amount) != amount:
        savings = nearest_pound(amount) - amount
    else:
        savings = 0
    return savings
    
    
# -------------------------
# Main program
# -------------------------
purchase_price = float(input("Enter the purchase price: £"))
debit = nearest_pound(purchase_price)
savings = save_the_change(purchase_price)
print("Debit - £{0:.2f}".format(debit))
print("Credit to savings - £{0:.2f}".format(savings))




