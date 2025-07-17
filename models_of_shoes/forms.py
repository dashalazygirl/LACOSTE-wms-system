from django import forms
from .models import Models_of_shoes, Arhiv

class Models_shoesForm(forms.ModelForm):
    class Meta:
        model = Models_of_shoes
        fields = '__all__'
        # fields = ['articul','model_s']
class ArticulForm(forms.Form):
    articul = forms.CharField(max_length=25,label='Артикул')

class SizeForm(forms.Form):
    size = forms.CharField(max_length=25,label='Размер русский')


class ArhivForm(forms.ModelForm):
    class Meta:
        model = Arhiv
        fields = '__all__'
