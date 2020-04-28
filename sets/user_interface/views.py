from django.shortcuts import render
from user_interface.forms import Form
from user_interface.inputHandling import cleanUp


def index(request):
    context = {}
    if request.method == "POST":
        form = Form(request.POST)
        set1 = cleanUp(request.POST['set1'])
        set2 = cleanUp(request.POST['set2'])
    else:
        form = Form()
        context['form'] = Form()
    return render(request, 'index.html', context)
