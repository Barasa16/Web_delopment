from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegForm

# Create your views here.
def register(request):
    if request.method == "POST":
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get(username)
            messages.success(request, f"Account created for {username}!")
            return redirect("login")

    else:
        reg_form = RegForm()
    return render(request, "register.html", {"form": reg_form})


def login(request):
    login_form = UserCreationForm()
    return render(request, "login.html", {"form": login_form})


def home(request):
    return render(request, "home.html")
