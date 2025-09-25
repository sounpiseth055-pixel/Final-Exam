from django.shortcuts import render,redirect
from . models import Lesson, LessonProgress, Assignment, Submission, Review
from .forms import LessonAddForm, LessonEditForm, LessonProgressAddForm, LessonProgressEditForm, AssignmentAddForm, AssignmentEditForm, SubmissionAddForm, SubmissionEditForm, ReviewAddForm, ReviewEditForm

def lesson_list(request):
    lesson = Lesson.objects.all()
    return render(request,"lesson/lesson_list.html",{"lessons":lesson})

def lesson_add(request):
    form = LessonAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lesson_list")
    return render(request,"lesson/lesson_add.html",{"form":form})

def lesson_edit(request, pk):
    lesson = Lesson.objects.filter(pk = pk).first()
    form = LessonEditForm(request.POST or None,instance=Lesson)
    if form.is_valid():
        form.save()
        return redirect("lesson_list")
    return render(request,"lesson/lesson_edit.html",{"form":form})

def lesson_deleted(request,pk):
    lesson = Lesson.objects.filter(pk = pk).first()
    if request.method == "POST":
        lesson.delete()
        return redirect("lesson_list")
    return render(request,"lesson/lesson_delete.html",{"lesson":lesson})

# LessonProgress

def lesson_progress_list(request):
    lesson_progress = LessonProgress.objects.all()
    return render(request,"lesson_progress/lesson_progress_list.html",{"lesson":lesson_progress})

def lesson_progress_add(request):
    form = LessonProgressAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lesson_progress_list")
    return render(request,"lesson_progress/lesson_progress_add.html",{"form":form})

def lesson_progress_edit(request, pk):
    lesson_progress = LessonProgress.objects.filter(pk = pk).first()
    form = LessonProgressEditForm(request.POST or None,instance=lesson_progress)
    if form.is_valid():
        form.save()
        return redirect("lesson_progress_list")
    return render(request,"lesson_progress/lesson_progress_edit.html",{"form":form})

def lesson_progress_deleted(request,pk):
    lesson_progress = LessonProgress.objects.filter(pk = pk).first()
    if request.method == "POST":
        lesson_progress.delete()
        return redirect("lesson_progress_list")
    return render(request,"lesson_progress/lesson_progress_delete.html",{"lesson":lesson_progress})

#Assignment
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request,"assignment/assignment_list.html",{"lessons":assignments})

def assignment_add(request):
    form = AssignmentAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("assignment_list")
    return render(request,"assignment/assignment_add.html",{"form":form})

def assignment_edit(request, pk):
    assignment = Assignment.objects.filter(pk = pk).first()
    form = AssignmentEditForm(request.POST or None,instance=assignment)
    if form.is_valid():
        form.save()
        return redirect("assignment_list")
    return render(request,"assignment/assignment_edit.html",{"form":form})

def assignment_deleted(request,pk):
    assignment = Assignment.objects.filter(pk = pk).first()
    if request.method == "POST":
        assignment.delete()
        return redirect("assignment_list")
    return render(request,"assignment/assignment_delete.html",{"lesson":assignment})

#Submisson


def submission_list(request):
    submisssion = Submission.objects.all()
    return render(request,"submission/submission_list.html",{"lessons":submisssion})

def submission_add(request):
    form = SubmissionAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("submission_list")
    return render(request,"submission/submission_add.html",{"form":form})

def submission_edit(request, pk):
    submission = submission.objects.filter(pk = pk).first()
    form = SubmissionEditForm(request.POST or None,instance=submission)
    if form.is_valid():
        form.save()
        return redirect("submission_list")
    return render(request,"submission/submission_edit.html",{"form":form})

def submission_deleted(request,pk):
    submission = Submission.objects.filter(pk = pk).first()
    if request.method == "POST":
        submission.delete()
        return redirect("submission_list")
    return render(request,"submission/submission_delete.html",{"lesson":submission})

#Review

def review_list(request):
    reviews = Review.objects.all()
    return render(request,"review/review_list.html",{"lessons":reviews})

def review_add(request):
    form = ReviewAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("review_list")
    return render(request,"review/review_add.html",{"form":form})

def review_edit(request, pk):
    review = Review.objects.filter(pk = pk).first()
    form = ReviewEditForm(request.POST or None,instance=review)
    if form.is_valid():
        form.save()
        return redirect("review_list")
    return render(request,"review/review_edit.html",{"form":form})

def review_deleted(request,pk):
    review = Review.objects.filter(pk = pk).first()
    if request.method == "POST":
        review.delete()
        return redirect("review_list")
    return render(request,"review/review_delete.html",{"lesson":review})