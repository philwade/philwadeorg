from django.contrib.syndication.feeds import Feed
from philwadeorg.philblog.models import Post

class LatestPosts(Feed):
	title = "phil wade dot org latest posts"
	link = "/"
	description = "Latest posts about code, cats and life"

	def items(self):
		return Post.objects.order_by('-pub_date')[:5]
