from django.contrib import admin
from .models import User , AddRecipe , Review , ContactUs
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# admin site password nonedit and display which field are show
class CustomUserAdmin(UserAdmin):
    list_display = ('email' , 'first_name' , 'last_name' , 'username' , 'is_active' , 'is_admin')
    ordering = ('-date_joined',) # - means descending order
    # list_display_links = ('email' , 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'recipe_name', 'star', 'review', 'created_at')

    def user_email(self, obj):
        return obj.user.email

    def recipe_name(self, obj):
        if obj.recipe:
            return obj.recipe.title
        else:
            return "No Title"
    
    

admin.site.register(User , CustomUserAdmin)

admin.site.register(AddRecipe)


admin.site.register(Review , ReviewAdmin)

admin.site.register(ContactUs)