##########Q2##########
#Q2-1
import numpy as np

# Generate 5x10 matrix M1  
M1 = np.random.randint(0, 50, size=(5, 10))

# Generate 10x5 matrix M2
M2 = np.random.randint(0, 50, size=(10, 5)) 

print("M1:")
print(M1)

print("M2:") 
print(M2)
#Q2-2
def Matrix_multip(M1, M2):
  result = [[0 for j in range(len(M2[0]))] for i in range(len(M1))]

  for i in range(len(M1)):
    for j in range(len(M2[0])):
      for k in range(len(M2)):
        result[i][j] += M1[i][k] * M2[k][j]

  return result
Matrix_multip(M1, M2)