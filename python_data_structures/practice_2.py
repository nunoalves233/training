#Write a program to remove the item present at index 4 
#and add it to the 2nd position and at the end of the list.

LIST_1 = [34, 54, 67, 89, 11, 43, 94]

ELEMENT = LIST_1.pop(4)
print("List After removing element at index 4", LIST_1)

LIST_1.insert(2, ELEMENT)
print("List after Adding element at index 2", LIST_1)

LIST_1.append(ELEMENT)
print("List after Adding element at last", LIST_1)