from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from pages.models import Post, TutoringHour

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_tutor",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", "is_tutor", "classes_can_tutor")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age", "is_tutor", "classes_can_tutor")}),
    )
    
    
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
    )


class TutoringHourAdmin(admin.ModelAdmin):
    list_display = (
        "tutor",
        "day_of_week", 
        "start_time",
        "end_time",
        "location",
        "is_active",
    )
    list_filter = ("day_of_week", "is_active", "location")
    search_fields = ("tutor__username", "tutor__first_name", "tutor__last_name")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(TutoringHour, TutoringHourAdmin)