from django.shortcuts import redirect , render
from account.models import AddRecipe , User , Review , ContactUs , Save
from django.db.models import Q
from django.contrib import messages

from django_xhtml2pdf.utils import pdf_decorator





from datetime import datetime, timedelta

def home(request):
    web_title = 'home'


    # Calculate the date 3 days ago
    latest = datetime.now() - timedelta(days=3)

    # Retrieve latest uploaded recipes within the last 3 days
    latest_recipes = AddRecipe.objects.filter(created_at__gte=latest).order_by('-created_at')

    context = {
        'web_title': web_title,
        'latest_recipes': latest_recipes
    }
    return render(request, 'home.html', context)



def homePageRecipe(request, pk):
    if request.user.is_authenticated:
        user = request.user

        data = AddRecipe.objects.get(pk=pk)
        ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
        ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

        step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
        step_data = [steps.replace('"', '') for steps in step_with_quotes]
        check = Save.objects.filter(recipe=pk)
        try:
            review = Review.objects.get(user=user, recipe=pk)
            

            context = {
                'check' : check,
                'data': data,
                'userFlag': True,
                'review': review,
                'request': request,
                'ingredient_data': ingredient_data,
                'step_data': step_data,
            }
        except Review.DoesNotExist:
            review = None

            if request.method == 'POST':
                Star = request.POST.get('star-value')
                review_text = request.POST.get('Reviews')

                recipe_rating = Review(user=user, star=Star, review=review_text, recipe=data)
                recipe_rating.save()

                # Redirect after POST to prevent form resubmission on page refresh
                return redirect('homePageRecipe', pk=pk)

            context = {
                'check' : check,
                'data': data,
                'userFlag': True,
                'request': request,
                'ingredient_data': ingredient_data,
                'step_data': step_data
            }
    else:
        data = AddRecipe.objects.get(pk=pk)
        ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
        ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

        step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
        step_data = [steps.replace('"', '') for steps in step_with_quotes]
        check = Save.objects.filter(recipe=pk)
        print(check)
        context = {
            'check' : check,
            'data': data,
            'userFlag': False,
            'request': request,
            'ingredient_data': ingredient_data,
            'step_data': step_data
        }

    return render(request, 'homePageRecipe.html', context)


def srcRecipe(request):
    query = request.POST.get('search_recipe_id')
    search_type = request.POST.get('search_type')

    # Start with all recipes
    fetch_recipe = AddRecipe.objects.all()

    if query:
        # If there's a query, filter by title, meals, or ingredients
        fetch_recipe = fetch_recipe.filter(
            Q(title__icontains=query) |
            Q(meals__icontains=query) |
            Q(ingredients__icontains=query) 
        )

    if search_type and search_type != 'All Types':
        # If a specific type is selected, further filter by that type
        fetch_recipe = fetch_recipe.filter(meals=search_type)

    context = {
        'fetch_recipe': fetch_recipe
    }

    return render(request, 'searchRecipe.html', context)



def formSearch(request):
    # Get the selected checkboxes from the form
    if request.method == 'POST':
        selected_meals = request.POST.getlist('meals')
        print(selected_meals)
        
        # Start with all recipes
        fetch_recipe = AddRecipe.objects.all()

        if selected_meals:
            # Start with an empty query
            query = Q()
            # Iterate over selected meals to build the query
            for meal in selected_meals:
                query |= Q(title__icontains=meal) | Q(description__icontains=meal) | Q(ingredients__icontains=meal)
            
            # Apply the combined query to filter recipes
            fetch_recipe = fetch_recipe.filter(query)

            context = {
                'fetch_recipe' : fetch_recipe
            }
            return render(request , 'showFormRecipe.html', context)

    return render(request, 'formSearch.html')

def ShowFormRecipe(request):
    return render(request , 'ShowFormRecipe.html')


def srcRecipePage(request , pk):
    if  request.user.is_authenticated:
        recipe = AddRecipe.objects.get(pk=pk)
        user = request.user
        data = AddRecipe.objects.get(pk=pk)

        ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
        ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

        step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
        step_data = [steps.replace('"', '') for steps in step_with_quotes]
        check = Save.objects.filter(recipe=pk)
        try:
            review = Review.objects.get(user=user , recipe=pk)


            context = {
                'check' : check,
                'data' : data,
                'userFlag' : True,
                'review' : review,
                'request': request,
                'ingredient_data': ingredient_data,
                'step_data': step_data
            }

        except:
            if request.method == 'POST':
                Star = request.POST.get('star-value')
                review = request.POST.get('Reviews')
        
                recipe_rating = Review( recipe=recipe, user=user, star=Star , review=review)
                recipe_rating.save()        

            context = {
                'check' : check,
                'data' : data,
                'userFlag' : True,
                'request': request,
                'ingredient_data': ingredient_data,
                'step_data': step_data
            }
        return render(request , 'searchRecipePage.html' , context)
     
    else:

        data = AddRecipe.objects.get(pk=pk)
        ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
        ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

        step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
        step_data = [steps.replace('"', '') for steps in step_with_quotes]
        check = Save.objects.filter(recipe=pk)
        
        context = {
            'check' : check,
            'data':data,
            'userFlag' : False,
            'request': request,
            'ingredient_data': ingredient_data,
            'step_data': step_data
        }
    return render(request , 'searchRecipePage.html' , context)


@pdf_decorator(pdfname = 'recipe.pdf')
def printRecipe(request ,pk):
    recipe = AddRecipe.objects.filter(pk=pk)
    data = AddRecipe.objects.get(pk=pk)
    ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
    ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

    step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
    step_data = [steps.replace('"', '') for steps in step_with_quotes]
    check = Save.objects.filter(recipe=pk)
 
    
    context = {
        'check' : check,
        'recipe' : recipe,
        'ingredient_data': ingredient_data,
        'step_data': step_data
    }
    return render(request, 'PrintRecipePage.html' , context)



def contact_us(request):
    web_title = 'Contact Us'
    if request.method == 'POST':
        # Assuming the user is logged in and you're using request.user to get the user
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database
        contact_us_form_data = ContactUs(email=email, message=message)
        contact_us_form_data.save()

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_us')
    else:
        return render(request, 'contact_us.html' , {'web_title' : web_title})


def about_us(request):
    web_title = 'About us'

    return render(request , 'about_us.html' , {'web_title' : web_title})

def team(request):
    web_title = 'Our team'
    return render(request , 'team.html' ,{'web_title' : web_title})