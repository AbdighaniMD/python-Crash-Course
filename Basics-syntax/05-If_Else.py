print("If ... Else")

a = 200
b = 20
if b > a: # False 
  print("b is greater than a")
elif a == b: # 
  print("a and b are equal") # "if the previous conditions were not true, then try this condition"
else: # The else keyword catches anything which isn't caught by the preceding conditions
  print("a is greater than b")

"""
The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.
"""
if b > a:
  pass


# Ternary Operators, or Conditional Expressions

# Short Hand If
if a > b: print("ShortHand if: - a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

#Multiple else statements on the same line:
D = 33
C = 33
print("D") if D > C else print("=") if D == C else print(C)

#And
if D < a and D == C:
  print("Both conditions are True, D is less then a and D and C are equal")

#OR
if D > a or D == C:
  print("At least one of the conditions is True")

#Not
if not D > C: #reverse the true into False
  print("D is NOT greater than C")


#Nested If
if b > 10:
  print("Above ten,")
  if b >= 20:
    print("and also above 20!")
  else:
    print("but not above 20.")