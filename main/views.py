from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Post


class IndexView(ListView):
    template_name = 'main/index.html'
    context_object_name  = "posts"
    allow_empty = False

    def get_queryset(self):
        return Post.objects.all().select_related("cat").order_by('-time_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['featured_post'] = Post.objects.get(is_featured=True)
        except Post.DoesNotExist:
            context['featured_post'] = None  # Если нет избранного поста
        return context


class CategoryPosts(ListView):
    template_name = 'main/category.html'
    context_object_name  = "posts"
    allow_empty = False

    def get_queryset(self, **kwargs):
        return Post.objects.filter(cat__slug=self.kwargs["cat_slug"]).select_related("cat").order_by('-time_create')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['featured_post'] = Post.objects.get(is_featured=True)
        except Post.DoesNotExist:
            context['featured_post'] = None  # Если нет избранного поста
        return context


class ShowPost(DetailView):
    model = Post
    template_name = 'main/showpost.html'
    slug_url_kwarg = 'post_slug'
    slug_field = 'slug'
    context_object_name = 'post'