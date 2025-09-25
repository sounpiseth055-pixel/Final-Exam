from django.urls import path
from . import views

urlpatterns = [
    path('',views.course_list,name="course_list"),
    path('add/',views.course_add,name="course_add"),
    path('edit/<int:pk>/',views.course_edit,name="course_edit"),
    path('delete/<int:pk>/',views.course_deleted,name="course_delete"),
]