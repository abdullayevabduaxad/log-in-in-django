from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Homework_Login
from .form import Home_Login_Forms


def Photo(request):
    template = loader.get_template('thret.html')
    return HttpResponse(template.render())


def Shop(request):
    template = loader.get_template('second.html')
    return HttpResponse(template.render())


def Link(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def Avatar(request):
    template = loader.get_template('four.html')
    return HttpResponse(template.render())


def homework_login(request):
    obj = Homework_Login.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        for i in obj:
            if username == i.username and password == i.password:
                return redirect('home_page')

        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})

    return render(request, "login.html")


def homework_home_page(request):
    temp = loader.get_template("welcom.html")
    return HttpResponse(temp.render())


def homework_register(request):
    if request.method == "POST":
        form = Home_Login_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_login')
    form = Home_Login_Forms()

    page = {
        "forms": form
    }
    return render(request, "register.html", page)
