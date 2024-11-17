# Exam grade program

# -------------------------
# Subprograms
# -------------------------
def interest_rate (money, interest, target_money):
  target = 0
  year = 1
  money = money
  interest_rate= interest/100
  interest_money = 0

  while interest_money !< target_money:
    interest_money = (interest_money * interest_rate)+interest_money
    year = year+1
    print ("Year",year,"Balance = £",interest_money)


# -------------------------
# Main program
# -------------------------
money = int(input("Enter the balance to the nearest pound: £ "))
interest = int(input("Enter the % interest rate:  "))
target_money = int(input("Enter the target balance to the nearest pound: £ "))
output = interest_rate(money, interest, target_money)
