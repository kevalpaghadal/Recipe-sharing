from django.urls import path
from . import views

urlpatterns = [
    path('loginUser/' , views.loginUser , name='loginUser'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('logoutUser/' , views.logoutUser , name='logoutUser'),
    path('userProfile/' , views.userProfile, name='userProfile'),
    path('addRecipe/', views.addRecipe , name='addRecipe'),
]