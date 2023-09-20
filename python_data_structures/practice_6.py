#Find the intersection (common) of two sets and remove those elements from the first set

FIRST_SET = {23, 42, 65, 57, 78, 83, 29}
SECOND_SET = {57, 83, 29, 67, 73, 43, 48}

COMMON_VALUES = FIRST_SET.intersection(SECOND_SET)
print("Intersection is ", COMMON_VALUES)

for item in COMMON_VALUES:
        FIRST_SET.remove(item)
            
print("First set after removing common elements", FIRST_SET)            