"""philblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lib.feeds import LatestPosts
import blog.views as blogviews

urlpatterns = [
	url(r'^$', blogviews.index, name='index'),
    url(r'^admin/', admin.site.urls),
	url(r'^google3ce605377dd30bad.html$', blogviews.verify, name='verify'),
	url(r'^page/(?P<page>\d+)/$', blogviews.index, name='index'),
	url(r'^post/(?P<websafe_title>.*)/$', blogviews.detail, name='detail'),
	url(r'^rss/(?P<url>.*)/$', LatestPosts()),
	url(r'^projects/$', blogviews.projects),
]
