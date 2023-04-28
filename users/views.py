from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from .models import Person


def login(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                messages.success(request, f"Successfully logged in {username}!")
            else:
                messages.alert(request, f"Not a valid user")
            return redirect('LC_SearchEngine_Contributor')

    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')

            user = form.save(commit=False)
            user.save()

            person = Person.objects.create(email=email, role=role, user=user)
            person.save()

            messages.success(request, f"Account has been created for {username} ! You can now login")
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})
