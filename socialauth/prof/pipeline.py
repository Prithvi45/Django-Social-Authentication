import datetime
from .models import UserProfile
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
# User details pipeline
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen

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

            img_url = response['avatar_url']

            if backend.name =='github':
                UP=UserProfile.objects.create(user=user,bio=response['bio'],email=response['email'],city=response['location'])
                UP.save()
                UP = UserProfile()
                # Save image
                image_url = response['avatar_url']
                img_temp = NamedTemporaryFile()
                img_temp.write(urlopen(image_url).read())
                img_temp.flush()
                UP.photo.save("image_%s" % UP.pk, File(img_temp))
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
    else:
        pass