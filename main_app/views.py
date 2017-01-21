from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movement
from .forms import MovementForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    movements = Movement.objects.all()
    form = MovementForm()
    return render(request, 'index.html', {'movements': movements,
                                          'form': form})


def detail(request, movement_id):
    movement = Movement.objects.get(id=movement_id)
    return render(request, 'detail.html', {'movement': movement})


def post_movement(request):
    form = MovementForm(request.POST, request.FILES)
    if form.is_valid():
        # form.save(commit=True)
        movement = form.save(commit=False)
        movement.user = request.user
        movement.save()
    return HttpResponseRedirect('/')


def profile(request, username):
    user = User.objects.get(username=username)
    movements = Movement.objects.filter(user=user)

    return render(request, 'profile.html',
                  {'username': username, 'movements': movements})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled!")
            else:
                print("The username and password were incorrect")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
