##########Q4##########
import random

def Least_moves(x):
  moves = 0

  while x > 1:
    if x%2 == 0: 
      x = x / 2
      moves += 1
    else:
      x = x - 1
      moves += 1

  print(moves)
#test
x = random.randint(1, 100)
print("Random x:", x)
Least_moves(x)