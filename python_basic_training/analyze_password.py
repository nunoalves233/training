def my_function(n):
        rev_n = n[::-1]
        print(*rev_n)
        lst = []
        for letter in n:
                lst.append(letter)
        print(*lst)
        n1 = input("Qual a letra que deseja encontrar?\n")  
        for i in range(len(lst)):
                if lst[i] == n1:
                        print("A letra foi encontrada na posição", i)     

n = input("Qual a palavra que deseja analisar?\n")
my_function(n)


