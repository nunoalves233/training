import math

def senx(a, b):
    s=0.0
    for i in range(1,b+1):
        s += (-1)**(i+1) * a**(2*i-1)/math.factorial(2*i-1)
    resultado="{:.4f}".format(s)
    return resultado