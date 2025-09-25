from django import forms
from .models import Lesson,LessonProgress,Assignment,Submission,Review
class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonEditForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonProgressAddForm(forms.ModelForm):
    class Meta:
        model = LessonProgress
        fields = '__all__'

class LessonProgressEditForm(forms.ModelForm):
    class Meta:
        model = LessonProgress
        fields = '__all__'

class AssignmentAddForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentEditForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class SubmissionAddForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = '__all__'

class SubmissionEditForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = '__all__'

class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'