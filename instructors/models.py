from django.db import models

from users.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    hire_date = models.DateField(auto_now_add=True)
    bio = models.TextField()
    expertise = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username
