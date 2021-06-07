from django.contrib import admin
from .models import Post, Comment, proxymodel

class postAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish','status','author','body','created','updated']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('body','title')
    raw_id_fields = ('author',)
    list_filter = ['status','publish','author']
    date_hierarchy = 'publish'

class commentAdmin(admin.ModelAdmin):
    list_display = ['post','name','email','body','created','updated','active']
    list_filter = ('active','name','email')
    search_fields = ('name','email')

class proxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status', 'author', 'body', 'created', 'updated']
    search_fields = ('body', 'title')

admin.site.register(Post,postAdmin)
admin.site.register(proxymodel,proxyAdmin)
admin.site.register(Comment,commentAdmin)