from django import forms 
from . models import Top

class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        fields ='__all__'
        widgets = {
            'id' : forms.TextInput(attrs={'class':'form-control'}),
            'users' : forms.TextInput(attrs={'class':'form-control'}),
            'balance' : forms.TextInput(attrs={'class':'form-control'}),
        }



