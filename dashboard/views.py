from django.shortcuts import render
from employees.models import Employee
from users.models import User
from lessons.models import Lesson
from categories.models import Category
from enrollments.models import Enrollment
from courses.models import Course
from instructors.models import Instructor
from students.models import Student
from tags.models import Tag
from categories.models import Category
from users.decorators import user_login_required

@user_login_required
def dashboard_home(request):
    # Count various models
    category_count = Category.objects.count()
    lesson_count = Lesson.objects.count()
    employee_count = Employee.objects.count()
    enrollment_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    instructor_count = Instructor.objects.count()
    student_count = Student.objects.count()
    tag_count = Tag.objects.count()
    user_count = User.objects.count()
    category_count = Category.objects.count()  # Added user count
    
    # Initialize financial totals (you'll need to adjust these based on your actual models)
    total_order_amount = 0
    total_order_remain_amount = 0
    
    # If you have an Order model, you would do something like:
    # from orders.models import Order  # Import your Order model
    # orders = Order.objects.all()
    # for order in orders:
    #     total_order_amount += order.total_amount
    #     total_order_remain_amount += order.total_remain
    
    content = {
        "category_count": category_count,
        "lesson_count": lesson_count,
        "employee_count": employee_count,
        "enrollment_count": enrollment_count,
        "course_count": course_count,
        "instructor_count": instructor_count,
        "student_count": student_count,
        "tag_count": tag_count,
        "user_count": user_count,
        "category_count":category_count,
    }
    return render(request, "dashboard/home.html", content)