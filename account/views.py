from django.shortcuts import render , redirect
from .forms import UserForm
from django.contrib import messages

# Create your views here.

def loginUser(request):
    return render(request , 'account/loginUser.html')

def registerUser(request):
    if request.method == 'POST':
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

def userProfile(request):
    return render(request , 'account/userProfile.html')

def addRecipe(request):
    return render(request , 'account/addRecipe.html')