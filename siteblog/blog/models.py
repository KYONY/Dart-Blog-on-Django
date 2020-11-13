from django.db import models

# Create your models here.
"""
Categoty
========
title, slug

Tag
========
title, slug

Post
========
title, slug, author, content, created_at, photo, views, category, tags 
"""

class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name='Категория')
	slug = models.SlugField(max_length=255,verbose_name='Url', unique=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Категория'
		verbose_name_plural = 'Категории'
		ordering = ['title']

class Tags(models.Model):
	title = models.CharField(max_length=50, verbose_name='Тег')
	slug = models.SlugField(max_length=255,verbose_name='Url slug', unique=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Тег'
		verbose_name_plural = 'Теги'
		ordering = ['title']


class Posts(models.Model):
	title = models.CharField(max_length=255, verbose_name='Пост')
	slug = models.SlugField(max_length=255, verbose_name='Url поста', unique=True)
	author = models.CharField(max_length=100, verbose_name='Автор')
	content = models.TextField(verbose_name='Контент', blank=True)
	created_at = models.DateTimeField(auto_now=True, verbose_name='Опубликовано')
	photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
	views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
	category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
	tags = models.ManyToManyField(Tags, blank=True, related_name='posts')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Пост'
		verbose_name_plural = 'Посты'
		ordering = ['-created_at']

