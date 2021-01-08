from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import UserForm

from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required

# Create your views here.


@ csrf_exempt
def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if is_admin(user):

            if user is not None:
                login(request, user=user)
                return redirect("admin_home")

        return render(request, "Account/login_page.html", {})

        # we don't need to store this information, django offer us a login function
    return render(request, "Account/login_page.html", {})


@ csrf_exempt
def register_page(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # let's give the user a cue that the account was really created
            user = form.cleaned_data.get('username')
            messages.info(request, "The account was created successfully for " + user)
            return redirect('login')

    return render(request, "Account/register_page.html", {"form": form})


@ login_required(login_url="login")
@ csrf_exempt
def logout_page(request):
    logout(request)
    return redirect("home")


# with my code, the admin doesn't have a last name
def is_admin(the_user):
    obj = User.objects.all().get(username=the_user)
    return obj.last_name == ""
