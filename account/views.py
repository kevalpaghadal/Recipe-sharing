from django.shortcuts import render , redirect

from account.models import User
from .forms import UserForm
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required
from .utils import send_verification_email
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


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

            # send varification email
            mail_subject = 'please activate your account'
            email_template = 'account/emails/account_verification_email.html'
            send_verification_email(request , user , mail_subject , email_template)
            messages.success(request , 'Your account has been register sucessfully, Please check your email')
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


def activate(request , uidb64 , token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError , ValueError , OverflowError , User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request , 'Congratulation! Your account is activated.')
        return redirect('loginUser')
    else:
        messages.error(request , 'Invalid activation link')
        return redirect('registerUser')




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
    user = User.objects.get(pk = request.user.pk)
    return render(request , 'account/userProfile.html',{'user' : user})

@login_required(login_url = 'loginUser')
def addRecipe(request):
    ingrediants = []
    steps = []
    if request.method == 'POST':
        titel = request.POST['titel']
        description = request.POST['description']
        # photo = request.POST['photo']
        ingrediant_ct = request.POST['js_inputCounter']
        for i in range(1 , int(ingrediant_ct)):
            ingrediants.append(request.POST['ingre-'+str(i)])
            # print(request.POST['ingre-'+str(i)])

        print(ingrediants)


        # ste_ct = request.POST['js_inputCounter']
        # for i in range(1 , int(ste_ct)):
        #     steps.append(request.POST['ste-'+str(i)])

        # print(steps)

        prep_time = request.POST['prep_time']
        prep_time_unit = request.POST['prep_time_unit']

        return redirect('addRecipe')
    

    return render(request , 'account/addRecipe.html')


def yourRecipe(requset):
    return render(requset , 'account/yourRecipe.html')



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact = email)

            # send reset password email
            mail_subject = 'Reset your password'
            email_template = 'account/emails/reset_password_email.html'
            send_verification_email(request , user , mail_subject , email_template)

            messages.success(request , 'password reset link has been sent to your email address.')
            return redirect('loginUser')
        else:
            messages.error(request , 'Account does not exist.')
            return redirect('forgot_password')

    return render(request , 'account/forgot_password.html')


def reset_password_validate(request , uidb64 , token):
    # valid the user by decoding the token and user pk
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError , ValueError , OverflowError , User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request , 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request , 'This link has been expired!')
        return redirect('loginUser')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk = pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'password reset successful')
            return redirect('loginUser')
        else:
            messages.error(request , 'password does not match!')
            return redirect('reset_password')
    return render(request , 'account/reset_password.html')

    