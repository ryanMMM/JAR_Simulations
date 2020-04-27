'''
This script must input 2 sets and detect whether one set
is a subset, proper subset or not a subset of the other
'''

def subset_checker(set1, set2):
    if set1.issubset(set2) and len(set1) == len(set2):
        return ("The first set is a non-proper subset of the second set")
    elif set1.issubset(set2):
        return("The first set is a proper subset of the second set")
    elif set2.issubset(set1):
        return("The second set is a proper subset of the first set")
    else:
        return("Neither set is a subset of the other")

set_A = {0, 1, 2}
set_B = {0, 1, 2}
set_C = {0, 1, 2, 3}
set_D = {0, 1, 4}
set_E = {4, 5, 6}

#TESTING
'''
print(subset_checker(set_A, set_B))
#Expected output: The first set is a non-proper subset of the second set
print(subset_checker(set_A, set_C))
#Expected output: The first set is a proper subset of the second set
print(subset_checker(set_C, set_A))
#Expected output: The second set is a proper subset of the first set
print(subset_checker(set_A, set_D))
#Expected output: Neither set is a subset of the other
'''
#Tests were successful