import datetime
from .models import UserProfile
# User details pipeline

def user_details(backend, details, response, user=None, *args, **kwargs):
    print backend
    if user:
        if kwargs['is_new']:
            attrs = {'user': user}
            print user
            print type(response)
            for k,v in response.items():
                print k,v
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