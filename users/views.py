from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . form import UserRegisterForm


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username} Your Account have been created and you are able to login !')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
