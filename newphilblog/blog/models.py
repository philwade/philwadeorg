from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    websafe_title = models.CharField(max_length=200, editable=False)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.title
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    def save(self, force_insert=False, force_update=False):
        unclean_title = self.title
        self.websafe_title = unclean_title.replace(' ', '_').strip("'\",.").lower()
        super(Post, self).save(force_insert, force_update)
    def get_absolute_url(self):
        return "/post/%s/" % self.websafe_title

    class Meta:
        db_table = 'philblog_post'
