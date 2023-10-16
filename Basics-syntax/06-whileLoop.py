print("Python has two primitive loop commands: While loops, For loops")

i = 1
while i <= 3:
  print(i)
  i += 1

print("At 4 Break the loop statement ")


# The break Statement we can stop the loop even if the while condition is true:
i = 1;
while i < 7:
  print(i)
  if i == 4:
    break
  i+=1

print("Continue = skip 4 statement ")

i = 0;
while i < 5:
  i+=1
  if i == 4:
    continue
  print(i)

print(" ")

#The else Statement
i = 1
while i < 3:
  print(i)
  i += 1
else:
  print("The else statement we can run a block of code once when the condition no longer is true:")


