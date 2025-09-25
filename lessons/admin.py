from django.contrib import admin
from .models import Lesson,LessonProgress,Assignment,Submission,Review
admin.site.register(Lesson)
admin.site.register(LessonProgress)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Review)
