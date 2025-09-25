from django.urls import path
from . import views


urlpatterns = [
    path('',views.user_list,name="user_list"),
    path('add/',views.user_add,name="user_add"),
    path('edit/<int:pk>/',views.user_edit,name="user_edit"),
    path('delete/<int:pk>/',views.user_deleted,name="user_delete"),
]