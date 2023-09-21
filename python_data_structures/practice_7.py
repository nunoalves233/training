#Checks if one set is a subset or superset of another set. 
#If found, delete all elements from that set

FIRST_SET = {27, 43, 34}
SECOND_SET = {34, 93, 22, 27, 43, 53, 48}

SUB_BOOLEAN_1 = FIRST_SET.issubset(SECOND_SET)
SUB_BOOLEAN_2 = SECOND_SET.issubset(FIRST_SET)
SUPER_BOOLEAN_1 = FIRST_SET.issuperset(SECOND_SET)
SUPER_BOOLEAN_2 = SECOND_SET.issuperset(FIRST_SET)

print("First set is subset of second set -", SUB_BOOLEAN_1)
print("Second set is subset of fisrt set -", SUB_BOOLEAN_2)
print("First set is super set of second set -", SUPER_BOOLEAN_1)
print("Second set is super set of first set -", SUPER_BOOLEAN_2)

if SUB_BOOLEAN_1 == True:
    FIRST_SET.clear()
if SUB_BOOLEAN_2 == True:
    SECOND_SET.clear()  
    
print("First set ", FIRST_SET,"\n""Second set ", SECOND_SET)            