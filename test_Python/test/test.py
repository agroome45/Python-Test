m = int(input("Enter Size please test test"))
Mat = []
for i in range (0,m):
    Mat.append([])
for i in range (0,m):
    for j in range(0,m):
        Mat[i].append(j)
        Mat[i][j]=0
for i in range (0,m):
    for j in range (0,m):
        print ('entry in row: ', i+1, ' column: ', j+1)
        Mat[i][j]= int(input())
print(Mat)
        
        

