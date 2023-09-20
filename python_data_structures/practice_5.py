#Create a Python set such that it shows the element from both lists in a pair

FIRST_LIST = [2, 3, 4, 5, 6, 7, 8]
SECOND_LIST = [4, 9, 16, 25, 36, 49, 64]

RESULT = zip(FIRST_LIST, SECOND_LIST)
RESULT_SET = set(RESULT)
print(RESULT_SET)