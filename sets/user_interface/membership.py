'''
this program checks if an input is a member of one of two
sets.
'''

def membership(set1, set2, user_input):
    if user_input in set1 and user_input in set2:
        return(str(user_input) + " is a member of both sets")
    elif user_input in set1:
        return(str(user_input) + " is a member of the first set")
    elif user_input in set2:
        return(str(user_input) + " is a member of the second set")
    else:
        return(str(user_input) + " is a not a member of either set")

'''
setA = {1, 2}
setB = {1, 3}
#Testing
print(membership(setA, setB, 1))
#expected output: 1 is a member of both sets
print(membership(setA, setB, 2))
#expected output: 2 is a member of the first set
print(membership(setA, setB, 3))
#expected output: 3 is a member of the second set
print(membership(setA, setB, 4))
#expected output: 4 is a not a member of either set
'''
