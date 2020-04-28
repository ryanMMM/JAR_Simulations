from matplotlib_venn import venn2
from matplotlib import pyplot as plt

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

'''
#testing
setA = {1, 2, 3, 4, 5}
setB = {1, 4, 5, 6, 7}
venn_diagram_generator(setA, setB)
'''
