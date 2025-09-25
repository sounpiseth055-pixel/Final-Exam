from django.urls import path
from . import views

urlpatterns = [
    # Lessons
    path('lessons/', views.lesson_list, name="lesson_list"),
    path('lessons/add/', views.lesson_add, name="lesson_add"),
    path('lessons/edit/<int:pk>/', views.lesson_edit, name="lesson_edit"),
    path('lessons/delete/<int:pk>/', views.lesson_deleted, name="lesson_delete"),

    # Lesson progress
    path('lesson-progress/', views.lesson_progress_list, name="lesson_progress_list"),
    path('lesson-progress/add/', views.lesson_progress_add, name="lesson_progress_add"),
    path('lesson-progress/edit/<int:pk>/', views.lesson_progress_edit, name="lesson_progress_edit"),
    path('lesson-progress/delete/<int:pk>/', views.lesson_progress_deleted, name="lesson_progress_delete"),

    # Assignments
    path('assignments/', views.assignment_list, name="assignment_list"),
    path('assignments/add/', views.assignment_add, name="assignment_add"),
    path('assignments/edit/<int:pk>/', views.assignment_edit, name="assignment_edit"),
    path('assignments/delete/<int:pk>/', views.assignment_deleted, name="assignment_delete"),
    
    # Submissions
    path('submissions/', views.submission_list, name="submission_list"),
    path('submissions/add/', views.submission_add, name="submission_add"),
    path('submissions/edit/<int:pk>/', views.submission_edit, name="submission_edit"),
    path('submissions/delete/<int:pk>/', views.submission_deleted, name="submission_delete"),
    
    # Reviews
    path('reviews/', views.review_list, name="review_list"),
    path('reviews/add/', views.review_add, name="review_add"),
    path('reviews/edit/<int:pk>/', views.review_edit, name="review_edit"),
    path('reviews/delete/<int:pk>/', views.review_deleted, name="review_delete"),
]
