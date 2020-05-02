from matplotlib_venn import venn2
from matplotlib import pyplot as plt
import itertools as ite

def venn_diagram_generator(set1, set2):

    venn_a = (set1-(set1.intersection(set2)))
    venn_b = (set2-(set1.intersection(set2)))
    venn_int = (set1.intersection(set2))

    v = venn2(subsets=(len(venn_a), len(venn_b), len(venn_int)), set_labels=('Set A', 'Set B', 'Intersection'))

    labels = [str(venn_a)[1:-1], str(venn_b)[1:-1], str(venn_int)[1:-1]]

    v.get_label_by_id('100').set_text(labels[0])
    v.get_label_by_id('010').set_text(labels[1])
    v.get_label_by_id('110').set_text(labels[2])

    plt.savefig('venn.png')

def subset_checker(set1, set2):
    if set1.issubset(set2) and len(set1) == len(set2):
        return ("Set A is a non-proper subset of the Set B")
    elif set1.issubset(set2):
        return("Set A is a proper subset of the Set B")
    elif set2.issubset(set1):
        return("Set B is a proper subset of the Set A")
    else:
        return("Neither set is a subset of the other")


def cartesian_product(set1, set2):
    return set(ite.product(set1, set2))


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
#testing
setA = {1, 2, 3, 4, 5}
setB = {1, 4, 5, 6, 7}
venn_diagram_generator(setA, setB)
'''
