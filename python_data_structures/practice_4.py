#Write a program to iterate a given list and count the occurrence 
#of each element and create a dictionary to show the count of each element.

SAMPLE_LIST = [11, 45, 8, 11, 23, 45, 23, 45, 89]

COUNT_DICT = dict()
for item in SAMPLE_LIST:
    if item in COUNT_DICT:
        COUNT_DICT[item] += 1
    else:
        COUNT_DICT[item] = 1

print("Printing count of each item  ", COUNT_DICT)