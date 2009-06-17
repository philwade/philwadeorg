from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(User)
	def __unicode__(self):
		return self.title
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
