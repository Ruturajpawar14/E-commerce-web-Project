from django import forms


class myForm(forms.Form):
    num1=forms.CharField(label="value1",required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label="value2",widget=forms.TextInput(attrs={'class':"form-control"}))
