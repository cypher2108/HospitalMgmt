from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect


# Create your views here.
def about(request):
    return render(request, 'about.html')


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


def login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            if not request.user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'index.html', d)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request, 'index.html')
