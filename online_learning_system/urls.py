"""
URL configuration for online_learning_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import urls as user_urls
from lessons import urls as lesson_urls
from tags import urls as tags_urls
from employees import urls as employee_urls
from courses import urls as course_urls
from students import urls as student_urls
from instructors import urls as instructor_urls
from categories import urls as categories_urls
from enrollments import urls as enrollment_urls
from dashboard import urls as dashboard_urls
from lessons import urls as lesson_urls
from accounts import urls as account_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',include(student_urls)),
    path("users/", include(user_urls)),
    path("enrollments/",include(enrollment_urls)),
    path("employees/",include(employee_urls)),
    path("instructor/",include(instructor_urls)),
    path("courses/",include(course_urls)),
    path("categories/",include(categories_urls)),
    path("lessons/", include(lesson_urls)),
    path("tags",include(tags_urls)),
    path("",include(dashboard_urls)),
    path("",include(account_urls)),
]
