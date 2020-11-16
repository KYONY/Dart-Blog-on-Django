from django.db import models

# Create your models here.
from django.urls import reverse

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
	slug = models.SlugField(max_length=255,verbose_name='Slug', unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category', kwargs={'slug':self.slug})

	class Meta:
		verbose_name='Категория'
		verbose_name_plural = 'Категории'
		ordering = ['title']

class Tags(models.Model):
	title = models.CharField(max_length=50, verbose_name='Тег')
	slug = models.SlugField(max_length=255,verbose_name='Slug', unique=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Тег'
		verbose_name_plural = 'Теги'
		ordering = ['title']

	def get_absolute_url(self):
		return reverse('tag', kwargs={'slug': self.slug})


class Posts(models.Model):
	title = models.CharField(max_length=255, verbose_name='Пост')
	slug = models.SlugField(max_length=255, verbose_name='Slug', unique=True)
	author = models.CharField(max_length=100, verbose_name='Автор')
	content = models.TextField(verbose_name='Контент', blank=True)
	created_at = models.DateTimeField(auto_now=True, verbose_name='Опубликовано')
	photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
	views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
	category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
	tags = models.ManyToManyField(Tags, blank=True, related_name='posts')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post', kwargs={'slug':self.slug})

	class Meta:
		verbose_name='Статья(ю)'
		verbose_name_plural = 'Статьи'
		ordering = ['-created_at']


#TODO - создать таблицы для главного поста + для второго - внедрить в шаблон
class MainPost(models.Model):
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	content = models.TextField(verbose_name='Содержание', blank=True)
	photo = models.ImageField(upload_to='photo/main_post/', blank=True, verbose_name='Фото')
	created_at = models.DateTimeField(auto_now=True, verbose_name='Опубликовано')


	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Главный пост'
		verbose_name_plural = 'Главный пост'
		ordering = ['-created_at']



