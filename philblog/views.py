# Create your views here.
from philwadeorg.philblog.models import Post, Comment
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def index(request):
	latest_posts = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('philblog/index.html', {'latest_posts' : latest_posts})

def detail(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	return render_to_response('philblog/detail.html', {'post' : p})

def comment(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	c = Comment(body=request.POST['body'], post=p)
	c.save()
	return HttpResponseRedirect(reverse('philwadeorg.philblog.views.detail', args=(p.id,)))
