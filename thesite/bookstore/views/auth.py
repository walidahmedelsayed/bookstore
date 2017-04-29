from django.contrib.auth import authenticate , login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def generate_user(name,email,password):
    user = User.objects.create_user(name,email,password)
    return True

def register(request):
    if request.method == 'POST':
        errors = []
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if  username is "" or email is "" or password is "" or repassword is "":
            errors.append("Please Fill All The Fields")

        elif (password != repassword):
            errors.append("Password Mismatch")

        elif User.objects.filter(username=username).exists():
            errors.append('Username Already Exists With The Same Name')

        elif User.objects.filter(email=email).exists():
            errors.append('Email Already Exists')

        if  len(errors) > 0:
            return render(request, 'register.html', {'errors': errors})
        else:
            if generate_user(username, email, password):
                return redirect('bookstore:home')
            else:
                return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    errors=[]
    if request.user.is_authenticated():
        return redirect('bookstore:home')

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            authlogin(request, user)
            return redirect('bookstore:home')
        else:
            errors.append('Invalid UserName or Password')
            return render(request, 'login.html',{'errors':errors})

    else:
        return render(request, 'login.html')

def logout(request):
    authlogout(request)
    return redirect('bookstore:login')