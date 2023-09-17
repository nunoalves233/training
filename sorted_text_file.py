file = input('Filename:')
n = 0
fh = open(file,"r")
lines = fh.readlines()
lines.sort()
while lines != "":
    n += 1
    print(lines)
    print()
    if lines == "":
        break
fh.close()    
print("Count of names: ", n)    

