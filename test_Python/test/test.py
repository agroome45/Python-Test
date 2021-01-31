import random
from random import randint

def create_maze(m,R):
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
    return matrix


def print_maze(matrix,m):
    for i in range(m):
        for j in range(m):
            print(matrix[i][j], end="    ")
        print()
    print()
    
def DFS(matrix, start_location, end_location):
    fringe = []
    fringe.append(start_location)
    while(fringe.empty):
        current = fringe.pop()
        if(current == end_location):
            return True
        else:
            i = 0
            
        
    
        
m = int(input("Enter Size "))
R = int(input("Enter Probability"))

print()
matrix = create_maze(m, R)
print_maze(matrix, m)
