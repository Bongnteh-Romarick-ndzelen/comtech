from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import ContactForm, LiveChatForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    
    forms = LiveChatForm(request.POST)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Thank You, Your Message was submitted Successfully! We will get back to you soon!')
        return redirect('/')
    topics = HomePage.objects.all()
    context = {
        'forms': forms,
        'topics': topics,
    }
    return render(request, 'index.html', context)

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
                messages.info(request, 'Password too short! Password must be at least 8 characters')
                return redirect('signup')
            if password.isalpha():
                messages.info(request, 'Password must contain a number!')
                return redirect('signup')
            
            if password.isnumeric():
                messages.info(request, 'Password must contain an alphabet!')
                return redirect('signup')
            if password.islower():
                messages.info(request, 'Password must contain an Uppercase letter!')
                return redirect('signup')
            if len(username) < 7:
                messages.info(request, 'Username too short!')
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
            messages.info(request, "Invalid Credentials, Wrong Username Or Password!")
            return redirect("login")
    else:
        return render(request, "login.html")

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required(login_url='login')
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Thank You, Your Message was submitted Successfully! We will get back to you soon.')
        return redirect('contact')
    context = {
        'form': form,
        }
    return render(request,'contact.html', context)

@login_required(login_url='login')
def topic1(request):
    return render(request, 'topic1.html')

@login_required(login_url='login')
def topic2(request):
    return render(request, 'topic2.html')

@login_required(login_url='login')
def topic3(request):
    return render(request, 'topic3.html')

@login_required(login_url='login')
def topic4(request):
    return render(request, 'topic4.html')

@login_required(login_url='login')
def topic5(request):
    return render(request, 'topic5.html')


@login_required(login_url="login")
def settings(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Create a new Profile object if it doesn't exist
        user_profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('profileimg') is None:
            profileimg = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = profileimg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        if request.FILES.get('profileimg') is not None:
            profileimg = request.FILES.get('profileimg')
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = profileimg
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        return redirect('settings')
    
    return render(request, "settings.html", {'user_profile': user_profile})

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')