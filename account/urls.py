from django.urls import path
from . import views

urlpatterns = [
    path('loginUser/' , views.loginUser , name='loginUser'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('logoutUser/' , views.logoutUser , name='logoutUser'),
    path('userProfile/' , views.userProfile, name='userProfile'),
    path('addRecipe/', views.addRecipe , name='addRecipe'),
    path('yourRecipe/', views.yourRecipe , name='yourRecipe'),
    path('recipePage/<int:pk>/', views.recipePage , name='recipePage'),

    path('delete_recipe/<int:pk>/', views.delete_recipe , name='delete_recipe'),

    path('activate/<uidb64>/<token>/' , views.activate , name='activate'),

    path('forgot_password/' ,views.forgot_password , name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>' ,views.reset_password_validate , name='reset_password_validate'),
    path('reset_password/' ,views.reset_password , name='reset_password'),
]