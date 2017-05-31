import datetime
from .models import UserProfile
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
# User details pipeline
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
# from urllib.request import urlopen

def user_details(backend, details, response, user=None, *args, **kwargs):
    print backend.name
    if user:
        if kwargs['is_new']:
            attrs = {'user': user}
            # print user
            print type(response)
            print response['avatar_url']
            print user
            print response['bio']
            print response['email']
            print response['location']
            print response
            print user

            img_url = response['avatar_url']

            if backend.name =='github':
                UP=UserProfile.objects.create(user=user,bio=response['bio'],email=response['email'],city=response['location'],imgurl=response['avatar_url'])
                UP.save()
            else:
                print "another backend"
            
            # UserProfile.objects.create(user=user,gender=['user']['gender'],locale=['user']['locale'])
            # if backend.name == 'facebook':
            # if strategy.backend.__class__.__name__ == 'FacebookOAuth2':
            #     fb_data = {
            #     'city': response['location']['name'],
            #     'gender': response['gender'],
            #     'locale': response['locale'],
            #     'dob': datetime.fromtimestamp(mktime(strptime(response['birthday'], '%m/%d/%Y')))
            #     }
            #     print fb_data
            #     attrs = dict(attrs.items() + fb_data.items())
            #     up = UserProfile.objects.create(**attrs)
            #     up.save()
            #     return render(request,'home.html',locals())
        else:
            print "old user"
            print user
            print type(user)
            print str(user)
            nam = str(user)
            print nam
            print type(nam)
    else:
        pass



# github
# <type 'dict'>
# https://avatars3.githubusercontent.com/u/22132006?v=3
# Prithvi45
# Python Programmer
# pruthvimane5151@gmail.com
# Bangalore
# {u'bio': u'Python Programmer', u'site_admin': False, u'subscriptions_url': u'https://api.github.com/users/Prithvi45/subs
# criptions', u'token_type': u'bearer', u'gravatar_id': u'', u'hireable': None, u'id': 22132006, u'followers_url': u'https
# ://api.github.com/users/Prithvi45/followers', u'following_url': u'https://api.github.com/users/Prithvi45/following{/othe
# r_user}', u'blog': u'', u'followers': 4, u'location': u'Bangalore', u'scope': u'', u'type': u'User', u'email': u'pruthvi
# mane5151@gmail.com', u'public_repos': 10, u'events_url': u'https://api.github.com/users/Prithvi45/events{/privacy}', u'c
# ompany': u'@zekelabs ', u'gists_url': u'https://api.github.com/users/Prithvi45/gists{/gist_id}', u'html_url': u'https://
# github.com/Prithvi45', u'updated_at': u'2017-05-30T20:08:33Z', u'received_events_url': u'https://api.github.com/users/Pr
# ithvi45/received_events', u'starred_url': u'https://api.github.com/users/Prithvi45/starred{/owner}{/repo}', u'public_gis
# ts': 0, u'name': u'Prithviraj Mane', u'organizations_url': u'https://api.github.com/users/Prithvi45/orgs', u'access_toke
# n': u'e39fe69e3908490a14d134c505ccdcf6f0849265', u'created_at': u'2016-09-11T14:09:07Z', u'url': u'https://api.github.co
# m/users/Prithvi45', u'avatar_url': u'https://avatars3.githubusercontent.com/u/22132006?v=3', u'repos_url': u'https://api
# .github.com/users/Prithvi45/repos', u'following': 1, u'login': u'Prithvi45'}
# Prithvi45
# [31/May/2017 17:03:04]"GET /oauth/complete/github/?redirect_state=Jt3UiWo4ygPeCNNSc7YVc28lomKzRQrG&code=143cbe329a00032b
# 77cb&state=Jt3UiWo4ygPeCNNSc7YVc28lomKzRQrG HTTP/1.1" 302 0
# welcome
# [31/May/2017 17:03:04]"GET / HTTP/1.1" 200 224