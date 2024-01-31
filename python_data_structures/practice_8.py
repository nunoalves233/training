# Iterate a given list and check if a given element exists as a key’s value in a dictionary.
#If not, delete it from the list

ROLL_NUMBER = [47, 64, 69, 37, 76, 83, 95, 97]
SAMPLE_DICTIONARY = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

ROLL_NUMBER[:] = [item for item in ROLL_NUMBER if item in SAMPLE_DICTIONARY.values()]
print("after removing unwanted elements from list:", ROLL_NUMBER)