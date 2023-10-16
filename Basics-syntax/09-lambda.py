print("Lambda")

#A lambda function is a small anonymous function.

# Syntax : = lambda arguments : expression


x = lambda a : a + 10
print(x(5))

print(" ")

x = lambda a, b : a * b
print(x(5, 6))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)

print(mydoubler(5))