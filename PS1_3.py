##########Q4##########
import random

def Least_moves(x):
  moves = 0
  money = 1

  while money < x:
    if money*2 <= x: 
      money = money * 2
      moves += 1
    else:
      money += 1
      moves += 1

  print(moves)
#test
x = random.randint(1, 100)
print("Random x:", x)
Least_moves(x)