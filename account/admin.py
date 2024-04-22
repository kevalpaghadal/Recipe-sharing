from django.contrib import admin
from .models import User , AddRecipe , Review , ContactUs
from django.contrib.auth.admin import UserAdmin


from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

import datetime
# Register your models here.


def download_pdf(self, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    pdf = canvas.Canvas(response, pagesize= 'A4')
    pdf.setTitle('PDF Report')
    
    # Set page color
    pdf.setFillColorRGB(0.9, 0.9, 0.9)  # Light gray
    pdf.rect(0, 0, letter[0], letter[1], fill=1)
    
    # Add a header
    pdf.setFont("Helvetica-Bold", 30)
    pdf.setFillColorRGB(0, 0, 0)  # Black
    pdf.drawString(50, 730, "RECIPE SHARING SYSTEM")
    
    # Get model name
    model_name = queryset.model._meta.verbose_name_plural.title()
    pdf.setFont("Helvetica", 20)
    pdf.drawString(50, 670, f"Report For: {model_name}")

    # get date
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")  # Format it as you need

    model_name = queryset.model._meta.verbose_name_plural.title()
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, 650, f"date : {current_date}")
    


    if isinstance(queryset.first(), User):
        headers = ['Name', 'Username', 'E-mail']  # Changed headers
        fields = ['username', 'email']  # Removed 'full_name' field
    
    data = [headers]
    
    for obj in queryset:
        full_name = f"{obj.first_name} {obj.last_name}"
        data_row = [full_name] + [str(getattr(obj, field)) for field in fields]  # Concatenate full_name and other fields
        data.append(data_row)

    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    canvas_width = 100
    canvas_height = 740
    table.wrapOn(pdf, canvas_width, canvas_height)
    table.drawOn(pdf, 50, canvas_height - len(data) * 20 - 100)  # Adjust table position
    
    pdf.save()
    return response

download_pdf.short_description = ("Download selected items as PDF")

# admin site password nonedit and display which field are show
class CustomUserAdmin(UserAdmin):
    list_display = ('email' , 'first_name' , 'last_name' , 'username' , 'is_active' , 'is_admin')
    actions = [download_pdf]
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