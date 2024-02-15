from django.shortcuts import render , redirect
from .forms import UserForm
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request , 'You are already logged in!')
        return redirect('home')
    elif request.method == 'POST':  
        # print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            messages.success(request , 'Your account has been register sucessfully')
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form' : form,
    }
    return render(request , 'account/registerUser.html' , context)

def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request , 'You are already logged in!')
        return redirect('home')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email , password=password)

        if user is not None:
            auth.login(request , user)
            messages.success(request , 'You are now logged in. ')
            return redirect('home')
        else:
            messages.error(request , 'Invalid login')
            return redirect('loginUser')
    return render(request , 'account/loginUser.html')

def logoutUser(request):
    auth.logout(request)
    messages.info(request , 'You are logged out.')
    return redirect('loginUser')

@login_required(login_url = 'loginUser')
def userProfile(request):
    return render(request , 'account/userProfile.html')

@login_required(login_url = 'loginUser')
def addRecipe(request):
    return render(request , 'account/addRecipe.html')