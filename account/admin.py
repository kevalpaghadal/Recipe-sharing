from django.contrib import admin
from .models import User , AddRecipe , Review
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# admin site password nonedit and display which field are show
class CustomUserAdmin(UserAdmin):
    list_display = ('email' , 'first_name' , 'last_name' , 'username' , 'is_active')
    ordering = ('-date_joined',) # - means descending order
    # list_display_links = ('email' , 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User , CustomUserAdmin)

admin.site.register(AddRecipe)
admin.site.register(Review)