from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from prof.models import UserProfile


# Create your views here.
@login_required
def home(request):
	print "welcome"
	userprofile = UserProfile.objects.get(user=request.user)
	return render(request,'home.html',locals())

def index(request):
	print "welcome"
	return render (request,'index.html',locals())