import itertools as ite

def cartesian_product(set1, set2):
    return set(ite.product(set1, set2))

'''
#TESTING
setA = {1, 2}
setB = {3, 4}
print(cartesian_product(setA, setB))
'''
#tests were successful
