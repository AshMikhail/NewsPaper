from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'categoryType', 'title', 'dateCreation')
    list_filter = ('author', 'categoryType', 'dateCreation')

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryThrough', 'postThrough')

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'category')

admin.site.register(Category)
admin.site.unregister(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Subscriber, SubscriberAdmin)