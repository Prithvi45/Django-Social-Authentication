from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	email = models.EmailField(null=True)
	bio = models.TextField(null=True)
	city = models.CharField(max_length=250, null=True, blank=True)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
	def __unicode__(self):
		return u'%s profile' % self.user.username