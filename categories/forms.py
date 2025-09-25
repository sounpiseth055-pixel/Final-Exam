from django import forms
from .models import Category
class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'