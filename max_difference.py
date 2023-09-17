n = int(input())
max = 0
max1 = 0
m = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j] = int(input())
for i in range(n):
    for j in range(n):
        if m[i][j] - m[i][j-1] > m[i][j-1] - m[i][j-2]:
            max = m[i][j] - m[i][j-1]
        if m[i][j] - m[i-1][n-1] > m[i-1][n-1] - m[i-1][n-2]:
            max1 = m[i][j] - m[i-1][n-1]
if max > max1:            
    print(max)
else: print(max1)                  