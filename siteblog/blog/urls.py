from django.urls import path
from .views import *

urlpatterns = [
	# path('', index, name='home'),
	path('', Home.as_view(), name='home'),
	# path('category/<str:slug>/', get_category, name='category'),
	path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
	path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
	# path('post/<str:slug>/', get_post, name='post'),
	path('post/<str:slug>/', GetPost.as_view(), name='post'),
	path('search/', Search.as_view(), name='search'),


]