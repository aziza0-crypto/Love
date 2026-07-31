from django.shortcuts import render, redirect
from .models import Student, Application


def index(request):

    if request.method == "POST":

        Application.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            comment=request.POST.get("comment"),
            agree=True if request.POST.get("agree") else False
        )

        return redirect("index")


    students = Student.objects.all()


    return render(request, "index.html", {
        "students": students
    })