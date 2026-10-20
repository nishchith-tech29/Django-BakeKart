from django.shortcuts import render
from .forms import RegistrationForm
def register(request):
    form=RegistrationForm()
    context={'form':form}
    return render(request, 'accounts/register.html', context)    
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    pass
# Create your views here.
