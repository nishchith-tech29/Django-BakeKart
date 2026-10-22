
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout    


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            username = email.split('@')[0]

            try:
                user = Account.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password
                )

                user.phone_number = phone_number
                user.save()

                messages.success(
                    request, 'Your account has been created successfully!'
                )
                return redirect('register')

            except Exception as e:
                form.add_error(None, str(e))

        else:
            print(form.errors)

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Account.objects.filter(email=email).first()

        if user is not None and user.check_password(password):
            # Perform login logic here (e.g., set session, redirect to dashboard)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Replace 'dashboard' with your desired URL name
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'accounts/login.html')


def logout(request):

    auth_logout(request)  
    # Perform logout logic here (e.g., clear session, redirect to login page)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')  # Replace 'login' with your desired URL name
