from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
	GENDERS = (
		('male', 'Male'),
        ('female', 'Female')
        )
	user = models.OneToOneField(User, unique=True)
	gender = models.CharField(max_length=20, null=True, blank=True,choices=GENDERS)
	city = models.CharField(max_length=250, null=True, blank=True)
	dob = models.DateField(blank=True, null=True)
	locale = models.CharField(max_length=10, blank=True, null=True)
	def __unicode__(self):
		return u'%s profile' % self.user.username