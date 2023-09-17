def printMat(mat, n):
 
    for i in range(n):
        for j in range(n):
            print(mat[i][j] , " ", end="")
        print()

n = int(input())
m = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j] = int(input())
for i in range(n):
    for j in range(n):
        m.sort(int, quicksort, str)
printMat(m,n)   
