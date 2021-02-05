from django import forms


class Account(forms.Form):

    opportunity = forms.CharField(max_length=200)
    Company = forms.CharField(max_length=200)
    Stage_of_completion = forms.CharField(max_length=200)
    Amount = forms.DecimalField(max_digits=100, decimal_places=2)
