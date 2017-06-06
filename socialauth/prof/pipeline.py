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
            # UP = UserProfile.objects.create(user=user,full_name=response['displayName'],email=email_dict['value'],img_url=image['url'])
            # up = UserSocialAuth.objects.get(user=user)
            # print up.uid
            # print up.extra_data['access_token']
            # print response['access_token']
            # # print user.email
            # # print response
            # url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
            # # data ="http://graph.facebook.com/%s/me?fields=id,name,email" % response['id']
            # # data = "https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cemail&access_token={token}".format(token=response['access_token'])
            # print url
            # data = requests.get('https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cemail%2cabout&access_token={token}'.format(token=response['access_token']))
            # j = json.loads(data.text)
            # print j
            # print j['name']
            # print j['email']
            # print j['about']


    else:
        pass


        # EAAaAJvSTd90BABePloB6ZAdwI9YLd9ZCJZCSHnTT1fA75GNJFNeoUe3l9GbIImlAm1tTyeAwnv2BXS34pcUI89ZABbzVg3TcAI69S37PisZBP2zZBDInXuFyQU4S2fhbCyc4SKHh0LSsyZCPQ7PKspTMqZANu7NC9MYZD


# pruthvimane5151
# {u'id_token': u'eyJhbGciOiJSUzI1NiIsImtpZCI6IjJmODRiYWU5NTIwYzA5NTQ0NjFkZTUwYjA2MTE1ZDI1MzliOGEyMWIifQ.eyJhenAiOiI3MzM1M
# jkxOTYzMTktbjJqNjhzaHVxOGhjcDVobTk5bHNvcGM2NWxoZnByZjMuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI3MzM1MjkxOTYzMTktb
# jJqNjhzaHVxOGhjcDVobTk5bHNvcGM2NWxoZnByZjMuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDA4NzQ0MTg3MjU3MTQ0Nzk2ODAiL
# CJlbWFpbCI6InBydXRodmltYW5lNTE1MUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IkI1U0RjWnpveTRPNDhmYzg0eVJUT
# lEiLCJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiaWF0IjoxNDk2Njc2NzkxLCJleHAiOjE0OTY2ODAzOTF9.t6k9v4ubcFy4mPytIp4OmAPVGr2T6Fs9
# pJNB8qattxUrhEGNJcP0Cise2wDan7dmevdIyL6MVALZKqSNWusmrNybsOScK-6W_4f3Nu6HxVLJ00DGvlmKYYJCweK3Sq3XKrTOj3az8PJZUc-Rtc3Ih_wG
# wHbN2O4GeNvbSQOQsltoGLJwwNz7VqylUjmMy61vXnySS0KOmySWMYx9BXyr13N9ud46vKNIId7dhrOIrekTv1vzABYjiNIhPCd9nj3GtlbXmr78-6kyQXHT
# zOrqe-g396zLPQ4YKS5OWeNDdJ_lhCWkfuZBc3uoVV6C5XTwpt2sNAFSmcT_TIShdtOaRg', u'image': {u'url': u'https://lh4.googleusercont
# ent.com/-tl-qmFO_C8k/AAAAAAAAAAI/AAAAAAAAAH4/PKfPKSQPl_E/photo.jpg?sz=50', u'isDefault': False}, u'relationshipStatus':
# u'single', u'token_type': u'Bearer', u'etag': u'"Sh4n9u6EtD24TM0RmWv7jTXojqc/Tr8kQAoj8o1M4OVnRvlEf2hOCHI"', u'verified':
#  False, u'emails': [
#  {u'type': u'account', u'value': u'pruthvimane5151@gmail.com'}
#  ], u'objectType': u'person', u'organiza
# tions': [{u'startDate': u'2012', u'endDate': u'2015', u'name': u'Shree Guru Gobind Singhji Institute of Engineering & Te
# chnology', u'title': u'B.Tech', u'primary': False, u'type': u'school'}, {u'startDate': u'2009', u'endDate': u'2012', u'n
# ame': u'Brahmdevdada Mane Polytechnic, Solapur.', u'title': u'Diploma', u'primary': False, u'type': u'school'}, {u'start
# Date': u'1999', u'type': u'school', u'name': u'Shree Shardamata English Medium High School, Akkalkot', u'endDate': u'200
# 9', u'primary': False}], u'kind': u'plus
# person', u'displayName': u'Prithviraj Mane', u'name': {u'givenName': u'Prithvir
# aj', u'familyName': u'Mane'}, u'language': u'en', u'access_token': u'ya29.GltgBEngLnHp1aKxreqUyg0Zq55s-au_FQ-Kdc5f1hLAPc
# 8HPFS87uKp1OPLMt_YBr14CCs4S3VyNl7VTKEMaRV5nL0V6yy6s9kSc_TxY7gu-KwhxaSty8De-4KX', u'gender': u'male', u'expires_in': 3599
# , u'id': u'100874418725714479680', u'url': u'https://plus.google.com/100874418725714479680', u'isPlusUser': True, u'circ
# ledByCount': 4}