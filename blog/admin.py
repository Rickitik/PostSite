from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')  # поиск по заголовку и тексту
	prepopulated_fields = {'slug': ('title', )}  # автозаполнение slug при создании поста
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')

