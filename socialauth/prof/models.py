from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
import os


class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	email = models.EmailField(null=True)
	bio = models.TextField(null=True)
	city = models.CharField(max_length=250, null=True, blank=True)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
	imgurl = models.URLField(null=True)

	def __unicode__(self):
		return u'%s profile' % self.user.username

	def get_remote_image(self):
		if self.imgurl and not self.photo:
			print "im here"
			result = urllib.urlretrieve(self.imgurl)
			self.photo.save(os.path.basename(self.imgurl),File(open(result[0])))
			self.save()