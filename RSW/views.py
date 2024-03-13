from django.shortcuts import redirect , render


def home(request):
    return render(request , 'home.html')

def contact_us(request):
    return render(request , 'contact_us.html')


def about_us(request):
    return render(request , 'about_us.html')