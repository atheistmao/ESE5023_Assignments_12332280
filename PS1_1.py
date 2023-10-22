##########Q1##########
def Print_values(a, b, c):
  if a >= b and a >= c:
    if b >= c:
      print(a, b, c)
    else:
      print(a, c, b)
  elif b >= a and b >= c:
    if a >= c:
      print(b, a, c)
    else:
      print(b, c, a)
  else:
    if a >= b:
      print(c, a, b)
    else:
      print(c, b, a)

a = int(input("please enter the a value:"))  
b = int(input("please enter the b value:"))
c = int(input("please enter the c value:"))

Print_values(a, b, c)