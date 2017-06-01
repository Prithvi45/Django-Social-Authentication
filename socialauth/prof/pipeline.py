import datetime
from .models import UserProfile
from social.apps.django_app.default.models import UserSocialAuth
import urllib
import json
from urllib import urlopen
from django.shortcuts import render
import requests
import json
# from django.core.files import File
# from django.core.files.temp import NamedTemporaryFile
# User details pipeline
# from django.core.files import File
# from django.core.files.temp import NamedTemporaryFile
# from urllib.request import urlopen

def user_details(backend, details, response, user=None, *args, **kwargs):
    print backend.name
    if user:
        if kwargs['is_new']:
            attrs = {'user': user}
            # print user
            # print type(response)
            # print response['avatar_url']
            # print user
            # print response['bio']
            # print response['email']
            # print response['location']
            # print response
            # print user
            # img_url = response['avatar_url']

            if backend.name =='github':
                UP=UserProfile.objects.create(user=user,bio=response['bio'],email=response['email'],city=response['location'],imgurl=response['avatar_url'])
                UP.save()

            elif backend.name =='facebook':
                print "FacebookOAuth2"
                up = UserSocialAuth.objects.get(user=user)
                url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
                data = requests.get('https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cemail%2cabout&access_token={token}'.format(token=response['access_token']))
                j = json.loads(data.text)
                print j
                print j['name']
                print j['email']
                print j['about']
                UP = UserProfile.objects.create(user=user,bio=j['about'],imgurl=url,email=j['email'])
            else:
                print "another backend"
                print response['access_token']
                print user.uid            
        else:
            print "old user"
            up = UserSocialAuth.objects.get(user=user)
            print up.uid
            print up.extra_data['access_token']
            print response['access_token']
            # print user.email
            # print response
            url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
            # data ="http://graph.facebook.com/%s/me?fields=id,name,email" % response['id']
            # data = "https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cemail&access_token={token}".format(token=response['access_token'])
            print url
            data = requests.get('https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cemail%2cabout&access_token={token}'.format(token=response['access_token']))
            j = json.loads(data.text)
            print j
            print j['name']
            print j['email']
            print j['about']


    else:
        pass


# EAAYo5GTe8oYBAEV8zzFbM0w4VibqoAk4iy86p6kfXzXISXMSVrax8pZBm5lZBmMgtgHl7hvGOKniJIxzMFn9GpfTJeV8XVXiLi8yZBe2u73VzEjn3nY9D7pPz8HYa9b6ugb8GZAfciQXTHBkzr1rzaftZAuP9jgIZD
# EAAYo5GTe8oYBAL9zxJPC8Bm7SOTWAurowqt8Ey8aGE9gZABF5t0YjiWrZA9NuafjCvQVhGBNVQfSwuUkqdJf9ZCbyzbVlKcNy1H292JUTWCvMp7rMmd7EJeofZAdmU3ELNDAZAUfcoUiIDfQCkbtYx6mQ5rIBPvMZD