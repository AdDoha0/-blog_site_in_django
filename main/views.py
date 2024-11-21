from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



from main.forms import AddPostForm

from .models import Post


class PostsView(ListView):
    template_name = 'main/index.html'  # Укажите путь к вашему шаблону
    context_object_name = "posts"
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        # Получаем параметр cat_slug из URL
        cat_slug = self.kwargs.get("cat_slug")
        if cat_slug:
            # Если cat_slug присутствует, фильтруем посты по категории
            return Post.objects.filter(cat__slug=cat_slug).select_related("cat").order_by('-time_create')
        # Если cat_slug отсутствует, возвращаем все посты
        return Post.objects.all().select_related("cat").order_by('-time_create')

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





class AddPost(LoginRequiredMixin, CreateView):
    template_name = "main/createpost.html"
    form_class = AddPostForm
    success_url = reverse_lazy('main:all_posts')
    login_url = reverse_lazy('users:login')