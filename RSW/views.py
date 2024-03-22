from django.shortcuts import redirect , render
from account.models import AddRecipe , User , Review , ContactUs
from django.db.models import Q
from django.contrib import messages





def home(request):
    web_title = 'home'

    data = AddRecipe.objects.all().order_by('-updated_at')

    context = {
        'data' : data,
        'web_title' : web_title
    }
    return render(request , 'home.html' , context)

def homePageRecipe(request, pk):
    if request.user.is_authenticated:
        user = request.user

        data = AddRecipe.objects.get(pk=pk)
        ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
        ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

        step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
        step_data = [steps.replace('"', '') for steps in step_with_quotes]


        try:
            review = Review.objects.get(user=user, recipe=pk)

            context = {
                'data': data,
                'userFlag': True,
                'review': review,
                'request': request,
                'ingredient_data': ingredient_data,
                'step_data': step_data
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
                'data': data,
                'userFlag': True,
                'request': request,
                'ingredient_data': ingredient_data,
                'step_data': step_data
            }
    else:
        data = AddRecipe.objects.get(pk=pk)
        ingredient_data = [i.strip() for i in data.ingredients.split(',') if i.strip()]
        step_data = [i.strip() for i in data.steps.split(',') if i.strip()]
        context = {
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
    print(search_type)
    # print(query)

    if query == None or query == "" and search_type == 'All Types':
        fetch_recipe = AddRecipe.objects.all()
    
    elif search_type == 'Breakfast':
        fetch_recipe = AddRecipe.objects.filter(meals=search_type)

    elif search_type == 'Main Course':
        fetch_recipe = AddRecipe.objects.filter(meals=search_type)

    elif search_type == 'Side Dish':
        fetch_recipe = AddRecipe.objects.filter(meals=search_type)

    elif search_type == 'Snacks':
        fetch_recipe = AddRecipe.objects.filter(meals=search_type)

    elif search_type == 'Desserts':
        fetch_recipe = AddRecipe.objects.filter(meals=search_type)

    else:
        fetch_recipe = AddRecipe.objects.filter(
            Q(title__icontains=query) |
            Q(meals__icontains=query) |
            Q(ingredients__icontains=query)) 
        
    context = {
        'fetch_recipe' : fetch_recipe
    }


    return render(request, 'searchRecipe.html' , context)

def srcRecipePage(request , pk):
    if  request.user.is_authenticated:
        recipe = AddRecipe.objects.get(pk=pk)
        user = request.user
        data = AddRecipe.objects.get(pk=pk)

        ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
        ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

        step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
        step_data = [steps.replace('"', '') for steps in step_with_quotes]

        try:
            review = Review.objects.get(user=user , recipe=pk)


            context = {
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
                'data' : data,
                'userFlag' : True,
                'request': request,
                'ingredient_data': ingredient_data,
                'step_data': step_data
            }
        return render(request , 'searchRecipePage.html' , context)
     
    else:

        data = AddRecipe.objects.get(pk=pk)
        ingredient_data = [i.strip() for i in data.ingredients.split(',') if i.strip()]
        step_data = [i.strip() for i in data.steps.split(',') if i.strip()]
    
        context = {
            'data':data,
            'userFlag' : False,
            'request': request,
            'ingredient_data': ingredient_data,
            'step_data': step_data
        }
    return render(request , 'searchRecipePage.html' , context)





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