from django import forms
from .models import Enrollment
class EnrollmentAddForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

class EnrollmentEditForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'