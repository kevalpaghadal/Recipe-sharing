"""
URL configuration for RSW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "Recipe Sharing Administration"
admin.site.site_title = "Recipe Sharing Administration"
admin.site.index_title = "Welcome to Recipe Sharing"

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls , name='admin'),
    path('' , views.home, name='home'),
    path('homePageRecipe/<int:pk>/' , views.homePageRecipe, name='homePageRecipe'),
    path('account/', include('account.urls')),
    path('srcRecipe/' , views.srcRecipe , name='srcRecipe'),
    path('srcRecipePage/<int:pk>' , views.srcRecipePage , name='srcRecipePage'),
    path('formSearch/' , views.formSearch , name='formSearch'),
    path('ShowFormRecipe/' , views.ShowFormRecipe , name='ShowFormRecipe'),
    path('printRecipe/<int:pk>' , views.printRecipe , name='printRecipe'),


    path('contact_us', views.contact_us, name='contact_us'),
    path('about_us', views.about_us, name='about_us'),
    path('team', views.team, name='team'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
