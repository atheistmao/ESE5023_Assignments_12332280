##########Q5##########
#Q5-1
from functools import reduce
 
operator = {
    1: '+',
    2: '-',
    0: ''
}
 
base = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
 
def operator_evaluation(num):
 
    arr = []
    for index in range(8):
        index = 7 - index
        arr.append(num // (3 ** index))
        num -= (num // (3 ** index)) * (3 ** index)
    arr = map(lambda x: operator[x], arr)
 
    formula = reduce(lambda x, y: x + y, zip(base, arr))
 
    formula = list(formula)
    formula.append('9')
 
    formula = ''.join(formula)
    res = eval(formula)
    return res, formula
 
def Find_expression(target):
  total = 3 ** 8
  for i in range(total):
    res, formula = operator_evaluation(i)
    if res == target:
      print(formula + ' = %d' % target)
#test
Find_expression(50)
#Q5-2
import matplotlib.pyplot as plt

# Existing code

Total_solutions = []
for i in range(1, 101):
  count = 0
  for j in range(3**8):
    res, formula = operator_evaluation(j)
    if res == i:
      count += 1
  Total_solutions.append(count)

plt.plot(range(1, 101), Total_solutions)
plt.xlabel('Integer')
plt.ylabel('Number of solutions')
plt.title('Number of solutions for integers 1-100')
plt.show()
# Get index of max and min counts
max_idx = Total_solutions.index(max(Total_solutions))    
min_idx = Total_solutions.index(min(Total_solutions))

print("Integer with max solutions:", max_idx + 1)
print("Integer with min solutions:", min_idx + 1)