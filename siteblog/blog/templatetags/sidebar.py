from django import template
from blog.models import Posts, Tags

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_posts(count=3):
	posts = Posts.objects.order_by('-views')[:count]
	return {'posts': posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
	tags = Tags.objects.all()
	return {'tags': tags}


# @register.inclusion_tag('blog/search_tpl.html')
# def search():
# 	tags = Tags.objects.all()
# 	return {'tags': tags}
