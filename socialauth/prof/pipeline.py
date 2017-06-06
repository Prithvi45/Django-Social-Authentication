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
    print "im here"
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
            elif backend.name=='google-oauth2':
                print "im google"
                # print backend.name
                # print response
                # print response['emails']
                print response['displayName']
                email_list = response['emails']
                email_dict = email_list[0]
                # print email_dict['value']
                image =response['image']
                # print image['url']
                UP = UserProfile.objects.create(user=user,email=email_dict['value'],imgurl=image['url'])
                UP.save()
            else:
                print "another backend"
                print response['access_token']
                print user.uid            
        else:
            print "old user"
            print backend.namer
            print response
            print response['emails']
            print response['displayName']
            email_list = response['emails']
            email_dict = email_list[0]
            print email_dict['value']
            image =response['image']
            print image['url']

    else:
        pass

