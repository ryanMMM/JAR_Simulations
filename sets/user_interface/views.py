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
        print(request.POST)
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
        elif choice == '':
            pass
    else:
        form = Form()
        context['form'] = Form()
        context['display'] = 'true'
    return render(request, 'index.html', context)
