import random
from random import randint

m = int(input("Enter Size "))
R = int(input("Enter Probability"))

matrix=[]
for i in range(m):
    c=[]
    for j in range(m):
        rand = randint(0,100)
        if(i == 0 and j == 0):
            j = "S"
        elif(i == (m-1) and j == (m-1)):
            j = "E"
        elif(rand > R):
            j = "O"
        else:
            j = "X"
        c.append(j)
    matrix.append(c)

print()

for i in range(m):
    for j in range(m):
        print(matrix[i][j], end="    ")
    print()
        

