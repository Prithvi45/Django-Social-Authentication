from django.contrib import admin
from .models import UserProfile

# Register your models here.
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user','gender']

admin.site.register(UserProfile,UserProfileAdmin)