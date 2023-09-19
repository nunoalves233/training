#Given two lists, l1 and l2, write a program to create
#a third list l3 by picking an odd-index element from the 
#list l1 and even index elements from the list l2.

LIST_1 = [3, 6, 9, 12, 15, 18, 21]
LIST_2 = [4, 8, 12, 16, 20, 24, 28]
FINAL_LIST = list()

ODD_ELEMENTS = LIST_1[1::2]
print("Element at odd-index positions from list one")
print(ODD_ELEMENTS)

EVEN_ELEMENTS = LIST_2[0::2]
print("Element at even-index positions from list two")
print(EVEN_ELEMENTS)

print("Printing Final third list")
FINAL_LIST.extend(ODD_ELEMENTS)
FINAL_LIST.extend(EVEN_ELEMENTS)
print(FINAL_LIST)