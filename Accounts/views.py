from django.shortcuts import render

# Create your views here.
from .forms import Account
from django.contrib.auth.models import User


def account(request):
    acc_form = Account()
    if request.method == "POST":
        acc_form = Account(request.POST)
        if acc_form.is_valid():
            username = acc_form.cleaned_data.get(User.username)
            # messages.success(request, f"Account details for {{username}}! saved")
            acc_form = Account()
    return render(request, "home.html", {"form": acc_form})

