from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from pandas import read_excel
import pandas
from .models import PreSchedule, User
from .helper_functions import file_handler
from .forms import Login, CreateUser, Upload, EditSchedule
from numba import jit, prange
import time

# Create your views here.
def homepage(request):
    title = "Roost"
    content = "Welcome"
    return render(request, "base.html", {"title": title, "content": content})

def process(request):
    title = "Roost"
    content = "Please upload an excel file"
    form = Upload
    if request.method =="POST":
        print("here")
        form = form(request.POST, request.FILES)
        if form.is_valid():
            file = read_excel(request.FILES['file'])
            start = time.time()
            datum = file_handler(file)
            end = time.time()
            print("Elapsed (after compilation) = %s" % (end - start))
            pre_schedule = PreSchedule(user=request.user, data=datum)
            pre_schedule.save()
        else:
            print("An error occurred with this file")
            form = form
    return render(request, "upload.html", {"title": title, "content": content, "form":form})

@jit(nopython=True, parallel= True, cache= True, nogil = True)
def generate(request, identity):
    start = time.time()
    schedule = PreSchedule.objects.get(user=request.user,pk=identity)
    data_frame = pandas.DataFrame(schedule.data)
    print(data_frame)

    for i in prange(1,3000):
        print(i)
        pass

    end = time.time()
    print("Elapsed (after compilation) = %s" % (end - start))
    return render(request, "dataframelist.html", {"content": data_frame})

def pre_schedule_view(request,identity):
    title = "Preview"
    datum = PreSchedule.objects.get(user=request.user,pk=identity)
    check = datum.data
    data_frame = pandas.DataFrame(check)
    print(data_frame)
    return render(request,"dataframe.html",{"title":title,"data_frame":data_frame})


def pre_schedule_list(request):
    title = "Staff Lists"
    datum = PreSchedule.objects.filter(user=request.user).values('name','id')
    return render(request, "dataframelist.html", {"content": datum, "title":title})


def edit_schedule(request, identity):
    title = "Edit"
    content = "Please edit this Schedule"

    form = EditSchedule

    if request.method =="POST":
        form = form(request.POST)
        if form.is_valid():
            pre_schedule = PreSchedule.objects.get(user=request.user, pk=identity)
            edit_form = EditSchedule(request.POST, instance=pre_schedule)
            edit_form.save()
        else:
            print("An error occurred with this file")
            form = form
    return render(request, "upload.html", {"title": title, "content": content, "form": form})







def register(request):
    message = ""
    form = CreateUser
    title = "Register"
    purpose = "Register"

    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            title = "Register"
            return render(request, "base.html", {"form": form, "title":title})
    return render(
        request,
        "base.html",
        {"form": form, "message": message, "title": title, "purpose": purpose},
    )


def log_in(request):
    title = "Login"
    message = ""
    purpose = "Login"
    form = Login
    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User(email=email, password=password)
            # user= User(username=username, password=password)
            try:
                login(request, user)
                return redirect("dashboard")
                # HttpResponsePermanentRedirect(redirect_to="/dashboard")
            except:
                message = "invalid credentials"
                return render(
                    request,
                    "registration/login.html",
                    {"form": form, "message": message},
                )

        else:
            return render(
                request, "registration/login.html", {"form": form, "message": message}
            )
    return render(
        request,
        "registration/login.html",
        {"form": form, "message": message, "title": title, "purpose": purpose},
    )


def forget_password(request):
    pass


def recover_password(request):
    pass


## Error Pages
def server_error(request):
    data = request.path
    return render(request, "errors/500.html", {"data": data})


def not_found(request, exception):
    data = request.path
    print(data)
    return render(request, "errors/404.html", {"data": data})


def permission_denied(request, exception):
    data = request.path
    return render(request, "errors/403.html", {"data": data})


def bad_request(request, exception):
    data = request.path
    return render(request, "errors/400.html", {"data": data})