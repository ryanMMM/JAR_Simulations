from django import forms

# define choices user has
CHOICES = [
('csv', 'Load csv file'),
('own', 'Input your own array (syntax: comma sepparated values, e.g. 1, 2, 3, 4, 5)'),
('random', 'Generate random array (syntax: start, end, number of entries, e.g. -5, 5, 7)')
]

# define form that user will complete
class Form(forms.Form):
    # user input depending on choice
    set1 = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your set 1:"}
        ),
    )
    set2 = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your set 2:"}
        ),
    )
    # radio buttons for ch
    """choice = forms.MultipleChoiceField(
            required=True,
            widget=forms.RadioSelect,
            choices=CHOICES,
        )
    # file upload
    file = forms.FileField(required=False)
    # for search only: target element
    target = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Target element"}
        ),
    )
    """
