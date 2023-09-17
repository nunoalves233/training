#Exercise1

number1 = int(input("number1 = "))
number2 = int(input("number2 = "))
p = number1 * number2
if p <= 1000:
    print("The result is ", p)
else:
    print("The result is ", number1 + number2) 

#Exercise2

num = 0
pr_num = 0
for i in range(10):
    sum = num + pr_num
    print(f"Current Number {num:.0f} Previous Number {pr_num:.0f} Sum: {sum:.0f}")
    pr_num = num
    num += 1

#Exercise3

string = input("Original String is  ")
lst = []
 
for letter in string:
    lst.append(letter)

print("Printing only even index chars")    

for i in range(len(lst)):
    if i == 0 or i % 2 == 0:
        print(lst[i])

#Exercise4

string = input("String in cause: ")
n = int(input("Number of characters to remove: "))

print(string[n:])

#Exercise5

n = int(input("Size of the list:"))
lst =[]

for i in range(n):
    lst.append(int(input("")))

print("Given list = ", lst)

if lst[0] == lst[n-1]:
    print("result is True")
else: print("result is False")

#Exercise6

n = int(input("Size of the list:"))
lst =[]

for i in range(n):
    lst.append(int(input("")))

print("Given list is ", lst)
print("Divisible by 5")

for x in range(n):
    if lst[x] % 5 == 0:
        print(lst[x])

#Exercise7

str = input("String to analyse: ")
sub_str = input("The substring we need to count: ")
print(str.count(sub_str))        

#Exercise8

# outer loop
for i in range(6):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')

#Exercise9

n = int(input("Enter the number you want to analyse: "))

def rev_num(n):
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return rev    

if rev_num(n) == n:
    print("Yes. given number is palindrome number")
else: print("No. given number is not a palindrome number")  

#Exercise10

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_lst = []

for i in range(len(list1)):
    if list1[i] % 2 == 1:
        new_lst.append(list1[i])    
for j in range(len(list2)):
    if list2[j] % 2 == 0:
        new_lst.append(list2[j]) 
print(new_lst)        

#Exercise11

n = int(input("Enter the number you want to analyse: "))

rev = 0
while(n > 0):
    a = n % 10
    print(a, end=' ')
    rev = rev * 10 + a
    n = n // 10
print('')    

#Exercise12

income = int(input("Income: "))
first = 10000
second = 10000
rest = income - first - second
tax_payable = first * 0 + second * 0.1 + rest * 0.2
print(int(tax_payable))

#Exercise13

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=' ')
    print('')    

#Exercise14

rows = int(input("Enter the number of rows: "))  
  
# the outer loop is executing in reversed order  
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ") 

#Exercise15

def exponent(base, exp):
    result = 0
    result = base**exp
    return result

base = int(input("base = "))
exp = int(input("exponent = "))
answer = exponent(base, exp)
print("", base,"raises to the power of", exp,": ", answer)






        