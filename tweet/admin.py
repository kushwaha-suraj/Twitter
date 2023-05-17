from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile,tweet
# Register your models here.

#Unregister Groups 
admin.site.unregister(Group)

# mix profile info to user info
class ProfileInline(admin.StackedInline):
    model = Profile

#Extend User Model
class UserAdmin(admin.ModelAdmin):
    model=User
    #just display username field on admin page
    fields=['username']
    inlines= [ProfileInline]
    
#unregister initial user
admin.site.unregister(User)

#Re-register initial user and profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

#register a tweet
admin.site.register(tweet)
