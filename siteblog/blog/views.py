from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Posts, Category, Tags
from django.db.models import F



class Home(ListView):
	model = Posts
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	paginate_by = 4

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Classic Blog Design'
		return context

class PostsByCategory(ListView):
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	paginate_by = 4
	allow_empty = False

	def get_queryset(self):
		return Posts.objects.filter(category__slug=self.kwargs['slug'])

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = Category.objects.get(slug=self.kwargs['slug'])
		return context



class GetPost(DetailView):
	model = Posts
	template_name = 'blog/single.html'
	context_object_name = 'post'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		self.object.views = F('views') +1
		self.object.save()
		self.object.refresh_from_db()
		return context



class PostsByTag(ListView):
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	paginate_by = 4
	allow_empty = False

	def get_queryset(self):
		return Posts.objects.filter(tags__slug=self.kwargs['slug'])

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Записи по тегу: ' + str(Tags.objects.get(slug=self.kwargs['slug']))
		return context

class Search(ListView):
	template_name = 'blog/search.html'
	context_object_name = 'posts'
	paginate_by = 4

	def get_queryset(self):
		return Posts.objects.filter(title__icontains=self.request.GET.get('search'))

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search'] = f"search={self.request.GET.get('search')}&"
		return context


# def index(request):
# 	return render(request, 'blog/index.html')


# def get_category(request, slug):
# 	return render(request, 'blog/category.html')
#
# def get_post(request, slug):
# 	return render(request, 'blog/category.html')