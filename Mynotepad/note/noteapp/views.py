from django.shortcuts import render,redirect
from noteapp.forms import NOTEForm
from django.contrib import messages
from .models import NOTE
from noteapp.models import NOTE,Contact
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,"front.html")

def note(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login First")
        return redirect('/auth/signup')
    return redirect("home")

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = NOTEForm()
        notes = NOTE.objects.filter(user = user).order_by('date')
        return render(request , 'index.html' , context={'form' : form , 'notes' : notes})

@login_required(login_url='login')
def add_note(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = NOTEForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})


def delete_note(request , id ):
    print(id)
    NOTE.objects.get(pk = id).delete()
    return redirect('home')


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"we will get back to you soon..")
        return render(request,"contact.html")

    return render(request,"contact.html")

# def signup(request):
#     return render(request,"signup.html")

# def signin(request):
#     return render(request,"login.html")

