from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse

def verify(request):
    return HttpResponse("google-site-verification: google3ce605377dd30bad.html")

def index(request, page=1):
    latest_posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(latest_posts, 5)
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts' : posts})

def detail(request, websafe_title):
    p = get_object_or_404(Post, websafe_title=websafe_title)
    return render(request, 'blog/detail.html', {'post': p})
