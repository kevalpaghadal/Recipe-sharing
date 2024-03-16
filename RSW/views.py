from django.shortcuts import redirect , render
from account.models import AddRecipe , User , Review
from django.db.models import Q




def home(request):
    data = AddRecipe.objects.all().order_by('-updated_at')

    context = {
        'data' : data
    }
    return render(request , 'home.html' , context)

def homePageRecipe(request , pk):
    if  request.user.is_authenticated:
        recipe = AddRecipe.objects.get(pk=pk)
        user = request.user
        data = AddRecipe.objects.get(pk=pk)
        try:
            review = Review.objects.get(user=user , recipe=pk)


            context = {
                'data' : data,
                'userFlag' : True,
                'review' : review,
            }

        except:
            if request.method == 'POST':
                Star = request.POST.get('star-value')
                review = request.POST.get('Reviews')
        
                recipe_rating = Review( recipe=recipe, user=user, star=Star , review=review)
                recipe_rating.save()

            # review = Review.objects.filter(user=user , recipe=pk)
                
            
        

            context = {
                'data' : data,
                'userFlag' : True,
                # 'review' : review,
            }
        return render(request , 'homePageRecipe.html' , context)
    else:

        data = AddRecipe.objects.get(pk=pk)
    
        context = {
            'data':data,
            'userFlag' : False,
        }
    return render(request , 'homePageRecipe.html' , context)

def srcRecipe(request):
    
    query = request.POST.get('search_recipe_id')
    print(query)

    if query == None or query == "":
        return redirect('home')
    else:
        fetch_recipe = AddRecipe.objects.filter(
            Q(title__icontains=query) |
            Q(meals__icontains=query) |
            Q(ingredients__icontains=query))
        
    context = {
        'fetch_recipe' : fetch_recipe
    }   


    return render(request, 'searchPageRecipe.html' , context)

def contact_us(request):
    return render(request , 'contact_us.html')


def about_us(request):
    return render(request , 'about_us.html')