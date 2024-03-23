from django.shortcuts import render, redirect

from account.models import User, AddRecipe
from .forms import UserForm , UserProfileForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .utils import send_verification_email
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.

def registerUser(request):
    web_title = 'register'
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')
    elif request.method == 'POST':
        # print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            # send varification email
            mail_subject = 'please activate your account'
            email_template = 'account/emails/account_verification_email.html'
            send_verification_email(
                request, user, mail_subject, email_template)
            messages.success(
                request, 'Your account has been register sucessfully, Please check your email')
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
        'web_title' : web_title
    }
    return render(request, 'account/registerUser.html', context)



def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation! Your account is activated.')
        return redirect('loginUser')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('registerUser')


def loginUser(request):
    web_title = 'login'
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in. ')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login')
            return redirect('loginUser')
        
    return render(request, 'account/loginUser.html' , {'web_title': web_title})


def logoutUser(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('loginUser')

@login_required(login_url='loginUser')
def userProfile(request):
    web_title = 'profile'
    user = request.user

    if request.method == 'POST':
        userform = UserProfileForm(request.POST, request.FILES, instance=user)
        if userform.is_valid():
            userform.save()
            messages.success(request, 'Congratulations! Your profile has been updated.')
            return redirect('userProfile')
        else:
            # Print form errors for debugging
            print(userform.errors)
            messages.error(request, 'Invalid form data. Please correct the errors.')
    else:
        userform = UserProfileForm(instance=user)
    
    context = {
        'user': user,
        'userform': userform,
        'web_title' : web_title
        
    }

    return render(request, 'account/userProfile.html', context)


@login_required(login_url='loginUser')
def addRecipe(request):
    web_title = 'Add Recipe'

    ingredients = ''
    steps = ''

    if request.method == 'POST' and request.FILES:

        user = User.objects.get(email=request.user)
        print(user)

        title = request.POST['titel']
        description = request.POST['description']
        photo = request.FILES['recipe_photo']

        if 'recipe_video' in request.FILES:
            video = request.FILES['recipe_video']
            Recipe_data = AddRecipe(video=video)
            Recipe_data.save()
        # ingrediants input fileds loop
        ingrediant_ct = request.POST['js_inputCounter']
        for i in range(1, int(ingrediant_ct)):
            ingredients += request.POST['ingre-' + str(i)] + ":::"

        # step input fileds loop
        step_ct = request.POST['js_inputCounter_step']
        for i in range(1, int(step_ct)):
            steps += request.POST['step-' + str(i)] + ":::"

        prep_time = request.POST['prep_time']
        prep_time_unit = request.POST['prep_time_unit']
        meals = request.POST['meals']
        Servings = request.POST['Servings']


        Recipe_data = AddRecipe(user=user, title=title, description=description, photo=photo,steps=steps, Servings=Servings, meals=meals, prep_time=prep_time, prep_time_unit=prep_time_unit)
    
        Recipe_data.set_ingredients(ingredients)

        Recipe_data.save()
        messages.success(request , 'Recipe Submited sucessfully')
        return redirect('addRecipe')

    return render(request, 'account/addRecipe.html' , {'web_title': web_title})


@login_required(login_url='loginUser')
def yourRecipe(request):
    web_title = 'Your Recipe'

    user = request.user
    data = AddRecipe.objects.filter(user=user)
    # print(data)
    context = {
        'data': data,
        'web_title' : web_title
    }
    return render(request, 'account/yourRecipe.html', context)

@login_required(login_url='loginUser')
def delete_recipe(request , pk):
    recipe = get_object_or_404(AddRecipe , pk=pk)
    recipe.delete()
    return redirect('yourRecipe')

@login_required(login_url='loginUser')
def recipePage(request, pk):

    web_title = 'Recipe'
    data = AddRecipe.objects.get(pk=pk)

    ingredient_with_quotes = [i.strip() for i in data.ingredients.split(':::') if i.strip()]
    ingredient_data = [ingredient.replace('"', '') for ingredient in ingredient_with_quotes]

    step_with_quotes = [i.strip() for i in data.steps.split(':::') if i.strip()]
    step_data = [steps.replace('"', '') for steps in step_with_quotes]

    user = request.user
    data = AddRecipe.objects.filter(user=user, pk=pk)


    context = {
        'data': data,
        'web_title' : web_title,
        'ingredient_data': ingredient_data,
        'step_data': step_data
    }
    return render(request, 'account/recipePage.html', context)


def forgot_password(request):
    web_title = 'Forgot Password'

    # Check if the user is logged in
    if request.user.is_authenticated:
        # If the user is logged in, log them out
        logoutUser(request)

    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # send reset password email
            mail_subject = 'Reset your password'
            email_template = 'account/emails/reset_password_email.html'
            send_verification_email(
                request, user, mail_subject, email_template)

            messages.success(
                request, 'password reset link has been sent to your email address.')
            return redirect('loginUser')
        else:
            messages.error(request, 'Account does not exist.')
            return redirect('forgot_password')

    return render(request, 'account/forgot_password.html' , {'web_title': web_title})


def reset_password_validate(request, uidb64, token):
    # valid the user by decoding the token and user pk
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('loginUser')


def reset_password(request):

    web_title = 'Reset Password'

    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'password reset successful')
            return redirect('loginUser')
        else:
            messages.error(request, 'password does not match!')
            return redirect('reset_password')
    return render(request, 'account/reset_password.html' , {'web_title': web_title})
