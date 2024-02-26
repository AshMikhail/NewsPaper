from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'all_news.html'
    context_object_name = 'all_news'


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
