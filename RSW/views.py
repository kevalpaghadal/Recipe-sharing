from django.shortcuts import redirect , render
from account.models import AddRecipe , User


def home(request):
    user = request.user
    data = AddRecipe.objects.filter(user=user)

    context = {
        'data' : data
    }
    return render(request , 'home.html' , context)

def homePageRecipe(request , pk):

    user = request.user
    data = AddRecipe.objects.filter(user=user, pk=pk)

    recipe = AddRecipe.objects.get(pk=pk)

    ingredient_data = recipe.ingredients
    ingredient_X = []
    for ingredient in ingredient_data.split(', '):
        ingredient_X.append(ingredient)

    step_data = recipe.steps
    step_X = []
    for step in step_data.split(', '):
        step_X.append(step)

    context = {
        'data': data,
        'ingredient_X': ingredient_X,
        'step_X' : step_X,
    }

    return render(request , 'homePageRecipe.html' , context)

def contact_us(request):
    return render(request , 'contact_us.html')


def about_us(request):
    return render(request , 'about_us.html')