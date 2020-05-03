from django.shortcuts import render
from user_interface.forms import Form
from user_interface.inputHandling import cleanUp
from user_interface import setsOperations


def index(request):
    context = {}
    if request.method == "POST":
        context['display'] = 'false'
        form = Form(request.POST)
        set1 = cleanUp(request.POST['set1'])
        set2 = cleanUp(request.POST['set2'])
        choice = request.POST['choice']
        if 'venn_diagram' in request.POST:
            generateVennDiagram = True
        else:
            generateVennDiagram = False
        if choice == 'union':
            context['return_set'] = set1.union(set2)
        elif choice == 'intersection':
            context['return_set'] = set1.intersection(set2)
        elif choice == 'difference':
            context['return_set'] = set1.difference(set2)
        elif choice == 'subset':
            context['return_set'] = setsOperations.subset_checker(set1, set2)
        elif choice == 'cartesian':
            context['return_set'] = setsOperations.cartesian_product(set1, set2)
        elif choice == 'member':
            user_input = request.POST['user_input']
            try:
                user_input = int(user_input)
                context['return_set'] = setsOperations.membership(set1, set2, user_input)
            except:
                context['return_set'] = "Invalid input for the membership operation"
        if generateVennDiagram:
            setsOperations.venn_diagram_generator(set1, set2, setsOperations.membership(set1, set2), choice)
            context['display_diagram'] = 'true'
        else:
            context['display_diagram'] = 'false'
    else:
        form = Form()
        context['form'] = Form()
        context['display'] = 'true'
    return render(request, 'index.html', context)
