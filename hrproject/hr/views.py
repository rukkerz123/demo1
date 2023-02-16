from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid max account")
            return redirect('login')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        tenth_passed = request.POST["tenth_passed"]
        twelve_passed = request.POST["twelve_passed"]
        graduation_degree = request.POST["graduation_degree"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["password1"]

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This Already Name Taken")
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This Already Email Taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username, tenth_passed=tenth_passed, twelve_passed=twelve_passed,
                                                email=email, password=password, graduation_degree=graduation_degree)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not matched")
            return redirect("signup")
        return redirect('/')
    return render(request, "signup.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
