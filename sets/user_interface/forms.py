from django import forms

# define choices user has
CHOICES = [
('union', 'Perform union operation (set of members in set A or B or both)'),
('intersection', 'Perform intersection operation (set of members in both set A and B)'),
('difference', 'Perform difference operation (set of members in set A but not in B)'),
('subset', 'Check whether set A is a (proper) subset of set B')
]

# define form that user will complete
class Form(forms.Form):
    set1 = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your set A:"}
        ),
    )
    set2 = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your set B:"}
        ),
    )
    choice = forms.MultipleChoiceField(
            required=True,
            widget=forms.RadioSelect,
            choices=CHOICES,
    )
    venn_diagram = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[('yes', 'Do you want to display the venn diagram?')],
    )
