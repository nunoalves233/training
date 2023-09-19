#Write a program to remove the item present at index 4 
#and add it to the 2nd position and at the end of the list.

SAMPLE_LIST = [34, 54, 67, 89, 11, 43, 94]

ELEMENT = SAMPLE_LIST.pop(4)
print("List After removing element at index 4", SAMPLE_LIST)

SAMPLE_LIST.insert(2, ELEMENT)
print("List after Adding element at index 2", SAMPLE_LIST)

SAMPLE_LIST.append(ELEMENT)
print("List after Adding element at last", SAMPLE_LIST)