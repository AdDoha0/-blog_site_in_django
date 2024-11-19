from django.urls import path

from main import views


app_name = "main"

urlpatterns = [
    path("all/", views.IndexView.as_view(), name="all_posts"),
    path("category/<slug:cat_slug>", views.CategoryPosts.as_view(), name="category"),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
]
