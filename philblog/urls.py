from django.conf.urls.defaults import *

urlpatterns = patterns('philwadeorg.philblog.views',
	(r'^$', 'index'),
	(r'^post/(?P<websafe_title>.*)/$', 'detail'),
)
