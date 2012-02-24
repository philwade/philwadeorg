# Create your views here.
from philwadeorg.philblog.models import Post
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext

def index(request, page=1):
    latest_posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(latest_posts, 5)
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response('philblog/index.html', {'posts' : posts})

def detail(request, websafe_title):
    p = get_object_or_404(Post, websafe_title=websafe_title)
    post_data = { 'post' : p }
    csrfContext = RequestContext(request, post_data)
    return render_to_response('philblog/detail.html', csrfContext)
