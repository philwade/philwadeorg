from django.conf.urls.defaults import *
from philwadeorg.lib.feeds import LatestPosts

feeds = {
	'latest':LatestPosts,
}
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^philwadeorg/', include('philwadeorg.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	(r'', include('philwadeorg.philblog.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', 
		{'feed_dict':feeds}),
    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
