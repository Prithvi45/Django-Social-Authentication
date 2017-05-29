from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from prof.facebook import facebook_view
from prof import views as profviews

urlpatterns = [
    url(r'^$', profviews.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', admin.site.urls),
    # url(r'^fb/', facebook_view, name='fb_app'),
    url('', include('social_django.urls', namespace='social'))
]