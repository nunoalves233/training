MAX_SIZE=10
  
# function to sort each row of the matrix
# according to the order specified by
# ascending.
def sortByRow(mat, n, ascending):
 
    for i in range(n):
        if (ascending):   
            mat[i].sort()
        else:
            mat[i].sort(reverse=True)
  
# function to find
# transpose of the matrix
def transpose(mat, n):
 
    for i in range(n):
        for j in range(i + 1, n):
         
            # swapping element at index (i, j)
            # by element at index (j, i)
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
 
# function to sort
# the matrix row-wise
# and column-wise
def sortMatRowAndColWise(mat, n):
 
    # sort rows of mat[][]
    sortByRow(mat, n, False)
  
    # get transpose of mat[][]
    transpose(mat, n)
  
    # again sort rows of
    # mat[][] in descending
    # order.
    sortByRow(mat, n, False)
  
    # again get transpose of mat[][]
    transpose(mat, n)
  
# function to print the matrix
def printMat(mat, n):
 
    for i in range(n):
        for j in range(n):
            if j == 0:
                print("["f"{mat[i][j]:.1f}, ", end="")
            if j == n-1:
                print(f"{mat[i][j]:.1f}""]", end="")    
            if j in range(1, n-1):
                print(f"{mat[i][j]:.1f}, ", end="")    
        print()
 
#Driver code
n = int(input())
m = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j] = int(input())
  
sortMatRowAndColWise(m, n)
  
printMat(m, n)