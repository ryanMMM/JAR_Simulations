from matplotlib_venn import venn2
from matplotlib import pyplot as plt
import itertools as ite
import os

def venn_diagram_generator(set1, set2, membership_output, operation_choice):
    plt.switch_backend('Agg')
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()
    subset_checker_output = subset_checker(set1, set2)
    venn_a = (set1-(set1.intersection(set2)))
    venn_b = (set2-(set1.intersection(set2)))
    venn_int = (set1.intersection(set2))
    venn_a_string = (str(venn_a)[1:-1])
    venn_b_string = (str(venn_b)[1:-1])
    venn_int_string = (str(venn_int)[1:-1])
    if operation_choice == 'membership' and membership_output[0] == 0:
        venn_int_string = venn_int_string[:membership_output[1] - 1] + '[' + venn_int_string[membership_output[1] - 1] + ']' + venn_int_string[membership_output[1]:]
    elif operation_choice == 'membership' and membership_output[0] == 1:
        venn_a_string = venn_a_string[:membership_output[1] - 1] + '[' + venn_a_string[membership_output[1] - 1] + ']' + venn_a_string[membership_output[1]:]
    elif operation_choice == 'membership' and membership_output[0] == 2:
        venn_b_string = venn_int_string[:membership_output[1] - 1] + '[' + venn_b_string[membership_output[1] - 1] + ']' + venn_b_string[membership_output[1]:]
    else:
        pass
    v = venn2(subsets=(len(venn_a), len(venn_b), len(venn_int)), set_labels=('Set A', 'Set B', 'Intersection'))

    if operation_choice == 'intersection' and venn_int:
        v.get_label_by_id('110').set_color('b')
    elif operation_choice == 'union':
        v.get_label_by_id('110').set_color('b')
        v.get_label_by_id('010').set_color('b')
        v.get_label_by_id('100').set_color('b')
    elif operation_choice == 'difference':
        v.get_label_by_id('100').set_color('b')
    else:
        pass
    labels = [venn_a_string, venn_b_string, venn_int_string]
    if subset_checker_output == "Neither set is a subset of the other":
        v.get_label_by_id('100').set_text(labels[0])
    else:
        v.get_label_by_id('100').set_text('')
    v.get_label_by_id('010').set_text(labels[1])
    if venn_int:
        v.get_label_by_id('110').set_text(labels[2])
    plt.savefig('user_interface/static/user_interface/img/'+'venn.png')
    plt.savefig('user_interface/img/'+'venn.png')

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
        index = str(set1.intersection(set2))[1:-1].find(str(user_input))
        return_text = str(user_input) + " is a member of both sets at position " + str(index) + "of intersection"
        return return_text
    # 0 represents intersection, index represents to position of the input in the intersection string
    elif user_input in set1:
        index = str(set1)[1:-1].find(str(user_input))
        return_text = str(user_input) + " is a member of set A at position " + str(index)
        return return_text
    # 1 represents set 1, index represents to position of the input in the set1 string
    elif user_input in set2:
        index = str(set1)[1:-1].find(str(user_input))
        return_text = str(user_input) + " is a member of set B at position " + str(index)
        return return_text
    # 2 represents set 1, index represents to position of the input in the set2 string
    else:
        return_text = str(user_input) + " is a not a member of either set"
        return return_text

'''
#testing
setA = {1, 2, 3, 4, 5}
setB = {1, 4, 5, 6, 7}
venn_diagram_generator(setA, setB)
'''
