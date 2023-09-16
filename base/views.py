from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
#from django.http HttpResponse

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, "Email already Exist, used a different email address"
                )
                return redirect("signup")

            if User.objects.filter(username=username).exists():
                messages.info(
                    request,
                    "Username taken, used a different username!",
                )
                return redirect("signup")
            if len(password) < 8:
                messages.info(request, 'Password must be at least 8 characters')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()

                # log user in and direct to settings page
                user_login = auth.authenticate(
                    username=username, password=password
                )
                auth.login(request, user_login)

                # create a Profile model for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id
                )
                new_profile.save()
                return redirect("login")#login
        else:
            messages.info(
                request,
                "Password not Matching!",
            )
            return redirect("signup")
    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, "Invalid Credentials, please make sure you enter the correct information!")
            return redirect("login")
    else:
        return render(request, "login.html")

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("login")

def contact(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def topic1(request):
    return render(request, 'topic1.html')

@login_required(login_url='login')
def topic2(request):
    return render(request, 'topic2.html')