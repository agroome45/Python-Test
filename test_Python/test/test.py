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
            print(matrix[i][j],i,j, end="    ")
        print()
    print()
    
def DFS(matrix, start_location, end_location):
    fringe = []
    closed = []
    fringe.append(start_location)
    while(len(fringe) != 0):
        print(fringe, "fringe")
        current = fringe.pop()
        print(current, "current")
        if(closed.count(current) == 0):
            if(current == end_location):
                return True
            else:
                i = current[0]
                j = current[1]
                if((i + 1) >= 0 and (i + 1) <= m and matrix[i+1][j] == "O"):
                    fringe.append([i+1,j])
                if((i - 1) >=0 and (i - 1) <= m and matrix[i-1][j] == "O" ):
                    fringe.append([i-1,j])
                if((j + 1) >=0 and (j + 1) <= m and matrix[i][j+1] == "O" ):
                    fringe.append([i,j+1])  
                if((j - 1) >= 0 and (j - 1) <= m and matrix[i][j-1] == "O"):
                    fringe.append([i,j-1])
                closed.append(current) 
    return False 
     
            
m = int(input("Enter Size "))
R = int(input("Enter Probability"))

print()
matrix = create_maze(m, R)
print_maze(matrix, m)

print(DFS(matrix, [0,0], [m,m]))
