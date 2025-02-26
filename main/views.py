from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from main.models import Maqola


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        if request.POST.get('password1') != request.POST.get('password2') or request.POST.get(
                'username') in User.objects.values_list('username', flat=True):
            return redirect('register')
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password1')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('register')
    return render(request, 'register.html')

def maqola_view(request):
    maqola = Maqola.objects.all()
    context = {
        'maqola': maqola,
    }
    return render(request, 'maqolalar.html', context)