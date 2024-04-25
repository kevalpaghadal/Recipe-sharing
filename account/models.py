from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
import json


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self , first_name , last_name , username , email , password=None):
        if not email:
            raise ValueError('user must have an email address')
        
        if not username:
            raise ValueError('user must have an username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self , first_name , last_name , username , email , password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    first_name = models.CharField(max_length = 50 , blank=True , null=True)
    last_name = models.CharField(max_length = 50 , blank=True , null=True)
    username = models.CharField(max_length = 50 , unique = True , null=True)
    email  = models.EmailField(max_length = 100 , unique = True , null=True)
    phone_number = models.CharField(max_length = 10 , blank = True , null=True)
    profile_picture = models.ImageField(upload_to='users/profile_picture' , blank=True , null= True , default='users/profile_picture/profile_avatar.png')
    address = models.CharField(max_length = 250 , blank=True , null=True)
    country = models.CharField(max_length = 30 , blank=True , null=True)
    state = models.CharField(max_length = 20 , blank=True , null=True)
    city = models.CharField(max_length = 20 , blank=True , null=True)
    pin_code = models.CharField(max_length = 6 , blank=True , null=True)



    # required fields 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now = True)
    
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # override the username as login to email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'first_name' , 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self , perm , obj=None):
        return self.is_admin
    
    def has_module_perms(self , app_label):
        return True
    

    
class AddRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    photo = models.ImageField(upload_to='users/recipe_photos/' , null= True , max_length = 250)
    video = models.FileField(upload_to='users/recipe_video/' , null= True , blank=True , max_length = 250)
    ingredients = models.TextField(blank=True , null=True)
    steps = models.TextField(blank=True , null=True)
    Servings = models.PositiveIntegerField(default=0, blank=True , null=True)
    meals = models.CharField(blank=True , null=True)
    prep_time = models.PositiveIntegerField(default=0 , blank=True , null=True) # in minutes
    prep_time_unit = models.CharField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def set_ingredients(self, value):
        self.ingredients = json.dumps(value)

    def get_ingredients(self):
        return json.loads(self.ingredients)


class Review(models.Model):
    recipe = models.ForeignKey(AddRecipe, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review = models.TextField(max_length=1000,null=True, blank=True)
    star = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        self.recipe


class ContactUs(models.Model):
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email
    
class Save(models.Model):
    recipe = models.ForeignKey(AddRecipe , on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Saved recipe: {self.recipe.title} by {self.user.username}'