from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from tkinter import messagebox

# Create your views here.
def customer(request):
    # return HttpResponse("this is for customers")
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        uname = request.POST['uname']
        passw = request.POST['password']
        cpassw = request.POST['cpassword']
        if passw == cpassw:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username is already taken.")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=uname,
                                                password=passw,
                                                email=email,
                                                first_name=fname,
                                                last_name=lname)
                user.save()
                print("User Created")
        else:
            messages.info(request, "Password Mismatch")
            return redirect('/register')
        return redirect('/login')
    return render(request, 'newsignin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('customerlog')
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('/login')
    return render(request, 'login.html')

@login_required
def customerlog(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
    return render(request, 'account.html', context)

def exitsite(request):
    messagebox.showwarning('Exiting',"successfully exited")
    return render(request, 'exit_file.html')