n = int(input())
a = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = float(input())       
for i in range(n):
    print(a[::-1][i][::-1])