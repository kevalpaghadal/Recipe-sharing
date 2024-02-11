from django.shortcuts import render

# Create your views here.

def loginUser(request):
    return render(request , 'account/loginUser.html')

def registerUser(request):
    return render(request , 'account/registerUser.html')

def userProfile(request):
    return render(request , 'account/userProfile.html')

def addRecipe(request):
    return render(request , 'account/addRecipe.html')