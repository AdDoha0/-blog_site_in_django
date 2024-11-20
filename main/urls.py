from django.urls import path

from main import views


app_name = "main"


urlpatterns = [
    path("all/", views.PostsView.as_view(), name="all_posts"),  # Общее представление постов
    path("category/<slug:cat_slug>/", views.PostsView.as_view(), name="category_posts"),  # Представление постов по категории
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),  # Представление отдельного поста
    path('addpost/', views.AddPost.as_view(), name='addpost'),  # Представление отдельного поста
]