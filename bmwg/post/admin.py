from post.models import Lecture, Post
from django.contrib import admin

class WordsInline(admin.TabularInline):
	model = Post
	extra = 1

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['title']}),
	]
	inlines = [WordsInline]

admin.site.register(Lecture, PostAdmin)