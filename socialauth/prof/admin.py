from django.contrib import admin
from .models import UserProfile

# Register your models here.
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user']

admin.site.register(UserProfile,UserProfileAdmin)