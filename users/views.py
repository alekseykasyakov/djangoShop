from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Создан аккаунт {username}!')
			return redirect('login	')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


def password_reset(request):
	return render(request, 'users/password_reset_form.html')


@login_required
def profile(request):
	return render(request, 'users/profile.html')