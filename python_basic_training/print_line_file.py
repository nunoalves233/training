####1
file1 = input('Filename:')
f1 = open(file1,"r")
total = 0
num_items = 0

line1 = f1.readline()
while line1 != '':
    total += float(line1)
    num_items += 1
    line1 = f1.readline()
    
mean = total / num_items    
print(f"Mean = {mean:.2f}")
f1.close()

####3
file = input('Filename 1:')
fh = open(file,"r")
file1 = input('Filename 2:')
fh1 = open(file1,"r")
line = fh.readline().strip()
line1 = fh1.readline().strip()
while line != "":
    print(line)
    line = fh.readline().strip()
while line1 != "":
    print(line1)
    line1 = fh1.readline().strip()
fh.close()
fh1.close()

####2
file_name1 = input('Filename 1:')
file_name2 = input('Filename 2:')

with open(file_name1, "r") as file1:
    line1 = file1.readline().strip()
    
    while line1 != '':

        with open(file_name2, "r") as file2:

            line2 = file2.readline().strip()

            while line2 != '':
                print(line1, line2)
                line2 = file2.readline().strip()

        line1 = file1.readline().strip()