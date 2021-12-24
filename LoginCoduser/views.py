from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request,'home.html')


def signUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
def signIn(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/',user)
            else:
                
                return render(request,'login.html')

    return render(request,'login.html')
        
def logoutUser(request):
    logout(request)
    return redirect('login')


