# Exam grade program

# -------------------------
# Subprograms
# -------------------------
def grade(mark):
  if mark>= 80:
    grade = 9
    next_mark = "n/a"
  elif mark >= 67:
    grade = 8
    next_mark = 80 - mark
    
  elif mark >= 54:
    grade = 7
    next_mark = 67 - mark
  
  elif mark >= 41:
    grade = 6
    next_mark = 54 - mark
  
  elif mark>= 31:
    grade=5
    next_mark = 41 - mark
  
  elif mark >= 22:
    grade =  4
    next_grade= 31-mark
    
  elif mark >= 13:
    grade = 3
    next_grade = 22-mark
    
  elif mark >= 4:
    grade = 2
    next_grade = 13 - mark
  
  elif mark >= 2:
    grade = 1
    next_grade = 4-mark
  else:
    grade = "U"
    next_grade = 2-mark
# -------------------------
# Main program
# -------------------------
mark = int(input("Input the mark from 0-100: "))
grade = grade(mark)
