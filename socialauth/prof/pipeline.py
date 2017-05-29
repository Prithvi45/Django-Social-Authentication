import datetime
from .models import UserProfile
# User details pipeline

def user_details(backend, details, response, user=None, *args, **kwargs):
    if user:
        if kwargs['is_new']:
            attrs = {'user': user}
            print user
            print response
            if backend.name == 'facebook':
            # if strategy.backend.__class__.__name__ == 'FacebookOAuth2':
                fb_data = {
                'city': response['location']['name'],
                'gender': response['gender'],
                'locale': response['locale'],
                'dob': datetime.fromtimestamp(mktime(strptime(response['birthday'], '%m/%d/%Y')))
                }
                print fb_data
                attrs = dict(attrs.items() + fb_data.items())
                up = UserProfile.objects.create(**attrs)
                up.save()
                return render(request,'home.html',locals())
        else:
            print "old user"
    else:
        pass


# def user_details(backend, user, response, *args, **kwargs):
#     if backend.name == 'facebook':
#         profile = user.get_profile()
#         if profile is None:
#             profile = Profile(user_id=user.id)
#         profile.gender = response.get('gender')
#         profile.link = response.get('link')
#         profile.timezone = response.get('timezone')
#         profile.save()

        
# def user_details(backend, user, response, details, *args, **kwargs):
#     url = None
#     profile = UserProfile.objects.get_or_create(user = user)[0]
#     if backend.name == 'facebook':
#         profile.photo  = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
#     elif backend.name == "twitter":
#         if response['profile_image_url'] != '':
#             if not response.get('default_profile_image'):
#                 avatar_url = response.get('profile_image_url_https')
#                 if avatar_url:
#                     avatar_url = avatar_url.replace('_normal.', '_bigger.')
#                     profile.photo = avatar_url
#     elif backend.name == "google-oauth2":
#         if response['image'].get('url') is not None:
#             profile.photo  = response['image'].get('url')


#     profile.save()