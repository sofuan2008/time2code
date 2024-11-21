# Square root program

# -------------------------
# Subprograms
# -------------------------
def sqroot(x):
  root = x
  root_number=0
  while root != root_number:
    root_number = root
    root = 0.5 * (root+(x/root))
    print(root)
  return root
  

# -------------------------
# Main program
# -------------------------
x = int(input("Enter a square number = "))
print("The square root of", x, "is", sqroot(x))
