from django.conf.urls.defaults import *

urlpatterns = patterns('philwadeorg.philblog.views',
	(r'^$', 'index'),
	(r'^post/(?P<post_id>\d+)/$', 'detail'),
	(r'^post/(?P<post_id>\d+)/comment/$', 'comment'),
)
