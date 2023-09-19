def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f   

def comb(n, p):
    cb = fact(n) / (fact(p) * fact(n-p))
    return cb

m = int(input("n="))
p = int(input("p="))
cb = comb(m, p)
print("Combinations = ",cb)
